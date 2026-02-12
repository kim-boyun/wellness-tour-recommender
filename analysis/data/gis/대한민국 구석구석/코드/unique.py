import pandas as pd
import re

INPUT_CSV  = "wellness_with_addr.csv"   # 원본
OUTPUT_CSV = "wellness_unique.csv"      # 결과

# ---------- 주소 정규화 함수 ----------
def normalize(addr: str) -> str:
    """
    1) 괄호( ) 및 내부 내용 제거
    2) 마지막 숫자 블록(번지)까지만 남기고 뒤(층·호수·건물명 등) 제거
    """
    # ① 괄호 제거
    addr = re.sub(r'\([^)]*\)', '', addr).strip()
    # ② '숫자' 뒤 남는 상세 표기 제거
    m = re.match(r'^(.*?\d[\d\-]*)(?:\s.*)?$', addr)
    return m.group(1).strip() if m else addr

# ---------- 작업 ----------
df = pd.read_csv(INPUT_CSV)

# 0) address 열이 NaN인 행 모두 삭제
df = df.dropna(subset=["address"]).copy()

# 1) 중복 판단용 열 생성
df["norm_addr"] = df["address"].apply(normalize)

# 2) 중복 행 제거 (동일 norm_addr 기준 첫 행만 유지)
df_unique = df.drop_duplicates(subset="norm_addr", keep="first").copy()

# 3) 남은 address 열에서 괄호(+내용) 제거
df_unique["address"] = (
    df_unique["address"]
      .str.replace(r"\s*\([^)]*\)", "", regex=True)
      .str.strip()
)

# 4) 보조 열 삭제 & 저장
df_unique.drop(columns="norm_addr", inplace=True)
df_unique.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig") 

print(f"✔️ NaN 주소 제거 후 {len(df)}행, 중복 제거 후 {len(df_unique)}행을 '{OUTPUT_CSV}'에 저장했습니다.")
