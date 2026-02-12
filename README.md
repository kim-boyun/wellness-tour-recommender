# Wellness Tour Recommend System

한국 웰니스(힐링) 관광 맞춤 추천 대시보드입니다.  
로그인 후 7문항 설문으로 관광 성향을 분류하고, 그에 맞는 웰니스 관광지를 추천·지도·통계로 확인할 수 있습니다.

---

## 기술 스택

- **Python 3** · **Streamlit** (웹 대시보드)
- **pandas**, **numpy**, **scikit-learn** (데이터 처리·클러스터링)
- **Plotly** (차트), **Folium** (지도)
- **SQLite** (사용자 DB), **reverse_geocoder** (좌표→지역)

---

## 프로젝트 구조

```
recommend_DashBoard/
├── app.py                 # 진입점 (로그인/회원가입)
├── config.py              # 설정 (경로, 페이지명, 테스트 계정)
├── utils.py               # 공통 유틸 (접근 권한, 데이터 로드, 추천·차트·내보내기)
├── requirements.txt
├── README.md
├── .devcontainer/
├── core/                   # 공통 모듈
│   ├── constants.py       # 설문 문항(QUESTIONS), 클러스터 메타(get_cluster_info)
│   └── styles.py          # 전역 CSS (apply_global_styles)
├── data/
│   ├── wellness_tourism_list.csv
│   ├── wellness_cluster_score.csv
│   ├── wellness_nearby_spots_list.csv
│   ├── category_map.csv
│   ├── category_counts.csv
│   ├── korean_tourism_list.csv
│   ├── region_data.csv
│   └── wellness_users.db
└── pages/
    ├── 01_survey.py
    ├── 02_analysis.py
    ├── 03_home.py
    ├── 04_recommendations.py
    ├── 05_map.py
    └── 06_statistics.py
```

---

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

- 테스트 계정: **wellness** / **1234**

---

## 주요 기능

| 페이지 | 설명 |
|--------|------|
| 로그인 | 회원가입·로그인 (SQLite) |
| 01 설문 | 7문항 웰니스 성향 설문 |
| 02 분석 | 설문 기반 클러스터 분석 |
| 03 홈 | 대시보드 진입·메뉴 |
| 04 추천 | 클러스터별 웰니스 관광지 추천, 필터·차트 |
| 05 지도 | Folium 기반 추천 장소 지도 |
| 06 통계 | 추천·사용 통계 요약 |
