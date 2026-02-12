# Wellness Tour Recommender

한국 웰니스(힐링) 관광 맞춤 추천 시스템입니다.  
2025년 관광지식정보시스템·관광데이터 분석 공모전 **장려상** 수상 프로젝트입니다. 외래관광객조사 데이터를 기반으로 군집분석을 수행하고, 설문을 통해 사용자 성향을 분류하여 맞춤형 웰니스 관광지를 추천합니다.

---

## 프로젝트 구조

```
wellness-tour-recommender/
├── app/                      # Streamlit 웹 앱
│   ├── app.py                # 진입점 (로그인/회원가입)
│   ├── config.py             # 설정 (경로, 페이지, 테스트 계정)
│   ├── utils.py              # 공통 유틸 (데이터 로드, 추천, 차트)
│   ├── core/
│   ├── data/                 # 앱용 데이터
│   └── pages/
│
├── analysis/                 # 데이터 분석
│   ├── notebooks/            # Jupyter 노트북
│   ├── data/                 # raw, processed, gis
│   └── output/               # 분석 결과 (cluster_profile 등)
│
├── report/                   # 프로젝트·공모전 관련 문서
│   ├── 결과보고서.pdf
│   ├── 관광데이터분석공모전.jpeg  # 공모전 공고 포스터
│   ├── 분석활용 데이터 정보.pdf
│   └── 웰커밍_ppt기획.pdf
│
├── reference/                # 참고 자료 (2024 수상작, 인바운드 전략 등)
│
├── requirements.txt
└── README.md
```

---

## 기술 스택

| 구분 | 도구 |
|------|------|
| 웹 앱 | Python, Streamlit |
| 데이터 처리 | pandas, numpy, scikit-learn |
| 시각화 | Plotly, Folium |
| DB | SQLite (사용자) |
| 분석 | statsmodels, gower, kmodes, XGBoost, LightGBM |

---

## 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 웹 앱 실행

```bash
streamlit run app/app.py
```

- **테스트 계정**: `wellness` / `1234`

### 3. 데이터 분석 (선택)

Jupyter에서 `analysis/notebooks/` 내 노트북을 순서대로 실행합니다.

- `01_preprocessing.ipynb` → `02_difference_test.ipynb` → `03_feature_selection.ipynb` → `04_fa_clustering.ipynb`

> 노트북은 `analysis/notebooks/` 디렉터리 기준으로 상대 경로를 사용합니다.

---

## 주요 기능

| 페이지 | 설명 |
|--------|------|
| 로그인 | 회원가입·로그인 (SQLite) |
| 01 설문 | 7문항 웰니스 성향 설문 |
| 02 분석 | 설문 기반 클러스터 분석 |
| 03 홈 | 대시보드 진입·메뉴 |
| 04 추천 | 클러스터별 웰니스 관광지 추천 |
| 05 지도 | Folium 기반 추천 장소 지도 |
| 06 통계 | 추천·사용 통계 |

---

## 데이터 흐름

1. **분석** (`analysis/`): 외래관광객조사 원본 → 전처리 → 특징선택 → 군집분석 → 클러스터 프로파일
2. **앱** (`app/`): 설문 응답으로 클러스터 매칭 → 웰니스 관광지 추천 및 지도·통계 표시

---

## 라이선스

LICENSE 파일을 참조하세요.
