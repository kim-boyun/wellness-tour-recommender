import csv, re, time, requests
from bs4 import BeautifulSoup

CSV_IN   = "wellness_list_urls.csv"   # 입력 파일
CSV_OUT  = "wellness_with_addr.csv"   # 출력 파일
ENDPOINT = "https://korean.visitkorea.or.kr/call"
HEADERS  = {"User-Agent": "Mozilla/5.0"}

# ─────────────────────────────────────────
# 1. 주소 추출 헬퍼
# ─────────────────────────────────────────
def extract_addr_from_json(data, is_article=False):
    """/call 응답 JSON → 대표 주소 한 줄 반환 (없으면 "")"""
    if not is_article:
        # 여행지‧축제‧코스 등: body.detail.addr1
        return (
            data.get("body", {})
                .get("detail", {})
                .get("addr1", "")
                .strip()
        )

    # 여행 기사(10600): '- 주소 :' 뒤 첫 <br> 앞까지만
    for art in data.get("body", {}).get("subArticle", []):
        html_body = art.get("articleBody", "")
        if "주소" not in html_body:
            continue
        m = re.search(r"주소\s*:\s*([^<]+)", html_body)
        if m:
            # &nbsp; 등 HTML 엔티티 정리
            return BeautifulSoup(m.group(1), "html.parser").get_text(" ", strip=True)
    return ""

# ─────────────────────────────────────────
# 2. 입력 CSV 순회 → 주소 수집
# ─────────────────────────────────────────
records_out = []

with open(CSV_IN, newline="", encoding="utf-8-sig") as f_in:
    rdr = csv.DictReader(f_in)
    for row in rdr:
        title = row["title"]
        url   = row["url"]
        area  = row.get("areaCode", "").strip()
        ctype = int(row.get("contentType", 0))

        # areaCode 가 0/없음 → 주소 공란
        if area == "0" or area == "":
            records_out.append((title, url, ""))
            continue

        # cotid 추출
        m = re.search(r"cotid=([0-9a-f\-]+)", url, re.I)
        if not m:
            records_out.append((title, url, ""))
            continue
        cotid = m.group(1)

        # payload 분기
        if ctype == 10600:          # 여행 기사
            payload = {
                "cmd"  : "RECOM_CONTENT_DETAIL",
                "cotid": cotid,
                "otdid": "",        # 없어도 응답됨
            }
            is_article = True
        else:                       # 여행지·축제·코스 등
            payload = {
                "cmd"      : "TOUR_CONTENT_BODY_DETAIL",
                "cotId"    : cotid,
                "locationx": "0",
                "locationy": "0",
                "stampId"  : "",
            }
            is_article = False

        # /call 요청
        try:
            resp = requests.post(ENDPOINT, data=payload,
                                 headers=HEADERS, timeout=10)
            resp.raise_for_status()
            addr = extract_addr_from_json(resp.json(), is_article)
        except Exception:
            addr = ""   # 실패 시 공란

        records_out.append((title, url, addr))
        print(f"{title} → {addr or '주소 없음'}")
        time.sleep(0.2)             # 과도한 요청 방지

# ─────────────────────────────────────────
# 3. 결과 CSV 저장
# ─────────────────────────────────────────
with open(CSV_OUT, "w", newline="", encoding="utf-8-sig") as f_out:
    csv.writer(f_out).writerows([("title", "url", "address"), *records_out])

print(f"\n완료! {len(records_out)}건을 {CSV_OUT} 에 저장했습니다.")
