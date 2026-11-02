import streamlit as st
from pathlib import Path  # 파일과 폴더의 경로를 쉽게 관리하기 위한 모듈
from datetime import datetime  # 현재 날짜와 시간을 가져오기 위한 모듈

# =========================================================
# 1. 기본 설정
# =========================================================

# Streamlit 페이지의 제목, 레이아웃, 사이드바 초기 상태를 설정합니다.
st.set_page_config(
    page_title="CELL VISION | Tactical Command",  # 브라우저 탭에 표시되는 페이지 제목
    layout="wide",  # 화면을 넓게 사용하는 레이아웃
    initial_sidebar_state="expanded",  # 처음 접속했을 때 사이드바를 펼친 상태로 설정
)

# 현재 실행 중인 app.py 파일이 위치한 폴더의 절대 경로를 저장합니다.
# __file__은 현재 실행 중인 Python 파일을 의미합니다.
# resolve()는 절대 경로로 변환하고 parent는 해당 파일이 들어 있는 폴더를 가리킵니다.
ROOT_DIR = Path(__file__).resolve().parent

# 프로젝트 폴더 안에 있는 images 폴더의 경로를 저장합니다.
# 이후 이미지 파일을 불러올 때 이 경로를 기준으로 사용합니다.
IMAGE_DIR = ROOT_DIR / "images"

# =========================================================
# 2. 첫 접속 작전 브리핑 연결
# =========================================================

# session_state에 briefing_completed라는 값이 아직 없으면
# 브리핑을 완료하지 않은 상태(False)로 초기화합니다.
if "briefing_completed" not in st.session_state:
    st.session_state.briefing_completed = False

# 브리핑 완료 여부가 False라면 작전 브리핑 페이지로 이동합니다.
# 따라서 처음 접속한 사용자는 메인 화면보다 브리핑 페이지를 먼저 보게 됩니다.
if not st.session_state.briefing_completed:
    st.switch_page("pages/0_작전브리핑.py")

# =========================================================
# 3. 소기관 정보
# =========================================================

# 각 세포 소기관의 정보를 딕셔너리 형태로 저장하고,
# 여러 딕셔너리를 ORGANELLES라는 리스트에 모아 관리합니다.
#
# 각 소기관 정보에는 다음 항목이 들어 있습니다.
# name: 소기관 이름
# code: 소기관별 고유 자료 번호
# image: 소기관 이미지 파일 이름
# page: 소기관 상세 설명 페이지의 경로
# description: 소기관의 주요 기능을 요약한 설명

ORGANELLES = [
    {
        "name": "핵",
        "code": "BIO-01",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "description": "유전 정보를 보관하고 세포의 활동을 조절합니다.",
    },
    {
        "name": "리보솜",
        "code": "BIO-02",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "description": "유전 정보에 따라 단백질을 합성합니다.",
    },
    {
        "name": "미토콘드리아",
        "code": "BIO-03",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "description": "세포 호흡을 통해 ATP를 생성합니다.",
    },
    {
        "name": "소포체",
        "code": "BIO-04",
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "description": "단백질과 지질의 합성 및 이동에 관여합니다.",
    },
    {
        "name": "골지체",
        "code": "BIO-05",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "description": "물질을 가공하고 분류하여 목적지로 보냅니다.",
    },
    {
        "name": "리소좀",
        "code": "BIO-06",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "description": "세포 내 물질과 노폐물을 분해합니다.",
    },
    {
        "name": "세포막",
        "code": "BIO-07",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "description": "세포 안팎의 물질 이동을 조절합니다.",
    },
    {
        "name": "세포질",
        "code": "BIO-08",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "description": "다양한 세포 소기관이 존재하고 여러 화학 반응이 일어나는 공간입니다.",
    },
    {
        "name": "세포골격",
        "code": "BIO-09",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "description": "세포의 형태를 유지하고 세포 내 물질 이동을 돕습니다.",
    },
]

# =========================================================
# 4. 공통 디자인
# =========================================================

# CSS를 사용하여 메인 화면 전체의 디자인을 설정합니다.
# 배경, 글꼴, 색상, 패널, 버튼, 사이드바 등의 모양을 지정합니다.
st.markdown(
    """
    <style>
    /* 웹페이지에서 사용할 외부 글꼴을 가져옵니다. */
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    /* CSS 전체에서 반복해서 사용할 색상을 변수로 지정합니다. */
    :root {
        --bg: #050b12;       /* 전체 배경색 */
        --panel: #091521;    /* 패널 배경색 */
        --line: #244454;     /* 테두리 색상 */
        --cyan: #57d9e8;     /* 강조 색상 */
        --text: #dceaf0;     /* 기본 글자 색상 */
        --muted: #7993a3;    /* 보조 글자 색상 */
        --green: #8bd9b0;    /* 정상 작동 상태 표시 색상 */
    }

    /* HTML 문서와 Streamlit 내부 요소에 기본 글꼴을 적용합니다. */
    html, body, [class*="css"] {
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    /* 앱 전체의 배경과 글자 색상을 설정합니다. */
    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, #102433 0%, transparent 46%),
            #050b12;
        color: var(--text);
    }

    /* Streamlit 상단 헤더의 배경과 아래쪽 테두리를 설정합니다. */
    [data-testid="stHeader"] {
        background: rgba(5, 11, 18, 0.96);
        border-bottom: 1px solid #172d3b;
    }

    /* 왼쪽 사이드바의 배경과 오른쪽 테두리를 설정합니다. */
    [data-testid="stSidebar"] {
        background: #07111b;
        border-right: 1px solid #244454;
    }

    /* 사이드바 내부의 첫 번째 영역에도 배경색을 적용합니다. */
    [data-testid="stSidebar"] > div:first-child {
        background: #07111b;
    }

    /* 사이드바 내부의 모든 글자 색상을 지정합니다. */
    [data-testid="stSidebar"] * {
        color: #c9dce5;
    }

    /* Streamlit이 자동으로 생성하는 기본 페이지 이동 메뉴를 숨깁니다. */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* 메인 콘텐츠 영역의 최대 너비와 위아래 여백을 설정합니다. */
    .block-container {
        max-width: 1800px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    /* 제목, 문단, 목록 등의 기본 글자 색상을 설정합니다. */
    h1, h2, h3, p, li, label {
        color: var(--text);
    }

    /* 페이지 상단의 시스템 상태 표시 영역입니다. */
    .top-strip {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        padding: 9px 14px;
        margin-bottom: 18px;
        border-top: 2px solid #7d9aa9;
        border-bottom: 1px solid var(--line);
        background: linear-gradient(90deg, #132431, #07111b 75%);
        font-size: 10px;
        letter-spacing: 1.6px;
        color: #9cb7c4;
    }

    /* 상단 상태 표시 영역에서 strong 태그로 강조한 글자의 색상입니다. */
    .top-strip strong {
        color: var(--cyan);
        font-weight: 600;
    }

    /* 작은 분류 제목인 eyebrow의 디자인입니다. */
    .eyebrow {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }

    /* 메인 제목인 COMMAND CENTER의 디자인입니다. */
    .main-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: clamp(26px, 3vw, 42px);
        font-weight: 700;
        letter-spacing: 2px;
        line-height: 1.15;
        color: #edf8fc;
        margin: 0;
    }

    /* 메인 제목 아래의 부제목 디자인입니다. */
    .subtitle {
        font-size: 12px;
        color: #89a6b6;
        letter-spacing: 1px;
        margin-top: 9px;
        margin-bottom: 20px;
    }

    /* 각 콘텐츠 구역을 구분하는 제목 표시 영역입니다. */
    .section-bar {
        background: #0d1d2a;
        border-left: 3px solid var(--cyan);
        border-bottom: 1px solid #294958;
        padding: 10px 12px;
        margin: 12px 0;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #d8eef5;
    }

    /* 상황 정보 등을 담는 패널의 기본 디자인입니다. */
    .panel {
        background: linear-gradient(145deg, #0c1b28, #07111a);
        border: 1px solid #284655;
        border-top: 2px solid #5d8b9e;
        padding: 15px;
        margin-bottom: 12px;
        min-height: 112px;
    }

    /* 패널 안의 작은 항목 제목 디자인입니다. */
    .panel-label {
        font-size: 9px;
        color: #7fa1b2;
        letter-spacing: 1.6px;
        margin-bottom: 9px;
    }

    /* 패널 안의 주요 정보 디자인입니다. */
    .panel-value {
        font-size: 17px;
        font-weight: 700;
        color: #e6f4fa;
        letter-spacing: 0.5px;
        overflow-wrap: anywhere;
    }

    /* 패널 안의 보조 설명 디자인입니다. */
    .panel-note {
        font-size: 10px;
        color: #87a3b2;
        margin-top: 8px;
        line-height: 1.6;
    }

    /* 시스템이 정상 작동 중임을 나타내는 표시입니다. */
    .status-dot {
        color: var(--green);
        font-weight: 700;
    }

    /* 소기관 정보 카드의 전체 디자인입니다. */
    .intel-card {
        background: linear-gradient(140deg, #0c1b28, #07111a);
        border: 1px solid #284655;
        border-top: 2px solid #426c80;
        padding: 12px;
        margin-bottom: 10px;
        min-height: 205px;
    }

    /* 소기관의 자료 번호 디자인입니다. */
    .intel-code {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }

    /* 소기관 이름 디자인입니다. */
    .intel-name {
        color: #e8f5fa;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    /* 소기관의 기능을 설명하는 문장 디자인입니다. */
    .intel-description {
        color: #91aab8;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 12px;
        line-height: 1.7;
        min-height: 42px;
    }

    /* 소기관 카드 아래쪽의 자료 상태 표시 디자인입니다. */
    .intel-status {
        border-top: 1px solid #203a49;
        margin-top: 10px;
        padding-top: 8px;
        color: #86c9d5;
        font-size: 9px;
        letter-spacing: 1px;
    }

    /* 사이드바 상단의 프로젝트 로고 영역입니다. */
    .side-brand {
        border-top: 2px solid #6d95a7;
        border-bottom: 1px solid #284655;
        padding: 13px 6px;
        margin-bottom: 18px;
        background: linear-gradient(90deg, #122533, #07111b);
    }

    /* 사이드바의 CELL VISION 제목 디자인입니다. */
    .side-brand-title {
        font-size: 21px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #e5f4f9;
    }

    /* 사이드바의 소속 부제목 디자인입니다. */
    .side-brand-sub {
        font-size: 9px;
        color: var(--cyan);
        letter-spacing: 1.4px;
        margin-top: 5px;
    }

    /* 사이드바 메뉴 구역 제목의 디자인입니다. */
    .side-section {
        color: #70c7d9;
        font-size: 10px;
        letter-spacing: 1.5px;
        padding: 9px 0 5px 0;
        border-bottom: 1px solid #1e3949;
        margin: 12px 0 8px 0;
    }

    /* 사이드바 하단의 시스템 정보 글자 디자인입니다. */
    .side-info {
        color: #7894a5;
        font-size: 10px;
        line-height: 1.9;
    }

    /* 작전 지시 내용을 표시하는 상자의 디자인입니다. */
    .mission-box {
        background: #081722;
        border: 1px solid #294958;
        border-left: 3px solid #3988bd;
        padding: 14px;
        margin: 8px 0 15px 0;
    }

    /* 작전 지시 상자의 제목 디자인입니다. */
    .mission-box-title {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 1.7px;
        margin-bottom: 8px;
    }

    /* 작전 지시 상자의 본문 디자인입니다. */
    .mission-box-text {
        color: #c5d9e2;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 12px;
        line-height: 1.8;
    }

    /* 정보를 두 항목으로 나누어 표시하는 행의 디자인입니다. */
    .data-row {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        padding: 8px 0;
        border-bottom: 1px solid #1a3442;
        font-size: 10px;
    }

    /* data-row의 첫 번째 항목은 왼쪽 정보로 표시합니다. */
    .data-row span:first-child {
        color: #7e9baa;
    }

    /* data-row의 마지막 항목은 오른쪽 정보로 표시합니다. */
    .data-row span:last-child {
        color: #d6e8ef;
        text-align: right;
    }

    /* 페이지 맨 아래의 정보 표시 영역입니다. */
    .footer-line {
        border-top: 1px solid #284655;
        margin-top: 25px;
        padding-top: 10px;
        color: #658292;
        font-size: 9px;
        letter-spacing: 1.2px;
        display: flex;
        justify-content: space-between;
        gap: 10px;
        flex-wrap: wrap;
    }

    /* Streamlit 버튼과 페이지 링크의 기본 디자인을 설정합니다. */
    div[data-testid="stButton"] > button,
    div[data-testid="stPageLink"] a {
        background: #0b1c29 !important;
        color: #cceaf1 !important;
        border: 1px solid #315568 !important;
        border-radius: 0 !important;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
        font-size: 11px !important;
        letter-spacing: 0.4px;
        transition: 0.15s ease-in-out;
    }

    /* 버튼이나 페이지 링크에 마우스를 올렸을 때 적용되는 디자인입니다. */
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stPageLink"] a:hover {
        background: #123044 !important;
        border-color: var(--cyan) !important;
        color: #ffffff !important;
    }

    /* 화면에 표시되는 이미지에 테두리를 추가합니다. */
    [data-testid="stImage"] img {
        border: 1px solid #1d3949;
    }

    /* 경고 메시지 상자의 배경과 모서리 모양을 설정합니다. */
    [data-testid="stAlert"] {
        background: #0b1b28;
        border-radius: 0;
    }

    /* 구분선의 색상을 설정합니다. */
    hr {
        border-color: #203b4b;
    }

    /* 작전 돌입 전용 구역 */
    .operation-launch-panel {
        background:
            linear-gradient(110deg, rgba(21, 54, 72, 0.75), rgba(6, 16, 25, 0.97) 72%),
            #07111a;
        border: 1px solid #3a7188;
        border-top: 3px solid #57d9e8;
        padding: 25px 28px;
        margin-top: 18px;
        margin-bottom: 14px;
        position: relative;
    }

    /* 최종 작전 구역의 작은 분류 문구입니다. */
    .operation-launch-kicker {
        color: #57d9e8;
        font-size: 10px;
        letter-spacing: 2.2px;
        margin-bottom: 10px;
    }

    /* 최종 작전 구역의 큰 제목입니다. */
    .operation-launch-title {
        color: #edf8fc;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
        font-size: clamp(20px, 2.5vw, 30px);
        font-weight: 700;
        letter-spacing: 1.5px;
        line-height: 1.4;
        margin-bottom: 12px;
    }

    /* 최종 작전 구역의 설명 문구입니다. */
    .operation-launch-description {
        color: #a9c1ce;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 13px;
        line-height: 1.9;
        max-width: 850px;
    }

    /* 최종 작전 구역의 경고 및 상태 표시 문구입니다. */
    .operation-launch-warning {
        color: #79c9d8;
        font-size: 10px;
        letter-spacing: 1.3px;
        margin-top: 15px;
        padding-top: 12px;
        border-top: 1px solid #294958;
    }

    /* Streamlit에서 key="launch_operation"으로 지정한 버튼만 확대합니다. */
    .st-key-launch_operation button {
        min-height: 74px !important;
        padding: 18px 26px !important;
        background: linear-gradient(100deg, #12435a, #0b2637) !important;
        border: 2px solid #57d9e8 !important;
        border-radius: 0 !important;
        color: #f0fcff !important;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        box-shadow: 0 0 18px rgba(87, 217, 232, 0.08);
        transition: all 0.18s ease-in-out;
    }

    /* 최종 작전 버튼에 마우스를 올렸을 때의 디자인입니다. */
    .st-key-launch_operation button:hover {
        background: linear-gradient(100deg, #1a6079, #104057) !important;
        border-color: #a0f3ff !important;
        color: #ffffff !important;
        box-shadow: 0 0 22px rgba(87, 217, 232, 0.22);
        transform: translateY(-1px);
    }

    /* 버튼을 누르는 순간에는 위로 이동한 효과를 원래 위치로 되돌립니다. */
    .st-key-launch_operation button:active {
        transform: translateY(0);
    }

    /* 최종 작전 버튼 아래에 표시되는 안내 문구입니다. */
    .operation-launch-hint {
        color: #79c9d8;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 12px;
        line-height: 1.7;
        text-align: center;
        margin-top: 9px;
        letter-spacing: 0.2px;
    }

    /* 사이드바에 표시되는 작전 돌입 구역의 디자인입니다. */
    .sidebar-operation-panel {
        background: linear-gradient(145deg, #102b3b, #091722);
        border: 1px solid #3a7188;
        border-top: 2px solid #57d9e8;
        padding: 12px 10px;
        margin: 18px 0 14px 0;
    }

    /* 사이드바 작전 구역의 자료 번호 디자인입니다. */
    .sidebar-operation-code {
        color: #57d9e8;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 9px;
        letter-spacing: 1.3px;
        margin-bottom: 7px;
    }

    /* 사이드바 작전 구역의 제목 디자인입니다. */
    .sidebar-operation-title {
        color: #edf8fc;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    /* 사이드바 작전 구역의 설명 디자인입니다. */
    .sidebar-operation-description {
        color: #a9c1ce;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 11px;
        line-height: 1.7;
    }

    /* 사이드바에 있는 작전 개시 버튼의 크기와 디자인을 설정합니다. */
    .st-key-sidebar_launch_operation button {
        min-height: 52px !important;
        padding: 12px 8px !important;
        background: linear-gradient(100deg, #12435a, #0b2637) !important;
        border: 1px solid #57d9e8 !important;
        border-radius: 0 !important;
        color: #f0fcff !important;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 0 14px rgba(87, 217, 232, 0.08);
    }

    /* 사이드바 작전 개시 버튼에 마우스를 올렸을 때의 디자인입니다. */
    .st-key-sidebar_launch_operation button:hover {
        background: linear-gradient(100deg, #1a6079, #104057) !important;
        border-color: #a0f3ff !important;
        color: #ffffff !important;
        box-shadow: 0 0 18px rgba(87, 217, 232, 0.2);
    }

    /* 화면 너비가 800px 이하일 때 적용되는 반응형 디자인입니다. */
    @media (max-width: 800px) {
        /* 좁은 화면에서는 상단 상태 표시 요소가 다음 줄로 이동할 수 있게 합니다. */
        .top-strip {
            flex-wrap: wrap;
        }

        /* 모바일 화면에서 메인 제목의 글자 크기를 조절합니다. */
        .main-title {
            font-size: 25px;
        }

        /* 모바일 화면에서는 패널의 최소 높이를 해제합니다. */
        .panel {
            min-height: auto;
        }

        /* 작전 구역의 내부 여백을 줄입니다. */
        .operation-launch-panel {
            padding: 20px 16px;
        }

        /* 작전 제목의 글자 크기를 조절합니다. */
        .operation-launch-title {
            font-size: 21px;
        }

        /* 모바일 화면에서 작전 버튼의 글자 크기와 간격을 줄입니다. */
        .st-key-launch_operation button {
            font-size: 13px !important;
            letter-spacing: 0.8px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 5. 사이드바: 직접 만든 작전 메뉴
# =========================================================

# with st.sidebar 안에 작성한 요소들은 왼쪽 사이드바에 표시됩니다.
with st.sidebar:

    # 사이드바 상단에 프로젝트 이름과 소속을 표시합니다.
    st.markdown(
        """
        <div class="side-brand">
            <div class="side-brand-title">CELL VISION</div>
            <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 사이드바의 첫 번째 메뉴 구역 제목을 표시합니다.
    st.markdown(
        '<div class="side-section">01 / COMMAND MENU</div>',
        unsafe_allow_html=True,
    )

    # 메인 화면으로 이동하는 페이지 링크를 생성합니다.
    st.page_link(
        "app.py",
        label="COMMAND CENTER / 메인 화면",
    )

    # 작전 브리핑 페이지의 실제 파일 경로를 만듭니다.
    # ROOT_DIR을 기준으로 pages 폴더와 브리핑 파일의 경로를 연결합니다.
    briefing_page = ROOT_DIR / "pages" / "0_작전브리핑.py"

    # 브리핑 페이지 파일이 실제로 존재할 때만 사이드바에 링크를 표시합니다.
    if briefing_page.exists():
        st.page_link(
            "pages/0_작전브리핑.py",
            label="MISSION BRIEFING / 작전 브리핑",
        )

    # 사이드바의 두 번째 메뉴 구역 제목을 표시합니다.
    st.markdown(
        '<div class="side-section">02 / INTELLIGENCE FILES</div>',
        unsafe_allow_html=True,
    )

    # ORGANELLES 리스트에 저장된 각 소기관 정보를 하나씩 확인합니다.
    for organelle in ORGANELLES:

        # 각 소기관의 상세 페이지 파일이 실제로 존재하는지 확인합니다.
        # ROOT_DIR과 organelle["page"]를 연결해 파일 경로를 만듭니다.
        if (ROOT_DIR / organelle["page"]).exists():

            # 파일이 존재하면 해당 소기관으로 이동하는 링크를 생성합니다.
            st.page_link(
                organelle["page"],
                label=f'{organelle["code"]} / {organelle["name"]}',
            )

    # 최종 작전 페이지의 파일 경로를 지정합니다.
    game_page = ROOT_DIR / "pages" / "10_작전.py"

    # 최종 작전 페이지 파일이 존재하는 경우에만 작전 메뉴를 표시합니다.
    if game_page.exists():

        # 사이드바에 최종 작전의 설명 영역을 표시합니다.
        st.markdown(
            """
            <div class="sidebar-operation-panel">
                <div class="sidebar-operation-code">BIO-10 // FINAL OPERATION</div>
                <div class="sidebar-operation-title">작전 돌입</div>
                <div class="sidebar-operation-description">
                    소기관 정보를 충분히 수집하고 세포의 작동 원리를 이해했다면,
                    이제 최종 임무를 수행하십시오.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 버튼을 누르면 최종 작전 페이지로 이동합니다.
        st.button(
            "INITIATE OPERATION  /  작전 개시",
            key="sidebar_launch_operation",  # 버튼을 구별하기 위한 고유한 키
            use_container_width=True,  # 사이드바 너비에 맞춰 버튼을 표시합니다.
            on_click=lambda: st.switch_page("pages/10_작전.py"),  # 클릭하면 실행할 동작
        )

    # 사이드바 아래쪽에 시스템 상태와 보안 정보를 표시합니다.
    st.markdown(
        """
        <div class="side-section">03 / SYSTEM MONITOR</div>
        <div class="side-info">
            SYSTEM STATUS&nbsp;&nbsp; <span style="color:#8bd9b0;">ONLINE</span><br>
            DATABASE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOCAL FILES<br>
            SECURITY LEVEL&nbsp; BIO-RESTRICTED<br>
            ACCESS MODE&nbsp;&nbsp;&nbsp;&nbsp; EDUCATIONAL
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 사이드바에 구분선을 표시하고 프로젝트의 내부 사용 문구를 추가합니다.
    st.markdown("---")
    st.caption("CELL VISION / INTERNAL USE")

# =========================================================
# 6. 상단 전술 시스템 바
# =========================================================

# 현재 날짜를 연도-월-일 형식의 문자열로 가져옵니다.
# datetime.now()는 현재 날짜와 시간을 반환하고,
# strftime()은 원하는 형식으로 날짜를 바꿉니다.
current_time = datetime.now().strftime("%Y-%m-%d")

# f-string을 사용해 current_time 변수의 값을 HTML 안에 삽입합니다.
# 화면 상단에 시스템 이름, 보안 등급, 작동 상태, 현재 날짜를 표시합니다.
st.markdown(
    f"""
    <div class="top-strip">
        <span>CV // BIOLOGICAL INTELLIGENCE SYSTEM</span>
        <span>SECURITY LEVEL: <strong>RESTRICTED</strong></span>
        <span>SYSTEM STATUS: <strong>OPERATIONAL</strong></span>
        <span>{current_time}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# 메인 화면의 작은 분류 문구, 제목, 부제목을 표시합니다.
st.markdown(
    """
    <div class="eyebrow">TACTICAL BIOLOGY INTERFACE // TERMINAL 01</div>
    <h1 class="main-title">COMMAND CENTER</h1>
    <div class="subtitle">
        CELLULAR STRUCTURE ANALYSIS · BIOLOGICAL INTELLIGENCE · MISSION CONTROL
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 7. 상황 정보 패널
# =========================================================

# 화면을 세 개의 열로 나눕니다.
# 각 열의 너비는 기본적으로 동일합니다.
status_col1, status_col2, status_col3 = st.columns(3)

# 첫 번째 열에 작전 식별 정보를 표시합니다.
with status_col1:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">OPERATION IDENTIFIER</div>
            <div class="panel-value">BIO-OPS / 001</div>
            <div class="panel-note">MISSION: CELLULAR ANALYSIS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 두 번째 열에 현재 작전 상태를 표시합니다.
with status_col2:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">CURRENT OPERATION STATUS</div>
            <div class="panel-value"><span class="status-dot">●</span> STANDING BY</div>
            <div class="panel-note">AWAITING ANALYSIS INPUT</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 세 번째 열에 분석 대상인 동물세포 정보를 표시합니다.
with status_col3:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">TARGET PROFILE</div>
            <div class="panel-value">ANIMAL CELL</div>
            <div class="panel-note">BIOLOGICAL STRUCTURE / CLASSIFIED</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 8. 중앙 분석 화면
# =========================================================

# 중앙 분석 화면의 구역 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">LIVE ANALYSIS // TARGET RECONNAISSANCE</div>',
    unsafe_allow_html=True,
)

# 화면을 왼쪽, 중앙, 오른쪽 세 개의 열로 나눕니다.
# [0.85, 1.8, 1.0]은 각 열의 상대적인 너비 비율입니다.
# 중앙 열을 가장 넓게 설정해 세포 이미지를 크게 표시합니다.
left_col, center_col, right_col = st.columns(
    [0.85, 1.8, 1.0],
    gap="medium",
)

# 왼쪽 열에는 임무 지시와 주요 목표를 표시합니다.
with left_col:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">MISSION DIRECTIVE</div>
            <div class="panel-value">CELL / 001</div>
            <div class="panel-note">
                세포의 주요 구조를 식별하고 각 소기관의 기능 및 상호작용을 분석하십시오.
            </div>
        </div>

        <div class="section-bar">PRIMARY OBJECTIVES</div>
        <div class="data-row"><span>OBJECTIVE 01</span><span>구조 식별</span></div>
        <div class="data-row"><span>OBJECTIVE 02</span><span>기능 분석</span></div>
        <div class="data-row"><span>OBJECTIVE 03</span><span>물질 이동</span></div>
        <div class="data-row"><span>OBJECTIVE 04</span><span>시스템 이해</span></div>
        """,
        unsafe_allow_html=True,
    )

# 중앙 열에는 세포 전체 이미지와 분석 지시를 표시합니다.
with center_col:

    # 중앙 이미지 영역의 제목을 표시합니다.
    st.markdown(
        '<div class="section-bar">TARGET IMAGE // CELLULAR OVERVIEW</div>',
        unsafe_allow_html=True,
    )

    # images 폴더 안에 있는 cell.png 파일의 경로를 만듭니다.
    cell_image = IMAGE_DIR / "cell.png"

    # 이미지 파일이 실제로 존재하는지 확인합니다.
    if cell_image.exists():

        # 이미지가 존재하면 화면 너비에 맞춰 표시하고 설명을 추가합니다.
        st.image(
            str(cell_image),
            use_container_width=True,
            caption="TARGET 001 / ANIMAL CELL STRUCTURE",
        )

    else:

        # 이미지가 없으면 사용자에게 파일 확인 안내를 표시합니다.
        st.warning(
            "세포 전체 이미지가 없습니다. images 폴더에 cell.png 파일이 있는지 확인해 주세요."
        )

    # 세포의 구조와 기능을 분석하라는 지휘 내용을 표시합니다.
    st.markdown(
        """
        <div class="mission-box">
            <div class="mission-box-title">COMMAND DIRECTIVE // 001</div>
            <div class="mission-box-text">
                세포는 여러 소기관이 유기적으로 협력하는 생명 시스템입니다.
                각 소기관의 구조와 기능을 확인하고, 물질 합성·수송·에너지 전환 과정이
                어떻게 연결되는지 분석하십시오.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 오른쪽 열에는 분석 모드와 자료 분류 등 시스템 정보를 표시합니다.
with right_col:
    st.markdown(
        """
        <div class="section-bar">SYSTEM INTELLIGENCE</div>
        <div class="panel">
            <div class="panel-label">ANALYSIS MODE</div>
            <div class="panel-value">BIO / SCAN</div>
            <div class="panel-note">STRUCTURAL RECONNAISSANCE</div>
        </div>
        <div class="panel">
            <div class="panel-label">DATA CLASSIFICATION</div>
            <div class="panel-value">BIO-RESTRICTED</div>
            <div class="panel-note">EDUCATIONAL INTELLIGENCE FILES</div>
        </div>
        <div class="panel">
            <div class="panel-label">ANALYSIS PROTOCOL</div>
            <div class="panel-value">CELL SYSTEM</div>
            <div class="panel-note">IDENTIFY / ANALYZE / UNDERSTAND</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 9. 소기관 정보 파일
# =========================================================

# 소기관별 상세 정보를 확인할 수 있는 자료 구역의 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">다음은 우리가 확보한 기밀 자료이다. 전체를 다 숙지한 후 작전에 돌입하기를 바란다.</div>',
    unsafe_allow_html=True,
)

# 소기관 정보 파일을 선택하라는 안내 문구를 표시합니다.
st.markdown(
    """
    <div class="subtitle">
        SELECT AN INTELLIGENCE FILE TO ACCESS DETAILED BIOLOGICAL INFORMATION.
    </div>
    """,
    unsafe_allow_html=True,
)

# ORGANELLES 리스트를 세 개씩 나누어 화면에 표시합니다.
# range(0, len(ORGANELLES), 3)은 0부터 소기관 개수까지 3씩 증가합니다.
# 따라서 한 번의 반복마다 최대 세 개의 소기관을 처리합니다.
for start in range(0, len(ORGANELLES), 3):

    # 현재 위치(start)부터 세 개까지의 소기관 정보를 잘라냅니다.
    # 마지막 묶음에 세 개보다 적은 항목이 남아도 처리할 수 있습니다.
    row_items = ORGANELLES[start:start + 3]

    # 소기관 카드 세 개를 나란히 표시할 수 있도록 열을 만듭니다.
    columns = st.columns(3, gap="medium")

    # 각 열과 소기관 정보를 하나씩 짝지어 반복합니다.
    # zip()은 두 리스트의 항목을 순서대로 묶어 줍니다.
    for column, organelle in zip(columns, row_items):

        # 현재 소기관이 배치될 열을 지정합니다.
        with column:

            # 소기관의 자료 번호, 이름, 설명을 카드 형태로 표시합니다.
            # f-string을 사용해 organelle 딕셔너리의 값을 HTML에 삽입합니다.
            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="intel-code">
                        {organelle["code"]} // INTELLIGENCE FILE
                    </div>
                    <div class="intel-name">{organelle["name"]}</div>
                    <div class="intel-description">
                        {organelle["description"]}
                    </div>
                    <div class="intel-status">● DATA FILE / BIOLOGICAL</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 현재 소기관의 이미지 파일 경로를 만듭니다.
            # 이미지 이름은 ORGANELLES 리스트에 저장된 값을 사용합니다.
            image_path = IMAGE_DIR / organelle["image"]

            # 해당 이미지 파일이 존재하는지 확인합니다.
            if image_path.exists():

                # 이미지가 존재하면 화면 너비에 맞춰 표시합니다.
                st.image(
                    str(image_path),
                    use_container_width=True,
                )

            else:

                # 이미지가 없으면 어떤 파일을 찾지 못했는지 안내합니다.
                st.warning(
                    f'이미지 파일을 찾을 수 없습니다: images/{organelle["image"]}'
                )

            # 현재 소기관의 상세 페이지 경로를 만듭니다.
            page_path = ROOT_DIR / organelle["page"]

            # 상세 페이지 파일이 존재하는지 확인합니다.
            if page_path.exists():

                # 파일이 존재하면 해당 소기관의 상세 페이지로 이동하는 링크를 표시합니다.
                st.page_link(
                    organelle["page"],
                    label=f'ACCESS FILE / {organelle["name"]}',
                    use_container_width=True,
                )

            else:

                # 상세 페이지가 없으면 파일 경로를 확인하라는 안내를 표시합니다.
                st.caption(
                    f'상세 페이지 파일 확인 필요: {organelle["page"]}'
                )

# =========================================================
# 10. 작전 지침
# =========================================================

# 소기관을 분석할 때 따라야 할 작전 지침 구역의 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">FIELD INSTRUCTIONS // OPERATION PROTOCOL</div>',
    unsafe_allow_html=True,
)

# 작전 수행 순서와 설명을 튜플 형태로 저장합니다.
# 각 항목은 지침 제목과 지침 내용으로 구성됩니다.
protocols = [
    (
        "PROTOCOL 01 — OBSERVE",
        "세포 전체 이미지를 관찰하고 각 소기관의 위치와 형태를 확인하십시오.",
    ),
    (
        "PROTOCOL 02 — IDENTIFY",
        "소기관 정보 파일에 접근하여 구조, 기능, 세포 내 역할을 분석하십시오.",
    ),
    (
        "PROTOCOL 03 — CONNECT",
        "단백질 합성 및 이동, 세포 호흡 등 세포 내 과정의 연결 관계를 이해하십시오.",
    ),
]

# protocols 리스트의 각 지침을 하나씩 꺼내 화면에 표시합니다.
# title에는 지침 제목이, description에는 지침 설명이 저장됩니다.
for title, description in protocols:
    st.markdown(
        f"""
        <div class="mission-box">
            <div class="mission-box-title">{title}</div>
            <div class="mission-box-text">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 11. 작전 돌입 구역
# =========================================================

# 최종 작전 개시 구역의 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">FINAL DIRECTIVE // OPERATION LAUNCH</div>',
    unsafe_allow_html=True,
)

# 최종 작전의 배경 설명과 작전 개시 안내를 표시합니다.
st.markdown(
    """
    <div class="operation-launch-panel">
        <div class="operation-launch-kicker">
            CELL VISION // FINAL OPERATION AUTHORIZATION
        </div>
        <div class="operation-launch-title">
            FINAL OPERATION AUTHORIZATION
        </div>
        <div class="operation-launch-description">
            대원, 분석실에서 확보한 생물학적 정보를 다시 확인하십시오.
            각 소기관의 기능과 세포 내부의 작동 원리를 이해했다면
            최종 작전을 개시할 준비가 완료된 것입니다.<br>
            지금까지 습득한 지식을 활용해 주어진 임무를 수행하십시오.
        </div>
        <div class="operation-launch-warning">
            MISSION STATUS: STANDING BY
            &nbsp; / &nbsp;
            AUTHORIZATION REQUIRED
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 최종 작전 페이지의 파일 경로를 지정합니다.
game_page = ROOT_DIR / "pages" / "10_작전.py"

# 최종 작전 페이지 파일이 실제로 존재하는지 확인합니다.
if game_page.exists():

    # 작전 페이지로 이동하는 버튼을 생성합니다.
    st.button(
        "INITIATE OPERATION  /  작전 돌입",
        key="launch_operation",  # 버튼을 구분하기 위한 고유한 키
        type="primary",  # 주요 동작 버튼으로 설정
        use_container_width=True,  # 버튼이 화면의 사용 가능한 너비를 모두 차지하도록 설정
        on_click=lambda: st.switch_page("pages/10_작전.py"),  # 버튼을 누르면 작전 페이지로 이동
    )

    # 작전 개시 버튼 아래에 안내 문구를 표시합니다.
    st.markdown(
        '<div class="operation-launch-hint">'
        '정보를 충분히 수집했다면, 이제 작전에 돌입하십시오.'
        '</div>',
        unsafe_allow_html=True,
    )

else:

    # 작전 페이지 파일이 존재하지 않으면 오류 메시지를 표시합니다.
    st.error(
        "작전 페이지를 찾을 수 없습니다. "
        "pages/10_작전.py 파일이 존재하는지 확인해 주세요."
    )

# =========================================================
# 12. 하단 정보
# =========================================================

# 페이지 맨 아래에 프로젝트 이름, 사용 목적, 종료 문구를 표시합니다.
st.markdown(
    """
    <div class="footer-line">
        <span>CELL VISION // BIOLOGICAL OPERATIONS UNIT</span>
        <span>INTERNAL SYSTEM · EDUCATIONAL USE</span>
        <span>END OF TRANSMISSION</span>
    </div>
    """,
    unsafe_allow_html=True,
)
