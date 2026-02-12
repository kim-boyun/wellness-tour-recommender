"""
전역 CSS 및 스타일 적용.
Streamlit 앱 공통 테마를 한 곳에서 관리합니다.
"""
import streamlit as st

GLOBAL_CSS = """
<style>
    /* 전역 스타일 변수 - 밝은 테마 */
    :root {
        --primary: #3498DB;
        --primary-dark: #2980B9;
        --primary-light: #5DADE2;
        --secondary: #2ECC71;
        --accent: #E74C3C;
        --background: #F8F9FA;
        --card-bg: rgba(255, 255, 255, 0.95);
        --text-primary: #2C3E50;
        --text-secondary: #34495E;
        --border-color: rgba(52, 152, 219, 0.2);
        --shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        --shadow-hover: 0 8px 25px rgba(52, 152, 219, 0.15);
    }
    
    .stApp {
        background: linear-gradient(135deg, #F8F9FA 0%, #E8F4FD 50%, #D6EAF8 100%);
        min-height: 100vh;
    }
    
    [data-testid="stAppViewContainer"] > .main {
        background: transparent;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .main .block-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem 1.5rem !important;
    }
    
    .card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-hover);
        border-color: var(--primary);
    }
    
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, var(--primary), var(--primary-light)) !important;
        border: none !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(52, 152, 219, 0.2) !important;
        font-size: 14px !important;
        letter-spacing: 0.5px !important;
    }
    
    div[data-testid="stButton"] > button:hover {
        background: linear-gradient(135deg, var(--primary-dark), var(--primary)) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 16px rgba(52, 152, 219, 0.3) !important;
    }
    
    .main h1, .main h2, .main h3 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
    }
    
    .main p, .main span, .main div {
        color: var(--text-secondary) !important;
    }
    
    div[data-testid="stTextInput"] > div > div > input,
    div[data-testid="stSelectbox"] > div > div > div {
        border: 2px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 12px !important;
        background: white !important;
        color: var(--text-primary) !important;
        font-size: 14px !important;
    }
    
    div[data-testid="stTextInput"] > div > div > input:focus,
    div[data-testid="stSelectbox"] > div > div > div:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1) !important;
    }
    
    div[data-testid="stRadio"] > div { gap: 12px !important; }
    
    div[data-testid="stRadio"] label {
        background: white !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        margin: 0 !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        min-height: 60px !important;
        display: flex !important;
        align-items: center !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05) !important;
    }
    
    div[data-testid="stRadio"] label:hover {
        transform: translateY(-1px) !important;
        border-color: var(--primary) !important;
        box-shadow: 0 4px 16px rgba(52, 152, 219, 0.15) !important;
    }
    
    div[data-testid="stRadio"] input:checked + div {
        background: rgba(52, 152, 219, 0.05) !important;
        border-color: var(--primary) !important;
        box-shadow: 0 4px 16px rgba(52, 152, 219, 0.2) !important;
        transform: translateY(-1px) !important;
    }
    
    div[data-testid="stAlert"] {
        border-radius: 12px !important;
        border: none !important;
        box-shadow: var(--shadow) !important;
        margin: 16px 0 !important;
    }
    
    .stSuccess { background: rgba(46, 204, 113, 0.1) !important; color: #27AE60 !important; }
    .stError { background: rgba(231, 76, 60, 0.1) !important; color: #E74C3C !important; }
    .stWarning { background: rgba(243, 156, 18, 0.1) !important; color: #F39C12 !important; }
    .stInfo { background: rgba(52, 152, 219, 0.1) !important; color: var(--primary) !important; }
    
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, var(--primary), var(--secondary)) !important;
        border-radius: 8px !important;
        height: 12px !important;
    }
    
    div[data-testid="stProgress"] > div {
        background: rgba(52, 152, 219, 0.1) !important;
        border-radius: 8px !important;
        height: 12px !important;
    }
    
    [data-testid="stHeader"] { display: none; }
    [data-testid="stSidebarNav"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    footer { display: none; }
    
    @media (max-width: 768px) {
        .main .block-container { padding: 1rem !important; }
        .card { margin: 12px 0; padding: 16px; }
    }
</style>
"""


def apply_global_styles():
    """밝은 테마 전역 CSS 스타일 적용"""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
