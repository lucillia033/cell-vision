import streamlit as st
import os

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="동물세포 탐험대",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 존재하는 페이지 파일들을 감지하여 네비게이션 구성
ORGANELLE_PAGES_INFO = [
    ("pages/0_메인.py", "동물세포 한눈에 보기", "🔬", "메인"),
    ("pages/1_핵.py", "핵", "🧠", "핵"),
    ("pages/2_리보솜.py", "리보솜", "⚙️", "리보솜"),
    ("pages/3_미토콘드리아.py", "미토콘드리아", "⚡", "미토콘드리아"),
    ("pages/4_소포체.py", "소포체", "📦", "소포체"),
    ("pages/5_골지체.py", "골지체", "📮", "골지체"),
    ("pages/6_리소좀.py", "리소좀", "♻️", "리소좀"),
    ("pages/7_세포막.py", "세포막", "🛡️", "세포막"),
    ("pages/8_세포질.py", "세포질", "🌊", "세포질"),
    ("pages/9_세포골격.py", "세포골격", "🏗️", "세포골격"),
]

valid_pages = []

for path, title, icon, key in ORGANELLE_PAGES_INFO:
    if os.path.exists(path):
        # 첫 번째 항목(0_메인.py)을 기본(default) 페이지로 지정
        is_default = (key == "메인")
        p_obj = st.Page(path, title=title, icon=icon, default=is_default)
        valid_pages.append(p_obj)

# 3. 사이드바 메뉴 렌더링 및 실행
if valid_pages:
    pg = st.navigation(valid_pages)
    pg.run()
else:
    st.error("`pages/` 폴더 내에 접근 가능한 페이지 파일이 없습니다.")
