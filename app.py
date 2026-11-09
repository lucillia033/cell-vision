# Streamlit 라이브러리를 st라는 짧은 이름으로 가져옵니다.
# Streamlit은 Python 코드로 웹 애플리케이션을 만들 때 사용하는 도구입니다.
import streamlit as st

# 파일과 폴더의 경로를 운영체제에 맞게 관리하는 Path 클래스를 가져옵니다.
from pathlib import Path

# 현재 날짜와 시간을 가져오는 datetime 클래스를 가져옵니다.
from datetime import datetime


# =========================================================
# 1. 기본 설정
# =========================================================

# 웹페이지의 기본 설정을 지정합니다.
st.set_page_config(
    page_title="CELL VISION | Tactical Command",  # 브라우저 탭에 표시할 제목입니다.
    layout="wide",  # 웹페이지를 넓은 화면 형태로 표시합니다.
    initial_sidebar_state="expanded",  # 처음 접속했을 때 왼쪽 사이드바를 펼쳐 놓습니다.
)

# __file__은 현재 실행 중인 Python 파일의 위치를 의미합니다.
# resolve()는 해당 파일의 경로를 절대 경로로 바꿉니다.
# parent는 파일이 들어 있는 상위 폴더를 의미합니다.
# 따라서 ROOT_DIR에는 app.py가 들어 있는 프로젝트 폴더의 경로가 저장됩니다.
ROOT_DIR = Path(__file__).resolve().parent

# ROOT_DIR 뒤에 images를 연결하여 이미지 폴더의 경로를 만듭니다.
# / 연산자는 Path 객체에서 폴더와 파일 경로를 연결하는 데 사용됩니다.
IMAGE_DIR = ROOT_DIR / "images"


# =========================================================
# 2. 첫 접속 작전 브리핑 연결
# =========================================================

# st.session_state는 페이지를 이동하거나 화면이 다시 실행되어도
# 사용자별 상태를 유지할 수 있도록 Streamlit에서 제공하는 저장 공간입니다.
# "briefing_completed"라는 항목이 아직 없다면 아래 조건문이 실행됩니다.
if "briefing_completed" not in st.session_state:

    # 브리핑을 아직 완료하지 않은 상태를 False로 저장합니다.
    # False는 '아니요', '아직 완료하지 않음'이라는 의미입니다.
    st.session_state.briefing_completed = False

# 브리핑 완료 여부가 False라면 조건문 안의 코드를 실행합니다.
if not st.session_state.briefing_completed:

    # 작전 브리핑 페이지로 이동합니다.
    # not은 뒤에 있는 값이 False일 때 조건을 참으로 만듭니다.
    # 따라서 처음 접속했거나 브리핑을 완료하지 않은 사용자는 브리핑으로 이동합니다.
    st.switch_page("pages/0_작전브리핑.py")


# =========================================================
# 3. 소기관 정보
# =========================================================

# ORGANELLES는 세포 소기관 9개의 정보를 저장하는 리스트입니다.
# 리스트는 여러 데이터를 순서대로 모아 두는 자료형입니다.
# 대괄호 [] 안에 여러 소기관 정보를 넣습니다.
ORGANELLES = [

    # 중괄호 {} 안에 핵에 대한 정보를 딕셔너리 형태로 저장합니다.
    # 딕셔너리는 '이름표: 값' 형태로 데이터를 관리합니다.
    {
        "name": "핵",  # 소기관의 이름입니다.
        "code": "BIO-01",  # 소기관을 구분하기 위한 자료 번호입니다.
        "image": "nucleus.png",  # images 폴더에서 사용할 이미지 파일 이름입니다.
        "page": "pages/1_핵.py",  # 핵의 상세 설명 페이지가 있는 경로입니다.
        "description": "유전 정보를 보관하고 세포의 활동을 조절하라.",  # 카드에 표시할 설명입니다.
    },

    # 리보솜에 대한 정보를 저장합니다.
    {
        "name": "리보솜",  # 소기관 이름입니다.
        "code": "BIO-02",  # 고유 자료 번호입니다.
        "image": "ribosome.png",  # 이미지 파일 이름입니다.
        "page": "pages/2_리보솜.py",  # 상세 페이지 경로입니다.
        "description": "유전 정보에 따라 단백질을 합성하라.",  # 소기관의 주요 기능입니다.
    },

    # 미토콘드리아에 대한 정보를 저장합니다.
    {
        "name": "미토콘드리아",  # 소기관 이름입니다.
        "code": "BIO-03",  # 고유 자료 번호입니다.
        "image": "mitochondria.png",  # 이미지 파일 이름입니다.
        "page": "pages/3_미토콘드리아.py",  # 상세 페이지 경로입니다.
        "description": "세포 호흡을 통해 ATP를 생성하라.",  # 소기관의 주요 기능입니다.
    },

    # 소포체에 대한 정보를 저장합니다.
    {
        "name": "소포체",  # 소기관 이름입니다.
        "code": "BIO-04",  # 고유 자료 번호입니다.
        "image": "er.png",  # 이미지 파일 이름입니다.
        "page": "pages/4_소포체.py",  # 상세 페이지 경로입니다.
        "description": "단백질과 지질의 합성 및 이동을 담당하라.",  # 소기관의 주요 기능입니다.
    },

    # 골지체에 대한 정보를 저장합니다.
    {
        "name": "골지체",  # 소기관 이름입니다.
        "code": "BIO-05",  # 고유 자료 번호입니다.
        "image": "golgi.png",  # 이미지 파일 이름입니다.
        "page": "pages/5_골지체.py",  # 상세 페이지 경로입니다.
        "description": "물질을 가공하고 분류해 목적지로 보내라.",  # 소기관의 주요 기능입니다.
    },

    # 리소좀에 대한 정보를 저장합니다.
    {
        "name": "리소좀",  # 소기관 이름입니다.
        "code": "BIO-06",  # 고유 자료 번호입니다.
        "image": "lysosome.png",  # 이미지 파일 이름입니다.
        "page": "pages/6_리소좀.py",  # 상세 페이지 경로입니다.
        "description": "세포 내 물질과 노폐물을 분해하라.",  # 소기관의 주요 기능입니다.
    },

    # 세포막에 대한 정보를 저장합니다.
    {
        "name": "세포막",  # 소기관 이름입니다.
        "code": "BIO-07",  # 고유 자료 번호입니다.
        "image": "membrane.png",  # 이미지 파일 이름입니다.
        "page": "pages/7_세포막.py",  # 상세 페이지 경로입니다.
        "description": "세포 안팎의 물질 이동을 조절하라.",  # 세포막의 주요 기능입니다.
    },

    # 세포질에 대한 정보를 저장합니다.
    {
        "name": "세포질",  # 소기관 이름입니다.
        "code": "BIO-08",  # 고유 자료 번호입니다.
        "image": "cytosol.png",  # 이미지 파일 이름입니다.
        "page": "pages/8_세포질.py",  # 상세 페이지 경로입니다.
        "description": "다양한 세포 소기관과 화학 반응이 일어나는 공간을 확인하라.",  # 주요 특징입니다.
    },

    # 세포골격에 대한 정보를 저장합니다.
    {
        "name": "세포골격",  # 소기관 이름입니다.
        "code": "BIO-09",  # 고유 자료 번호입니다.
        "image": "cytoskeleton.png",  # 이미지 파일 이름입니다.
        "page": "pages/9_세포골격.py",  # 상세 페이지 경로입니다.
        "description": "세포의 형태를 유지하고 세포 내 물질 이동을 도와라.",  # 주요 기능입니다.
    },
]


# =========================================================
# 4. 공통 디자인
# =========================================================

# st.markdown()은 웹페이지에 Markdown 또는 HTML을 표시하는 함수입니다.
# 아래에서는 HTML과 CSS를 사용해 화면의 디자인을 직접 지정합니다.
st.markdown(
    """
    <style>
    /* @import는 외부 웹사이트에서 글꼴을 가져오는 CSS 명령어입니다. */
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    /* :root는 웹페이지 전체에서 사용할 CSS 변수를 정의하는 영역입니다. */
    :root {
        --bg: #050b12;       /* --bg라는 이름으로 전체 배경색을 저장합니다. */
        --panel: #091521;    /* --panel은 패널 배경색입니다. */
        --line: #244454;     /* --line은 테두리 색상입니다. */
        --cyan: #57d9e8;      /* --cyan은 강조할 때 사용하는 청록색입니다. */
        --text: #dceaf0;      /* --text는 기본 글자 색상입니다. */
        --muted: #7993a3;     /* --muted는 보조 글자 색상입니다. */
        --green: #8bd9b0;     /* --green은 정상 상태를 나타내는 색상입니다. */
    }

    /* 쉼표로 여러 선택자를 연결하면 여러 요소에 같은 스타일을 적용합니다. */
    html, body, [class*="css"] {
        /* font-family는 글꼴을 지정합니다. 앞의 글꼴을 사용할 수 없으면 다음 글꼴을 사용합니다. */
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    /* .stApp은 Streamlit 앱 전체를 감싸는 영역을 선택합니다. */
    .stApp {
        /* background는 배경을 설정합니다. radial-gradient는 중심에서 바깥으로 퍼지는 색상 효과입니다. */
        background:
            radial-gradient(ellipse at 50% 0%, #102433 0%, transparent 46%),
            #050b12;
        /* color는 이 영역에 적용되는 기본 글자 색상입니다. */
        color: var(--text);
    }

    /* Streamlit 상단 헤더를 선택합니다. */
    [data-testid="stHeader"] {
        /* rgba는 빨강, 초록, 파랑, 투명도를 사용해 색상을 지정합니다. */
        background: rgba(5, 11, 18, 0.96);
        /* border-bottom은 아래쪽 테두리만 설정합니다. */
        border-bottom: 1px solid #172d3b;
    }

    /* 왼쪽 사이드바의 배경과 오른쪽 테두리를 지정합니다. */
    [data-testid="stSidebar"] {
        background: #07111b;  /* 사이드바 배경색입니다. */
        border-right: 1px solid #244454;  /* 오른쪽에 1px 두께의 테두리를 표시합니다. */
    }

    /* >는 바로 아래에 있는 첫 번째 자식 요소를 선택합니다. */
    [data-testid="stSidebar"] > div:first-child {
        background: #07111b;  /* 사이드바 내부 첫 번째 영역에도 배경색을 적용합니다. */
    }

    /* 사이드바 안에 있는 모든 요소의 글자 색상을 지정합니다. */
    [data-testid="stSidebar"] * {
        color: #c9dce5;  /* *는 해당 영역 안의 모든 요소를 의미합니다. */
    }

    /* Streamlit의 기본 사이드바 페이지 메뉴를 선택합니다. */
    [data-testid="stSidebarNav"] {
        display: none !important;  /* display: none은 요소를 숨깁니다. !important는 이 설정의 우선순위를 높입니다. */
    }

    /* 메인 콘텐츠 영역의 크기와 여백을 설정합니다. */
    .block-container {
        max-width: 1800px;  /* 콘텐츠 영역이 최대 1800px을 넘지 않게 합니다. */
        padding-top: 1.2rem;  /* 위쪽 안쪽 여백입니다. rem은 기본 글자 크기를 기준으로 한 단위입니다. */
        padding-bottom: 2rem;  /* 아래쪽 안쪽 여백입니다. */
    }

    /* 제목, 문단, 목록, 입력 설명 등의 기본 글자 색상을 지정합니다. */
    h1, h2, h3, p, li, label {
        color: var(--text);  /* 앞에서 만든 --text 변수의 색상을 사용합니다. */
    }

    /* 페이지 상단의 시스템 상태 표시 영역입니다. */
    .top-strip {
        display: flex;  /* 내부 요소를 유연한 행 형태로 배치합니다. */
        justify-content: space-between;  /* 내부 요소 사이에 남는 공간을 고르게 배분합니다. */
        align-items: center;  /* 내부 요소를 세로 방향 가운데에 맞춥니다. */
        gap: 12px;  /* 내부 요소 사이의 간격을 12px로 설정합니다. */
        padding: 9px 14px;  /* 위아래 9px, 좌우 14px의 안쪽 여백입니다. */
        margin-bottom: 18px;  /* 영역 아래에 18px의 바깥 여백을 둡니다. */
        border-top: 2px solid #7d9aa9;  /* 위쪽에 2px 테두리를 표시합니다. */
        border-bottom: 1px solid var(--line);  /* 아래쪽 테두리 색상에 --line 변수를 사용합니다. */
        background: linear-gradient(90deg, #132431, #07111b 75%);  /* 왼쪽에서 오른쪽으로 배경색이 변합니다. */
        font-size: 10px;  /* 글자 크기를 10px로 설정합니다. */
        letter-spacing: 1.6px;  /* 글자 사이 간격을 넓힙니다. */
        color: #9cb7c4;  /* 기본 글자 색상입니다. */
    }

    /* 상단 표시 영역 안에서 strong 태그로 강조한 글자를 선택합니다. */
    .top-strip strong {
        color: var(--cyan);  /* 강조 글자에 청록색을 적용합니다. */
        font-weight: 600;  /* 글자를 조금 굵게 표시합니다. */
    }

    /* 작은 분류 제목의 디자인입니다. */
    .eyebrow {
        color: var(--cyan);  /* 글자 색상입니다. */
        font-size: 10px;  /* 작은 글자 크기입니다. */
        letter-spacing: 2px;  /* 글자 사이 간격입니다. */
        margin-bottom: 5px;  /* 아래쪽 바깥 여백입니다. */
    }

    /* COMMAND CENTER 메인 제목의 디자인입니다. */
    .main-title {
        font-family: 'IBM Plex Mono', monospace;  /* 제목에 사용할 글꼴입니다. */
        font-size: clamp(26px, 3vw, 42px);  /* 최소 26px, 화면 너비에 따라 커지되 최대 42px로 제한합니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        letter-spacing: 2px;  /* 글자 사이 간격을 넓힙니다. */
        line-height: 1.15;  /* 줄 사이의 간격을 글자 크기의 1.15배로 설정합니다. */
        color: #edf8fc;  /* 제목 글자 색상입니다. */
        margin: 0;  /* 제목의 기본 바깥 여백을 제거합니다. */
    }

    /* 메인 제목 아래의 부제목 디자인입니다. */
    .subtitle {
        font-size: 12px;  /* 글자 크기입니다. */
        color: #89a6b6;  /* 보조 글자 색상입니다. */
        letter-spacing: 1px;  /* 글자 사이 간격입니다. */
        margin-top: 9px;  /* 위쪽 바깥 여백입니다. */
        margin-bottom: 20px;  /* 아래쪽 바깥 여백입니다. */
    }

    /* 콘텐츠 구역을 구분하는 제목 표시 영역입니다. */
    .section-bar {
        background: #0d1d2a;  /* 제목 영역의 배경색입니다. */
        border-left: 3px solid var(--cyan);  /* 왼쪽에 청록색 강조선을 표시합니다. */
        border-bottom: 1px solid #294958;  /* 아래쪽 테두리를 표시합니다. */
        padding: 10px 12px;  /* 안쪽 여백입니다. */
        margin: 12px 0;  /* 위아래 바깥 여백을 12px로 설정합니다. */
        font-size: 11px;  /* 글자 크기입니다. */
        font-weight: 600;  /* 글자를 굵게 표시합니다. */
        letter-spacing: 1.5px;  /* 글자 사이 간격입니다. */
        color: #d8eef5;  /* 글자 색상입니다. */
    }

    /* 상황 정보를 표시하는 패널의 기본 디자인입니다. */
    .panel {
        background: linear-gradient(145deg, #0c1b28, #07111a);  /* 대각선 방향으로 배경색을 변화시킵니다. */
        border: 1px solid #284655;  /* 패널 전체 테두리입니다. */
        border-top: 2px solid #5d8b9e;  /* 위쪽 테두리를 조금 두껍게 만듭니다. */
        padding: 15px;  /* 패널 안쪽 여백입니다. */
        margin-bottom: 12px;  /* 패널 아래쪽 여백입니다. */
        min-height: 112px;  /* 패널의 최소 높이를 112px로 지정합니다. */
    }

    /* 패널 안의 작은 항목 제목 디자인입니다. */
    .panel-label {
        font-size: 9px;  /* 글자 크기입니다. */
        color: #7fa1b2;  /* 글자 색상입니다. */
        letter-spacing: 1.6px;  /* 글자 사이 간격입니다. */
        margin-bottom: 9px;  /* 아래쪽 여백입니다. */
    }

    /* 패널 안의 주요 정보 디자인입니다. */
    .panel-value {
        font-size: 17px;  /* 글자 크기입니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        color: #e6f4fa;  /* 글자 색상입니다. */
        letter-spacing: 0.5px;  /* 글자 사이 간격입니다. */
        overflow-wrap: anywhere;  /* 긴 문자열도 영역 밖으로 넘치지 않도록 줄바꿈합니다. */
    }

    /* 패널 안의 보조 설명 디자인입니다. */
    .panel-note {
        font-size: 10px;  /* 글자 크기입니다. */
        color: #87a3b2;  /* 보조 설명 색상입니다. */
        margin-top: 8px;  /* 위쪽 여백입니다. */
        line-height: 1.6;  /* 줄 간격을 설정합니다. */
    }

    /* SYSTEM INTELLIGENCE 구역의 안내 패널입니다. */
    .intelligence-notice {
        background: linear-gradient(145deg, #0c1b28, #07111a);  /* 패널 배경에 그라데이션을 적용합니다. */
        border: 1px solid #284655;  /* 패널 테두리입니다. */
        border-top: 2px solid #5d8b9e;  /* 위쪽 테두리를 강조합니다. */
        padding: 22px 16px;  /* 위아래 22px, 좌우 16px의 안쪽 여백입니다. */
        min-height: 240px;  /* 패널의 최소 높이입니다. */
        display: flex;  /* 내부 요소를 유연하게 배치합니다. */
        flex-direction: column;  /* 내부 요소를 세로 방향으로 배치합니다. */
        justify-content: center;  /* 내부 요소들을 세로 방향 가운데에 배치합니다. */
        gap: 14px;  /* 내부 요소 사이의 간격입니다. */
    }

    /* 기밀 정보 안내 문구의 디자인입니다. */
    .intelligence-notice-text {
        color: #c9dce5;  /* 글자 색상입니다. */
        font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;  /* 굵고 눈에 띄는 글꼴을 우선 사용합니다. */
        font-size: clamp(17px, 1.45vw, 22px);  /* 화면에 따라 글자 크기를 조절합니다. */
        font-weight: 400;  /* 글자 굵기를 보통으로 설정합니다. */
        line-height: 1.7;  /* 줄 간격입니다. */
        letter-spacing: 0.2px;  /* 글자 사이 간격입니다. */
    }

    /* 작전 수행 지시 문구를 더 크게 강조합니다. */
    .intelligence-notice-directive {
        color: var(--cyan);  /* 강조 색상입니다. */
        font-family: 'Black Han Sans', 'Noto Sans KR', sans-serif;  /* 사용할 글꼴입니다. */
        font-size: clamp(23px, 2vw, 32px);  /* 화면 크기에 따라 글자 크기를 조절합니다. */
        font-weight: 400;  /* 글자 굵기입니다. */
        line-height: 1.55;  /* 줄 간격입니다. */
        letter-spacing: 0.3px;  /* 글자 사이 간격입니다. */
    }

    /* 정상 작동 상태를 나타내는 표시의 색상과 굵기입니다. */
    .status-dot {
        color: var(--green);  /* 정상 상태 표시 색상입니다. */
        font-weight: 700;  /* 표시를 굵게 만듭니다. */
    }

    /* 소기관 정보 카드의 전체 디자인입니다. */
    .intel-card {
        background: linear-gradient(140deg, #0c1b28, #07111a);  /* 카드 배경입니다. */
        border: 1px solid #284655;  /* 카드 테두리입니다. */
        border-top: 2px solid #426c80;  /* 카드 위쪽 테두리입니다. */
        padding: 12px;  /* 카드 안쪽 여백입니다. */
        margin-bottom: 10px;  /* 카드 아래쪽 여백입니다. */
        min-height: 205px;  /* 카드의 최소 높이입니다. */
    }

    /* 소기관의 자료 번호 디자인입니다. */
    .intel-code {
        color: var(--cyan);  /* 자료 번호 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        letter-spacing: 1.5px;  /* 글자 사이 간격입니다. */
        margin-bottom: 6px;  /* 아래쪽 여백입니다. */
    }

    /* 소기관 이름 디자인입니다. */
    .intel-name {
        color: #e8f5fa;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글 표시를 고려한 글꼴입니다. */
        font-size: 17px;  /* 글자 크기입니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        margin-bottom: 8px;  /* 아래쪽 여백입니다. */
    }

    /* 소기관 기능 설명의 디자인입니다. */
    .intel-description {
        color: #91aab8;  /* 설명 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 12px;  /* 글자 크기입니다. */
        line-height: 1.7;  /* 줄 간격입니다. */
        min-height: 42px;  /* 설명 영역의 최소 높이를 지정합니다. */
    }

    /* 카드 아래쪽에 표시하는 자료 상태 문구입니다. */
    .intel-status {
        border-top: 1px solid #203a49;  /* 위쪽 구분선입니다. */
        margin-top: 10px;  /* 위쪽 여백입니다. */
        padding-top: 8px;  /* 구분선과 글자 사이의 안쪽 여백입니다. */
        color: #86c9d5;  /* 글자 색상입니다. */
        font-size: 9px;  /* 글자 크기입니다. */
        letter-spacing: 1px;  /* 글자 사이 간격입니다. */
    }

    /* 사이드바 상단의 프로젝트 로고 영역입니다. */
    .side-brand {
        border-top: 2px solid #6d95a7;  /* 위쪽 강조선입니다. */
        border-bottom: 1px solid #284655;  /* 아래쪽 구분선입니다. */
        padding: 13px 6px;  /* 안쪽 여백입니다. */
        margin-bottom: 18px;  /* 아래쪽 여백입니다. */
        background: linear-gradient(90deg, #122533, #07111b);  /* 가로 방향 배경 그라데이션입니다. */
    }

    /* 사이드바의 CELL VISION 제목 디자인입니다. */
    .side-brand-title {
        font-size: 21px;  /* 글자 크기입니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        letter-spacing: 2px;  /* 글자 사이 간격입니다. */
        color: #e5f4f9;  /* 글자 색상입니다. */
    }

    /* 사이드바의 소속 부제목 디자인입니다. */
    .side-brand-sub {
        font-size: 9px;  /* 글자 크기입니다. */
        color: var(--cyan);  /* 글자 색상입니다. */
        letter-spacing: 1.4px;  /* 글자 사이 간격입니다. */
        margin-top: 5px;  /* 위쪽 여백입니다. */
    }

    /* 사이드바 메뉴 구역 제목의 디자인입니다. */
    .side-section {
        color: #70c7d9;  /* 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        letter-spacing: 1.5px;  /* 글자 사이 간격입니다. */
        padding: 9px 0 5px 0;  /* 위쪽 9px, 오른쪽 0, 아래쪽 5px, 왼쪽 0의 안쪽 여백입니다. */
        border-bottom: 1px solid #1e3949;  /* 아래쪽 구분선입니다. */
        margin: 12px 0 8px 0;  /* 위쪽 12px, 아래쪽 8px의 바깥 여백입니다. */
    }

    /* 사이드바 아래쪽 시스템 정보 글자의 디자인입니다. */
    .side-info {
        color: #7894a5;  /* 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        line-height: 1.9;  /* 줄 간격입니다. */
    }

    /* 작전 지시 내용을 담는 상자의 디자인입니다. */
    .mission-box {
        background: #081722;  /* 배경색입니다. */
        border: 1px solid #294958;  /* 테두리입니다. */
        border-left: 3px solid #3988bd;  /* 왼쪽 강조선입니다. */
        padding: 14px;  /* 안쪽 여백입니다. */
        margin: 8px 0 15px 0;  /* 위쪽 8px, 아래쪽 15px의 바깥 여백입니다. */
    }

    /* 작전 지시 상자의 제목 디자인입니다. */
    .mission-box-title {
        color: var(--cyan);  /* 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        letter-spacing: 1.7px;  /* 글자 사이 간격입니다. */
        margin-bottom: 8px;  /* 아래쪽 여백입니다. */
    }

    /* 작전 지시 상자의 본문 디자인입니다. */
    .mission-box-text {
        color: #c5d9e2;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 12px;  /* 글자 크기입니다. */
        line-height: 1.8;  /* 줄 간격입니다. */
    }

    /* 정보를 두 항목으로 나누어 표시하는 행의 디자인입니다. */
    .data-row {
        display: flex;  /* 내부 항목을 한 행에 배치합니다. */
        justify-content: space-between;  /* 첫 항목과 마지막 항목을 양쪽 끝으로 배치합니다. */
        gap: 8px;  /* 두 항목 사이의 간격입니다. */
        padding: 8px 0;  /* 위아래 안쪽 여백입니다. */
        border-bottom: 1px solid #1a3442;  /* 행 아래에 구분선을 표시합니다. */
        font-size: 10px;  /* 글자 크기입니다. */
    }

    /* data-row 안에서 첫 번째 span 요소를 선택합니다. */
    .data-row span:first-child {
        color: #7e9baa;  /* 왼쪽 항목의 글자 색상입니다. */
    }

    /* data-row 안에서 마지막 span 요소를 선택합니다. */
    .data-row span:last-child {
        color: #d6e8ef;  /* 오른쪽 항목의 글자 색상입니다. */
        text-align: right;  /* 글자를 오른쪽에 맞춥니다. */
    }

    /* 페이지 맨 아래의 정보 표시 영역입니다. */
    .footer-line {
        border-top: 1px solid #284655;  /* 위쪽 구분선입니다. */
        margin-top: 25px;  /* 위쪽 바깥 여백입니다. */
        padding-top: 10px;  /* 위쪽 안쪽 여백입니다. */
        color: #658292;  /* 글자 색상입니다. */
        font-size: 9px;  /* 글자 크기입니다. */
        letter-spacing: 1.2px;  /* 글자 사이 간격입니다. */
        display: flex;  /* 내부 항목을 유연하게 배치합니다. */
        justify-content: space-between;  /* 항목 사이 공간을 고르게 배분합니다. */
        gap: 10px;  /* 항목 사이의 간격입니다. */
        flex-wrap: wrap;  /* 공간이 부족하면 다음 줄로 넘어가게 합니다. */
    }

    /* Streamlit 버튼과 페이지 링크의 기본 디자인입니다. */
    div[data-testid="stButton"] > button,
    div[data-testid="stPageLink"] a {
        background: #0b1c29 !important;  /* 버튼 배경색입니다. */
        color: #cceaf1 !important;  /* 버튼 글자 색상입니다. */
        border: 1px solid #315568 !important;  /* 버튼 테두리입니다. */
        border-radius: 0 !important;  /* 모서리를 둥글게 하지 않습니다. */
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;  /* 버튼 글꼴입니다. */
        font-size: 11px !important;  /* 버튼 글자 크기입니다. */
        letter-spacing: 0.4px;  /* 글자 사이 간격입니다. */
        transition: 0.15s ease-in-out;  /* 상태가 바뀔 때 0.15초 동안 부드럽게 변화합니다. */
    }

    /* 버튼이나 페이지 링크 위에 마우스를 올렸을 때 적용됩니다. */
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stPageLink"] a:hover {
        background: #123044 !important;  /* 마우스를 올렸을 때 배경색입니다. */
        border-color: var(--cyan) !important;  /* 테두리를 강조 색상으로 바꿉니다. */
        color: #ffffff !important;  /* 글자를 흰색으로 바꿉니다. */
    }

    /* Streamlit에서 표시하는 이미지에 테두리를 추가합니다. */
    [data-testid="stImage"] img {
        border: 1px solid #1d3949;  /* 이미지 테두리입니다. */
    }

    /* 경고 메시지 상자의 배경과 모서리 모양입니다. */
    [data-testid="stAlert"] {
        background: #0b1b28;  /* 경고 상자의 배경색입니다. */
        border-radius: 0;  /* 모서리를 둥글게 하지 않습니다. */
    }

    /* HTML의 hr 구분선 색상을 설정합니다. */
    hr {
        border-color: #203b4b;  /* 구분선 색상입니다. */
    }

    /* 작전 돌입 구역의 전체 디자인입니다. */
    .operation-launch-panel {
        background:
            linear-gradient(110deg, rgba(21, 54, 72, 0.75), rgba(6, 16, 25, 0.97) 72%),
            #07111a;  /* 반투명 그라데이션과 기본 배경색을 함께 사용합니다. */
        border: 1px solid #3a7188;  /* 전체 테두리입니다. */
        border-top: 3px solid #57d9e8;  /* 위쪽 청록색 강조선입니다. */
        padding: 25px 28px;  /* 안쪽 여백입니다. */
        margin-top: 18px;  /* 위쪽 바깥 여백입니다. */
        margin-bottom: 14px;  /* 아래쪽 바깥 여백입니다. */
        position: relative;  /* 내부 요소를 기준으로 위치를 조정할 수 있게 합니다. */
    }

    /* 최종 작전 구역의 작은 분류 문구입니다. */
    .operation-launch-kicker {
        color: #57d9e8;  /* 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        letter-spacing: 2.2px;  /* 글자 사이 간격입니다. */
        margin-bottom: 10px;  /* 아래쪽 여백입니다. */
    }

    /* 최종 작전 구역의 큰 제목입니다. */
    .operation-launch-title {
        color: #edf8fc;  /* 글자 색상입니다. */
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;  /* 제목 글꼴입니다. */
        font-size: clamp(20px, 2.5vw, 30px);  /* 화면 크기에 따라 글자 크기를 조절합니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        letter-spacing: 1.5px;  /* 글자 사이 간격입니다. */
        line-height: 1.4;  /* 줄 간격입니다. */
        margin-bottom: 12px;  /* 아래쪽 여백입니다. */
    }

    /* 최종 작전 구역의 설명 문구입니다. */
    .operation-launch-description {
        color: #a9c1ce;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 13px;  /* 글자 크기입니다. */
        line-height: 1.9;  /* 줄 간격입니다. */
        max-width: 850px;  /* 설명 문구의 최대 너비입니다. */
    }

    /* 최종 작전 구역의 경고 및 상태 표시 문구입니다. */
    .operation-launch-warning {
        color: #79c9d8;  /* 글자 색상입니다. */
        font-size: 10px;  /* 글자 크기입니다. */
        letter-spacing: 1.3px;  /* 글자 사이 간격입니다. */
        margin-top: 15px;  /* 위쪽 여백입니다. */
        padding-top: 12px;  /* 위쪽 안쪽 여백입니다. */
        border-top: 1px solid #294958;  /* 위쪽 구분선입니다. */
    }

    /* Streamlit에서 key를 launch_operation으로 지정한 버튼만 선택합니다. */
    .st-key-launch_operation button {
        min-height: 74px !important;  /* 버튼의 최소 높이를 74px로 설정합니다. */
        padding: 18px 26px !important;  /* 버튼 안쪽 여백입니다. */
        background: linear-gradient(100deg, #12435a, #0b2637) !important;  /* 버튼 배경 그라데이션입니다. */
        border: 2px solid #57d9e8 !important;  /* 청록색 테두리입니다. */
        border-radius: 0 !important;  /* 모서리를 둥글게 하지 않습니다. */
        color: #f0fcff !important;  /* 버튼 글자 색상입니다. */
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;  /* 버튼 글꼴입니다. */
        font-size: 17px !important;  /* 버튼 글자 크기입니다. */
        font-weight: 700 !important;  /* 버튼 글자를 굵게 표시합니다. */
        letter-spacing: 1.5px !important;  /* 글자 사이 간격입니다. */
        box-shadow: 0 0 18px rgba(87, 217, 232, 0.08);  /* 버튼 주변에 약한 빛 효과를 줍니다. */
        transition: all 0.18s ease-in-out;  /* 모든 스타일 변화를 0.18초 동안 부드럽게 적용합니다. */
    }

    /* 최종 작전 버튼 위에 마우스를 올렸을 때 적용됩니다. */
    .st-key-launch_operation button:hover {
        background: linear-gradient(100deg, #1a6079, #104057) !important;  /* 배경색을 밝게 바꿉니다. */
        border-color: #a0f3ff !important;  /* 테두리를 더 밝게 바꿉니다. */
        color: #ffffff !important;  /* 글자를 흰색으로 바꿉니다. */
        box-shadow: 0 0 22px rgba(87, 217, 232, 0.22);  /* 빛 효과를 더 강하게 만듭니다. */
        transform: translateY(-1px);  /* 버튼을 위로 1px 이동시킵니다. */
    }

    /* 최종 작전 버튼을 누르고 있는 동안 적용됩니다. */
    .st-key-launch_operation button:active {
        transform: translateY(0);  /* 위로 이동한 버튼을 원래 위치로 되돌립니다. */
    }

    /* 최종 작전 버튼 아래의 안내 문구입니다. */
    .operation-launch-hint {
        color: #79c9d8;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 12px;  /* 글자 크기입니다. */
        line-height: 1.7;  /* 줄 간격입니다. */
        text-align: center;  /* 글자를 가운데 정렬합니다. */
        margin-top: 9px;  /* 위쪽 여백입니다. */
        letter-spacing: 0.2px;  /* 글자 사이 간격입니다. */
    }

    /* 사이드바 작전 돌입 구역의 디자인입니다. */
    .sidebar-operation-panel {
        background: linear-gradient(145deg, #102b3b, #091722);  /* 패널 배경입니다. */
        border: 1px solid #3a7188;  /* 패널 테두리입니다. */
        border-top: 2px solid #57d9e8;  /* 위쪽 강조선입니다. */
        padding: 12px 10px;  /* 안쪽 여백입니다. */
        margin: 18px 0 14px 0;  /* 위쪽 18px, 아래쪽 14px의 바깥 여백입니다. */
    }

    /* 사이드바 작전 구역의 자료 번호입니다. */
    .sidebar-operation-code {
        color: #57d9e8;  /* 글자 색상입니다. */
        font-family: 'IBM Plex Mono', monospace;  /* 글꼴입니다. */
        font-size: 9px;  /* 글자 크기입니다. */
        letter-spacing: 1.3px;  /* 글자 사이 간격입니다. */
        margin-bottom: 7px;  /* 아래쪽 여백입니다. */
    }

    /* 사이드바 작전 구역의 제목입니다. */
    .sidebar-operation-title {
        color: #edf8fc;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 16px;  /* 글자 크기입니다. */
        font-weight: 700;  /* 글자를 굵게 표시합니다. */
        margin-bottom: 7px;  /* 아래쪽 여백입니다. */
    }

    /* 사이드바 작전 구역의 설명입니다. */
    .sidebar-operation-description {
        color: #a9c1ce;  /* 글자 색상입니다. */
        font-family: 'Noto Sans KR', sans-serif;  /* 한글용 글꼴입니다. */
        font-size: 11px;  /* 글자 크기입니다. */
        line-height: 1.7;  /* 줄 간격입니다. */
    }

    /* 사이드바에서 key가 sidebar_launch_operation인 버튼을 선택합니다. */
    .st-key-sidebar_launch_operation button {
        min-height: 52px !important;  /* 버튼의 최소 높이입니다. */
        padding: 12px 8px !important;  /* 버튼 안쪽 여백입니다. */
        background: linear-gradient(100deg, #12435a, #0b2637) !important;  /* 버튼 배경입니다. */
        border: 1px solid #57d9e8 !important;  /* 버튼 테두리입니다. */
        border-radius: 0 !important;  /* 모서리를 둥글게 하지 않습니다. */
        color: #f0fcff !important;  /* 글자 색상입니다. */
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;  /* 버튼 글꼴입니다. */
        font-size: 12px !important;  /* 글자 크기입니다. */
        font-weight: 700 !important;  /* 글자를 굵게 표시합니다. */
        letter-spacing: 0.5px !important;  /* 글자 사이 간격입니다. */
        box-shadow: 0 0 14px rgba(87, 217, 232, 0.08);  /* 주변에 약한 빛 효과를 줍니다. */
    }

    /* 사이드바 작전 버튼에 마우스를 올렸을 때 적용됩니다. */
    .st-key-sidebar_launch_operation button:hover {
        background: linear-gradient(100deg, #1a6079, #104057) !important;  /* 배경을 밝게 바꿉니다. */
        border-color: #a0f3ff !important;  /* 테두리를 밝게 바꿉니다. */
        color: #ffffff !important;  /* 글자를 흰색으로 바꿉니다. */
        box-shadow: 0 0 18px rgba(87, 217, 232, 0.2);  /* 빛 효과를 강하게 만듭니다. */
    }

    /* 화면 너비가 800px 이하인 경우에만 아래 스타일을 적용합니다. */
    @media (max-width: 800px) {

        /* 화면이 좁으면 상단의 항목들이 다음 줄로 넘어갈 수 있게 합니다. */
        .top-strip {
            flex-wrap: wrap;  /* 요소들이 한 줄에 들어가지 않으면 다음 줄로 배치합니다. */
        }

        /* 좁은 화면에서 메인 제목의 크기를 25px로 조절합니다. */
        .main-title {
            font-size: 25px;  /* 모바일 화면용 제목 크기입니다. */
        }

        /* 좁은 화면에서는 패널의 최소 높이 제한을 해제합니다. */
        .panel {
            min-height: auto;  /* 내용에 필요한 높이만 사용하게 합니다. */
        }

        /* 좁은 화면에서 작전 패널의 안쪽 여백을 줄입니다. */
        .operation-launch-panel {
            padding: 20px 16px;  /* 위아래 20px, 좌우 16px의 여백입니다. */
        }

        /* 좁은 화면에서 작전 제목의 크기를 조절합니다. */
        .operation-launch-title {
            font-size: 21px;  /* 모바일 화면용 제목 크기입니다. */
        }

        /* 좁은 화면에서 작전 버튼의 글자 크기와 간격을 줄입니다. */
        .st-key-launch_operation button {
            font-size: 13px !important;  /* 버튼 글자 크기입니다. */
            letter-spacing: 0.8px !important;  /* 글자 사이 간격입니다. */
        }
    }
    </style>
    """,
    unsafe_allow_html=True,  # HTML 코드를 일반 글자가 아니라 실제 HTML 요소로 해석하도록 합니다.
)


# =========================================================
# 5. 사이드바: 직접 만든 작전 메뉴
# =========================================================

# with st.sidebar: 아래에 작성한 요소는 메인 화면이 아니라 왼쪽 사이드바에 표시됩니다.
with st.sidebar:

    # HTML을 사용해 사이드바 맨 위에 프로젝트 이름과 소속을 표시합니다.
    st.markdown(
        """
        <div class="side-brand">
            <div class="side-brand-title">CELL VISION</div>
            <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML 태그를 실제 화면 요소로 표시합니다.
    )

    # 사이드바 메뉴의 첫 번째 구역 제목을 표시합니다.
    st.markdown(
        '<div class="side-section">01 / COMMAND MENU</div>',
        unsafe_allow_html=True,  # HTML을 실제 요소로 해석합니다.
    )

    # app.py를 가리키는 페이지 이동 링크를 만듭니다.
    st.page_link(
        "app.py",  # 이동할 Python 페이지 파일의 경로입니다.
        label="COMMAND CENTER / 메인 화면",  # 화면에 표시할 링크 문구입니다.
    )

    # 프로젝트 폴더 안에서 작전 브리핑 파일의 경로를 만듭니다.
    briefing_page = ROOT_DIR / "pages" / "0_작전브리핑.py"

    # exists()는 해당 경로에 파일이나 폴더가 실제로 있는지 확인합니다.
    # 파일이 존재할 때만 아래의 페이지 링크를 표시합니다.
    if briefing_page.exists():

        # 작전 브리핑 페이지로 이동할 수 있는 링크를 생성합니다.
        st.page_link(
            "pages/0_작전브리핑.py",  # 이동할 페이지 파일 경로입니다.
            label="MISSION BRIEFING / 작전 브리핑",  # 링크에 표시할 문구입니다.
        )

    # 사이드바의 두 번째 메뉴 구역 제목을 표시합니다.
    st.markdown(
        '<div class="side-section">02 / INTELLIGENCE FILES</div>',
        unsafe_allow_html=True,  # HTML을 실제 요소로 표시합니다.
    )

    # ORGANELLES 리스트에 저장된 소기관 정보를 하나씩 꺼내 반복합니다.
    # 반복할 때마다 organelle 변수에는 소기관 하나의 딕셔너리가 들어갑니다.
    for organelle in ORGANELLES:

        # 현재 소기관의 상세 페이지 파일이 존재하는지 확인합니다.
        # ROOT_DIR과 organelle["page"]를 연결하여 파일 경로를 만듭니다.
        if (ROOT_DIR / organelle["page"]).exists():

            # 파일이 존재하는 경우에만 해당 소기관의 링크를 표시합니다.
            st.page_link(
                organelle["page"],  # 현재 소기관의 상세 페이지 경로입니다.
                # f-string은 문자열 안에 변수 값을 넣을 수 있게 합니다.
                # 딕셔너리에서 자료 번호와 이름을 가져와 링크 문구를 만듭니다.
                label=f'{organelle["code"]} / {organelle["name"]}',
            )

    # 최종 작전 페이지 파일의 경로를 만듭니다.
    game_page = ROOT_DIR / "pages" / "10_작전.py"

    # 최종 작전 페이지 파일이 실제로 존재할 때만 작전 메뉴를 표시합니다.
    if game_page.exists():

        # 사이드바에 최종 작전 안내 패널을 표시합니다.
        st.markdown(
            """
            <div class="sidebar-operation-panel">
                <div class="sidebar-operation-code">BIO-10 // FINAL OPERATION</div>
                <div class="sidebar-operation-title">작전 돌입</div>
                <div class="sidebar-operation-description">
                    소기관 정보를 충분히 수집하고 세포의 작동 원리를 이해한 뒤,
                    최종 임무를 수행하라.
                </div>
            </div>
            """,
            unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
        )

        # 사이드바에서 작전 개시 버튼을 만듭니다.
        st.button(
            "INITIATE OPERATION  /  작전 개시",  # 버튼에 표시할 글자입니다.
            key="sidebar_launch_operation",  # 버튼을 구별하기 위한 고유한 이름입니다.
            use_container_width=True,  # 버튼을 사이드바 너비에 맞춰 표시합니다.
            # on_click은 버튼을 눌렀을 때 실행할 동작을 지정합니다.
            # lambda는 클릭할 때 실행할 함수를 간단하게 작성하는 문법입니다.
            # 버튼을 누르면 pages/10_작전.py 페이지로 이동합니다.
            on_click=lambda: st.switch_page("pages/10_작전.py"),
        )

    # 사이드바 아래쪽에 시스템 상태 정보를 표시합니다.
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
        unsafe_allow_html=True,  # HTML 태그와 줄바꿈을 실제 화면에 적용합니다.
    )

    # 가로 구분선을 표시합니다.
    st.markdown("---")

    # 사이드바 맨 아래에 작은 글씨로 프로젝트 정보를 표시합니다.
    st.caption("CELL VISION / INTERNAL USE")


# =========================================================
# 6. 상단 전술 시스템 바
# =========================================================

# datetime.now()는 현재 날짜와 시간을 가져옵니다.
# strftime("%Y-%m-%d")는 날짜를 연도-월-일 형식의 문자열로 바꿉니다.
# 예를 들어 2026년 11월 9일이면 "2026-11-09" 형태가 됩니다.
current_time = datetime.now().strftime("%Y-%m-%d")

# f""" ... """는 여러 줄 문자열 안에 변수 값을 넣을 수 있는 f-string입니다.
# {current_time} 부분에 위에서 만든 현재 날짜가 들어갑니다.
st.markdown(
    f"""
    <div class="top-strip">
        <span>CV // BIOLOGICAL INTELLIGENCE SYSTEM</span>
        <span>SECURITY LEVEL: <strong>RESTRICTED</strong></span>
        <span>SYSTEM STATUS: <strong>OPERATIONAL</strong></span>
        <span>{current_time}</span>
    </div>
    """,
    unsafe_allow_html=True,  # 문자열 안의 HTML을 실제 화면에 표시합니다.
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
    unsafe_allow_html=True,  # HTML 태그에 지정한 CSS 디자인을 적용합니다.
)


# =========================================================
# 7. 상황 정보 패널
# =========================================================

# 화면을 너비가 같은 세 개의 열로 나눕니다.
# 반환된 세 개의 열 객체를 각각 변수에 저장합니다.
status_col1, status_col2, status_col3 = st.columns(3)

# 첫 번째 열 안에 작성한 요소를 표시합니다.
with status_col1:

    # 첫 번째 패널에 작전 식별 정보를 표시합니다.
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">OPERATION IDENTIFIER</div>
            <div class="panel-value">BIO-OPS / 001</div>
            <div class="panel-note">MISSION: CELLULAR ANALYSIS</div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML을 실제 패널로 표시합니다.
    )

# 두 번째 열 안에 작성한 요소를 표시합니다.
with status_col2:

    # 두 번째 패널에 현재 작전 상태를 표시합니다.
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">CURRENT OPERATION STATUS</div>
            <div class="panel-value"><span class="status-dot">●</span> STANDING BY</div>
            <div class="panel-note">AWAITING ANALYSIS INPUT</div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML을 실제 패널로 표시합니다.
    )

# 세 번째 열 안에 작성한 요소를 표시합니다.
with status_col3:

    # 세 번째 패널에 분석 대상인 동물세포 정보를 표시합니다.
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">TARGET PROFILE</div>
            <div class="panel-value">ANIMAL CELL</div>
            <div class="panel-note">BIOLOGICAL STRUCTURE / CLASSIFIED</div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML을 실제 패널로 표시합니다.
    )


# =========================================================
# 8. 중앙 분석 화면
# =========================================================

# 중앙 분석 화면의 구역 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">LIVE ANALYSIS // TARGET RECONNAISSANCE</div>',
    unsafe_allow_html=True,  # HTML 제목에 CSS 디자인을 적용합니다.
)

# 화면을 왼쪽과 오른쪽 두 열로 나눕니다.
# [1, 1]은 두 열의 너비 비율이 1:1이라는 의미입니다.
# gap="medium"은 두 열 사이에 중간 크기의 간격을 둡니다.
left_col, right_col = st.columns([1, 1], gap="medium")

# 왼쪽 열에 표시할 내용을 작성합니다.
with left_col:

    # 왼쪽 열의 제목을 표시합니다.
    st.markdown(
        '<div class="section-bar">TARGET IMAGE // CELLULAR OVERVIEW</div>',
        unsafe_allow_html=True,  # HTML 제목에 CSS 디자인을 적용합니다.
    )

    # 이미지 폴더 안의 cell.png 파일 경로를 만듭니다.
    cell_image = IMAGE_DIR / "cell.png"

    # cell.png 파일이 실제로 존재하는지 확인합니다.
    if cell_image.exists():

        # 이미지 파일이 존재하면 화면에 표시합니다.
        st.image(
            str(cell_image),  # Path 객체를 문자열 경로로 바꾸어 전달합니다.
            use_container_width=True,  # 이미지가 콘텐츠 영역 너비에 맞게 표시됩니다.
            caption="TARGET 001 / ANIMAL CELL STRUCTURE",  # 이미지 아래에 표시할 설명입니다.
        )

    # 위 조건이 거짓이면 이미지가 없다는 안내를 표시합니다.
    else:
        st.warning(
            "세포 전체 이미지가 없습니다. images 폴더에 cell.png 파일이 있는지 확인하라."
        )

    # 기존 세포 분석 지시문을 표시합니다.
    st.markdown(
        """
        <div class="mission-box">
            <div class="mission-box-title">COMMAND DIRECTIVE // 001</div>
            <div class="mission-box-text">
                세포는 여러 소기관이 유기적으로 협력하는 생명 시스템이다.
                각 소기관의 구조와 기능을 확인하고, 물질 합성·수송·에너지 전환 과정이
                어떻게 연결되는지 분석하라.
            </div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
    )

# 오른쪽 열에 표시할 내용을 작성합니다.
with right_col:

    # 임무 지시 패널, 목표 목록, 시스템 안내를 세로로 표시합니다.
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">MISSION DIRECTIVE</div>
            <div class="panel-value">CELL / 001</div>
            <div class="panel-note">
                세포의 주요 구조를 식별하고 각 소기관의 기능과 상호작용을 분석하라.
            </div>
        </div>

        <div class="section-bar">PRIMARY OBJECTIVES</div>
        <div class="data-row"><span>OBJECTIVE 01</span><span>구조 식별</span></div>
        <div class="data-row"><span>OBJECTIVE 02</span><span>기능 분석</span></div>
        <div class="data-row"><span>OBJECTIVE 03</span><span>물질 이동</span></div>
        <div class="data-row"><span>OBJECTIVE 04</span><span>시스템 이해</span></div>

        <div class="section-bar" style="margin-top: 18px;">SYSTEM INTELLIGENCE</div>
        <div class="intelligence-notice">
            <div class="intelligence-notice-text">
                아래 파일들은 우리 요원들이 공수한 기밀 정보다. 숙지하라.
            </div>
            <div class="intelligence-notice-directive">
                정보를 수집한 뒤 작전을 수행하라.
            </div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML 태그와 CSS 스타일을 실제 화면에 적용합니다.
    )


# =========================================================
# 9. 소기관 정보 파일
# =========================================================

# 소기관별 상세 자료 구역의 제목을 표시합니다.
st.markdown(
    """
    <div class="section-bar" style="font-size: 15px;">
        확보한 기밀 자료를 전부 숙지하고 작전에 돌입하라.
    </div>
    """,
    unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
)

# 소기관 정보 파일을 선택하라는 안내 문구를 표시합니다.
st.markdown(
    """
    <div class="subtitle">
        SELECT AN INTELLIGENCE FILE TO ACCESS DETAILED BIOLOGICAL INFORMATION.
    </div>
    """,
    unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
)

# range(0, len(ORGANELLES), 3)은 0부터 시작해 3씩 증가하는 숫자를 만듭니다.
# len(ORGANELLES)는 ORGANELLES 리스트에 들어 있는 소기관의 개수입니다.
# 소기관이 9개라면 start에는 0, 3, 6이 차례대로 들어갑니다.
# 따라서 소기관 정보를 세 개씩 묶어 화면에 표시할 수 있습니다.
for start in range(0, len(ORGANELLES), 3):

    # start 위치부터 start + 3 직전까지의 소기관을 잘라냅니다.
    # 예를 들어 start가 0이면 인덱스 0, 1, 2의 소기관을 가져옵니다.
    # 리스트의 일부를 가져오는 문법을 슬라이싱이라고 합니다.
    row_items = ORGANELLES[start:start + 3]

    # 소기관 카드 세 개를 나란히 표시할 수 있도록 세 개의 열을 만듭니다.
    columns = st.columns(3, gap="medium")

    # zip()은 columns와 row_items의 항목을 순서대로 하나씩 짝지어 줍니다.
    # 예를 들어 첫 번째 열에는 첫 번째 소기관, 두 번째 열에는 두 번째 소기관이 배치됩니다.
    for column, organelle in zip(columns, row_items):

        # 현재 소기관 카드가 표시될 열을 지정합니다.
        with column:

            # 소기관의 자료 번호, 이름, 설명을 HTML 카드로 표시합니다.
            # f-string을 사용해 organelle 딕셔너리의 실제 값을 문자열에 넣습니다.
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
                unsafe_allow_html=True,  # HTML을 실제 카드로 표시합니다.
            )

            # 현재 소기관에 해당하는 이미지 파일 경로를 만듭니다.
            # organelle["image"]는 ORGANELLES 리스트에 저장된 이미지 이름입니다.
            image_path = IMAGE_DIR / organelle["image"]

            # 해당 이미지 파일이 존재하는지 확인합니다.
            if image_path.exists():

                # 이미지가 있으면 화면에 표시합니다.
                st.image(
                    str(image_path),  # Path 객체를 문자열 경로로 변환합니다.
                    use_container_width=True,  # 카드 열의 너비에 맞춰 이미지를 표시합니다.
                )

            # 이미지가 없으면 아래 안내 메시지를 표시합니다.
            else:

                # 찾을 수 없는 이미지 파일 이름을 사용자에게 알려 줍니다.
                st.warning(
                    f'이미지 파일을 찾을 수 없다: images/{organelle["image"]}'
                )

            # 현재 소기관의 상세 페이지 파일 경로를 만듭니다.
            page_path = ROOT_DIR / organelle["page"]

            # 해당 상세 페이지 파일이 실제로 존재하는지 확인합니다.
            if page_path.exists():

                # 파일이 존재하면 상세 페이지로 이동할 수 있는 링크를 표시합니다.
                st.page_link(
                    organelle["page"],  # 이동할 상세 페이지의 경로입니다.
                    label=f'ACCESS FILE / {organelle["name"]}',  # 소기관 이름을 링크 문구에 넣습니다.
                    use_container_width=True,  # 링크를 열 너비에 맞춰 표시합니다.
                )

            # 상세 페이지 파일이 없으면 아래 안내 문구를 표시합니다.
            else:

                # 어떤 상세 페이지 파일이 없는지 경로를 알려 줍니다.
                st.caption(
                    f'상세 페이지 파일을 확인하라: {organelle["page"]}'
                )


# =========================================================
# 10. 작전 지침
# =========================================================

# 소기관을 분석할 때 따라야 할 지침 구역의 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">FIELD INSTRUCTIONS // OPERATION PROTOCOL</div>',
    unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
)

# 작전 수행 순서와 설명을 튜플 형태로 저장합니다.
# 튜플은 여러 값을 하나로 묶어 저장하는 자료형이며 소괄호 ()를 사용합니다.
# 여기서는 각 항목에 지침 제목과 설명이라는 두 값을 저장합니다.
protocols = [
    (
        "PROTOCOL 01 — OBSERVE",  # 첫 번째 지침의 제목입니다.
        "세포 전체 이미지를 관찰하고 각 소기관의 위치와 형태를 확인하라.",  # 첫 번째 지침의 설명입니다.
    ),
    (
        "PROTOCOL 02 — IDENTIFY",  # 두 번째 지침의 제목입니다.
        "소기관 정보 파일에 접근해 구조, 기능, 세포 내 역할을 분석하라.",  # 두 번째 지침의 설명입니다.
    ),
    (
        "PROTOCOL 03 — CONNECT",  # 세 번째 지침의 제목입니다.
        "단백질 합성 및 이동, 세포 호흡 등 세포 내 과정의 연결 관계를 파악하라.",  # 세 번째 지침의 설명입니다.
    ),
]

# protocols 리스트에 저장된 지침을 하나씩 꺼내 반복합니다.
# 각 항목은 두 값으로 이루어져 있으므로 title과 description에 나누어 저장합니다.
for title, description in protocols:

    # 현재 지침의 제목과 설명을 HTML 상자 안에 표시합니다.
    # f-string의 {title}과 {description}에 반복 중인 값이 들어갑니다.
    st.markdown(
        f"""
        <div class="mission-box">
            <div class="mission-box-title">{title}</div>
            <div class="mission-box-text">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,  # HTML을 실제 화면 요소로 표시합니다.
    )


# =========================================================
# 11. 작전 돌입 구역
# =========================================================

# 최종 작전 개시 구역의 제목을 표시합니다.
st.markdown(
    '<div class="section-bar">FINAL DIRECTIVE // OPERATION LAUNCH</div>',
    unsafe_allow_html=True,  # HTML 제목에 CSS 디자인을 적용합니다.
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
            대원, 분석실에서 확보한 생물학적 정보를 다시 확인하라.
            각 소기관의 기능과 세포 내부의 작동 원리를 파악하고
            최종 작전을 개시하라.<br>
            지금까지 습득한 지식을 활용해 주어진 임무를 완수하라.
        </div>
        <div class="operation-launch-warning">
            MISSION STATUS: STANDING BY
            &nbsp; / &nbsp;
            AUTHORIZATION REQUIRED
        </div>
    </div>
    """,
    unsafe_allow_html=True,  # HTML 태그를 실제 화면 요소로 표시합니다.
)

# 최종 작전 페이지의 파일 경로를 만듭니다.
game_page = ROOT_DIR / "pages" / "10_작전.py"

# 최종 작전 페이지 파일이 실제로 존재하는지 확인합니다.
if game_page.exists():

    # 작전 페이지로 이동하는 버튼을 생성합니다.
    st.button(
        "INITIATE OPERATION  /  작전 돌입",  # 버튼에 표시할 문구입니다.
        key="launch_operation",  # 버튼을 구분하기 위한 고유한 키입니다.
        type="primary",  # Streamlit에서 주요 동작 버튼으로 표시합니다.
        use_container_width=True,  # 버튼을 사용 가능한 화면 너비에 맞춥니다.
        # 버튼을 누르면 작전 페이지로 이동하도록 지정합니다.
        on_click=lambda: st.switch_page("pages/10_작전.py"),
    )

    # 작전 개시 버튼 아래에 안내 문구를 표시합니다.
    st.markdown(
        '<div class="operation-launch-hint">'
        '정보를 충분히 수집했다면 지금 작전에 돌입하라.'
        '</div>',
        unsafe_allow_html=True,  # HTML을 실제 안내 문구로 표시합니다.
    )

# 위 조건이 거짓이라면 작전 페이지 파일이 없는 경우입니다.
else:

    # 작전 페이지 파일을 찾을 수 없다는 오류 메시지를 표시합니다.
    st.error(
        "작전 페이지를 찾을 수 없다. "
        "pages/10_작전.py 파일이 존재하는지 확인하라."
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
    unsafe_allow_html=True,  # HTML 요소를 실제 화면에 표시합니다.
)
