import csv, html, requests

# ------------------------------------------------
# 1) 공통 설정
# ------------------------------------------------
ENDPOINT = "https://korean.visitkorea.or.kr/call"
OTDID    = "287776d6-8939-11e8-8165-020027310001"   # 우수 웰니스 관광지 ID
HEADERS  = {"User-Agent": "Mozilla/5.0"}
CNT_PER_PAGE = 10

# ------------------------------------------------
# 2) 상세 URL 생성 ─ contentType → 경로 매핑
#    ※ 핵심 패치: ctype = str(ctype) 로 문자열화
# ------------------------------------------------
def build_url(cotid, ctype, cat1, cat2, area):
    ctype = str(ctype)            # ←★ 정수도 문자열로 통일
    if ctype == "12":             # 관광지
        return (f"https://korean.visitkorea.or.kr/detail/ms_detail.do?"
                f"cotid={cotid}&big_category={cat1}&mid_category={cat2}&big_area={area}")
    if ctype == "15":             # 축제
        return (f"https://korean.visitkorea.or.kr/detail/fes_detail.do?"
                f"cotid={cotid}&big_category={cat1}&mid_category={cat2}&big_area={area}")
    if ctype in {"25", "25000"}:  # 코스
        return f"https://korean.visitkorea.or.kr/detail/cs_detail.do?cotid={cotid}"
    if ctype == "30000":          # 이벤트
        return f"https://korean.visitkorea.or.kr/detail/event_detail.do?cotid={cotid}"
    # 그 밖(문화·숙박·레포츠·쇼핑·음식 등)
    return f"https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid={cotid}&con_type={ctype}"

# ------------------------------------------------
# 3) 페이지 루프 수집
# ------------------------------------------------
records, page = [], 1
while True:
    payload = {
        "cmd"          : "OTHER_SERVICE_LIST_VIEW",
        "otherkind"    : "well25",
        "otdid"        : OTDID,
        "page"         : str(page),
        "cnt"          : str(CNT_PER_PAGE),
        # 기본 필터
        "areaCode": "All", "sigunguCode": "All",
        "tagId": "All", "othertagyear": "All",
        "othertag": "Null", "othermoretag": "All",
        "locationx": "", "locationy": "",
        "bfreetitleKind": "All", "bfreetourKind": "All",
        "searchtype": "All",
    }

    resp = requests.post(ENDPOINT, data=payload, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    items = resp.json()["body"].get("content", [])
    if not items:
        break

    for it in items:
        title = html.unescape(it["title"])
        url   = build_url(
            it["cotId"], it["contentType"],
            it.get("cat1", ""), it.get("cat2", ""), it.get("areaCode", "")
        )
        records.append((
            title,
            url,
            it.get("areaCode", ""),
            it.get("sigunguCode", ""),
            it["contentType"]
        ))
        print(f"[{page:02}] {title}")

    page += 1

print(f"\n총 {len(records)}건 수집 완료")

# ------------------------------------------------
# 4) CSV 저장
# ------------------------------------------------
with open("wellness_list_urls.csv", "w", newline="", encoding="utf-8-sig") as f:
    csv.writer(f).writerows(
        [("title", "url", "areaCode", "sigunguCode", "contentType"), *records]
    )

print("CSV 저장: wellness_list_urls.csv")
