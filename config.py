"""
프로젝트 공통 설정 (경로, 페이지명, 테스트 계정 등).
포트폴리오 유지보수 시 한 곳만 수정하면 되도록 중앙화.
"""
from pathlib import Path

# ---------------------------------------------------------------------------
# 경로
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "wellness_users.db"

# 데이터 파일 (문자열 경로 - pandas/Streamlit 호환)
PATH_WELLNESS_LIST = "data/wellness_tourism_list.csv"
PATH_CLUSTER_SCORE = "data/wellness_cluster_score.csv"
PATH_NEARBY_SPOTS = "data/wellness_nearby_spots_list.csv"
PATH_CATEGORY_MAP = "data/category_map.csv"

# ---------------------------------------------------------------------------
# 페이지 (Streamlit multipage)
# ---------------------------------------------------------------------------
PAGE_APP = "app.py"
PAGE_SURVEY = "pages/01_survey.py"
PAGE_ANALYSIS = "pages/02_analysis.py"
PAGE_HOME = "pages/03_home.py"
PAGE_RECOMMENDATIONS = "pages/04_recommendations.py"
PAGE_MAP = "pages/05_map.py"
PAGE_STATISTICS = "pages/06_statistics.py"

# 접근 권한용 페이지 타입 (survey = 설문/분석 전 진입 가능)
PAGE_TYPE_SURVEY = "survey"
PAGE_TYPE_HOME = "home"

# ---------------------------------------------------------------------------
# 테스트 계정 (개발/데모용)
# ---------------------------------------------------------------------------
TEST_USER = "wellness"
TEST_PASSWORD = "1234"
