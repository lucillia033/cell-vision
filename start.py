
import streamlit as st
# Streamlit은 파이썬으로 웹 페이지를 만들 수 있게 해 주는 도구입니다.
# st라는 이름으로 줄여서 사용합니다.

from datetime import datetime
# 현재 날짜와 시간을 가져오기 위해 datetime 기능을 불러옵니다.


# =========================================================
# 1. 기본 설정
# =========================================================

# 웹 페이지의 기본 정보를 설정합니다.
st.set_page_config(
    page_title="CELL VISION | Mission Briefing",  # 브라우저 탭 등에 표시할 페이지 제목
    page_icon=None,  # 별도의 페이지 아이콘을 지정하지 않음
    layout="wide",  # 화면 너비를 넓게 사용하도록 설정
    initial_sidebar_state="collapsed",  # 처음 페이지를 열었을 때 사이드바를 접어 둠
)

# =========================================================
# 2. 작전 브리핑 전용 디자인
# =========================================================

# st.markdown()은 글이나 HTML을 화면에 표시하는 기능입니다.
# 여기서는 HTML과 CSS 코드를 이용해 페이지 디자인을 설정합니다.
st.markdown(
    """
    <style>
    /* 외부 글꼴을 가져옵니다. IBM Plex Mono는 영문과 숫자에, Noto Sans KR은 한글에 사용합니다. */
    /* wght@400;500;600;700은 글꼴의 굵기 종류를 의미합니다. */
    @import url(
        'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap'
    );

    /* :root는 페이지 전체에서 공통으로 사용할 CSS 변수를 정의하는 영역입니다. */
    /* --이름: 값; 형식으로 색상을 저장하면 여러 곳에서 같은 색상을 사용할 수 있습니다. */
    :root {
        --bg: #020810;       /* 기본 배경에 사용할 어두운 색 */
        --panel: #06121e;    /* 패널에 사용할 어두운 색 */
        --cyan: #24d9f5;      /* 강조할 때 사용할 청록색 */
        --cyan-soft: #57d9e8; /* 조금 더 부드러운 청록색 */
        --text: #d9edf8;      /* 기본 글자색 */
        --muted: #7899ad;     /* 덜 강조할 글자색 */
        --line: #17465a;      /* 구분선에 사용할 색 */
    }

    /* html은 문서 전체, body는 페이지 본문을 의미합니다. */
    /* [class*="css"]는 class 이름에 css라는 글자가 포함된 요소를 선택합니다. */
    /* font-family는 글꼴을 지정하며, 앞의 글꼴을 사용할 수 없으면 뒤의 글꼴을 사용합니다. */
    html, body, [class*="css"] {
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    /* .stApp은 Streamlit 앱의 전체 화면 영역을 가리킵니다. */
    .stApp {
        /* background는 화면의 배경을 설정합니다. */
        background:
            /* radial-gradient는 한 지점에서 바깥으로 퍼지는 원형 배경 효과입니다. */
            radial-gradient(
                ellipse at 50% 42%,  /* 배경 효과의 중심을 가로 50%, 세로 42% 위치로 지정 */
                rgba(0, 94, 133, 0.15), /* 투명도가 포함된 푸른색 */
                transparent 54% /* 54% 지점부터 투명하게 만듦 */
            ),
            /* linear-gradient는 한 방향으로 색상이 변하는 배경입니다. */
            linear-gradient(180deg, #030b14 0%, #020810 100%);
            /* 180deg는 위에서 아래로 향하는 방향입니다. */
            /* 0%는 시작 지점, 100%는 끝 지점의 색상입니다. */

        color: var(--text); /* 전체 글자색을 위에서 정의한 변수로 설정 */
    }

    /* 아래 세 선택자는 Streamlit의 기본 사이드바와 페이지 메뉴 관련 요소입니다. */
    /* 쉼표로 여러 선택자를 연결하면 같은 디자인 규칙을 모두 적용합니다. */
    [data-testid="stSidebar"],
    [data-testid="stSidebarNav"],
    [data-testid="collapsedControl"] {
        display: none !important;
        /* display: none은 요소를 화면에서 숨깁니다. */
        /* !important는 다른 CSS 설정이 있더라도 이 설정을 우선 적용하도록 합니다. */
    }

    /* Streamlit 기본 상단 헤더의 배경을 투명하게 만듭니다. */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* #MainMenu는 기본 메뉴, footer는 기본 하단 영역을 가리킵니다. */
    #MainMenu, footer {
        visibility: hidden;
        /* visibility: hidden은 화면에 보이지 않게 합니다. */
        /* display: none과 달리 요소가 원래 차지하던 공간이 남을 수 있습니다. */
    }

    /* .block-container는 Streamlit에서 본문 내용을 담는 영역입니다. */
    .block-container {
        max-width: 1600px; /* 본문이 최대 1600px까지만 넓어지도록 제한 */
        padding: 1.1rem 2.5rem 1.5rem;
        /* padding은 요소 안쪽의 여백입니다. */
        /* 세 값은 위쪽 1.1rem, 좌우 2.5rem, 아래쪽 1.5rem을 의미합니다. */
        /* rem은 기본 글자 크기를 기준으로 하는 길이 단위입니다. */
    }

    /* 상단 시스템 바 */

    /* .system-header는 로고와 시스템 상태를 담는 영역입니다. */
    .system-header {
        display: flex;
        /* flex는 내부 요소들을 유연하게 배치하는 방식입니다. */

        justify-content: space-between;
        /* 내부 요소를 양쪽 끝으로 배치하고 사이 공간을 나눕니다. */

        align-items: center;
        /* 내부 요소들을 세로 방향 가운데에 맞춥니다. */

        gap: 16px;
        /* 내부 요소 사이에 16px의 간격을 둡니다. */

        flex-wrap: wrap;
        /* 공간이 부족하면 내부 요소가 다음 줄로 내려가도록 합니다. */

        border-bottom: 1px solid var(--line);
        /* 아래쪽에 1px 두께의 실선을 추가합니다. */

        padding: 10px 4px 17px;
        /* 위쪽 10px, 좌우 4px, 아래쪽 17px의 안쪽 여백입니다. */

        margin-bottom: 30px;
        /* 이 영역 아래에 30px의 바깥쪽 여백을 둡니다. */
    }

    /* .brand는 CELL VISION 로고의 글자 디자인을 설정합니다. */
    .brand {
        color: #e6f6ff; /* 로고 글자색 */
        font-size: clamp(17px, 2vw, 25px);
        /* clamp(최솟값, 기준값, 최댓값)은 화면 크기에 따라 크기를 조절합니다. */
        /* 여기서는 글자 크기가 17px보다 작아지거나 25px보다 커지지 않도록 합니다. */

        font-weight: 700; /* 글자를 굵게 표시 */
        letter-spacing: 3px; /* 글자 사이 간격을 3px로 설정 */
    }

    /* .brand-symbol은 로고 앞에 있는 기호의 디자인을 설정합니다. */
    .brand-symbol {
        color: var(--cyan); /* 기호의 색상을 청록색으로 지정 */
        margin-right: 12px; /* 기호와 로고 글자 사이에 12px의 여백을 둠 */
    }

    /* .brand-sub는 로고 옆의 부대 이름을 꾸밉니다. */
    .brand-sub {
        color: var(--muted); /* 글자색 */
        font-size: 10px; /* 글자 크기 */
        letter-spacing: 1.6px; /* 글자 사이 간격 */
        margin-left: 12px; /* 왼쪽에 12px의 바깥쪽 여백을 둠 */
    }

    /* .system-status는 오른쪽 시스템 상태 문구의 디자인입니다. */
    .system-status {
        color: var(--cyan); /* 글자색 */
        font-size: 10px; /* 글자 크기 */
        letter-spacing: 1.3px; /* 글자 사이 간격 */
        text-align: right; /* 글자를 오른쪽으로 정렬 */
    }

    /* 메인 브리핑 프레임 */

    /* .briefing-frame은 작전 브리핑 전체를 감싸는 큰 상자입니다. */
    .briefing-frame {
        position: relative;
        /* 내부의 일부 요소를 이 상자를 기준으로 배치할 수 있게 합니다. */

        overflow: hidden;
        /* 상자 경계를 넘어가는 내용은 화면에 보이지 않도록 잘라냅니다. */

        background:
            /* 135deg 방향으로 두 가지 어두운 색상을 섞어 배경을 만듭니다. */
            linear-gradient(
                135deg,
                rgba(7, 24, 39, 0.97),
                rgba(2, 9, 17, 0.99) 68%
            );

        border: 1px solid #17627a;
        /* 상자의 네 방향에 1px 두께의 테두리를 추가합니다. */

        border-top: 2px solid var(--cyan);
        /* 위쪽 테두리만 2px 두께의 청록색으로 설정합니다. */

        padding: clamp(22px, 4vw, 58px);
        /* 화면 크기에 따라 안쪽 여백을 22px~58px 사이에서 조절합니다. */

        box-shadow:
            /* 상자 바깥쪽에 은은한 푸른빛을 추가합니다. */
            0 0 28px rgba(0, 190, 235, 0.06),
            /* inset은 상자 안쪽에 빛 효과를 적용합니다. */
            inset 0 0 35px rgba(0, 115, 160, 0.035);
    }

    /* ::before는 HTML에 직접 작성하지 않은 장식 요소를 CSS로 추가하는 기능입니다. */
    .briefing-frame::before {
        content: "";
        /* 내용이 없는 가상 요소를 생성합니다. */

        position: absolute;
        /* 부모인 briefing-frame을 기준으로 위치를 정할 수 있게 합니다. */

        inset: 7px;
        /* 상자의 위, 오른쪽, 아래, 왼쪽에서 각각 7px 떨어지도록 설정합니다. */

        border: 1px solid rgba(39, 128, 156, 0.18);
        /* 안쪽에 희미한 테두리를 추가합니다. */

        pointer-events: none;
        /* 장식 요소가 마우스 클릭을 방해하지 않도록 합니다. */
    }

    /* 브리핑 상단의 미션 번호와 기밀 분류 문구를 배치합니다. */
    .briefing-topline {
        display: flex; /* 내부 요소를 가로로 배치 */
        justify-content: space-between; /* 양쪽 끝으로 배치 */
        align-items: center; /* 세로 가운데 정렬 */
        gap: 12px; /* 요소 사이 간격 */
        flex-wrap: wrap; /* 공간이 부족하면 다음 줄로 이동 */

        color: var(--cyan); /* 글자색 */
        font-size: 11px; /* 글자 크기 */
        letter-spacing: 2px; /* 글자 사이 간격 */

        border-bottom: 1px solid #16465a; /* 아래쪽 구분선 */
        padding-bottom: 13px; /* 내용과 구분선 사이의 안쪽 여백 */
        margin-bottom: 28px; /* 구분선 아래쪽의 바깥 여백 */
    }

    /* .mission-index는 CELL VISION / CLASSIFIED 문구의 색상을 설정합니다. */
    .mission-index {
        color: #8bc7d9;
    }

    /* .hero-title은 가장 큰 제목인 CELL VISION을 꾸밉니다. */
    .hero-title {
        color: #e8f7ff; /* 제목 색상 */
        font-size: clamp(40px, 6vw, 78px); /* 화면 크기에 따라 글자 크기를 40~78px로 조절 */
        line-height: 1.08; /* 줄 사이 높이를 글자 크기의 1.08배로 설정 */
        letter-spacing: 3px; /* 글자 사이 간격 */
        font-weight: 700; /* 굵은 글자 */
        margin: 0; /* 바깥쪽 여백을 없앰 */
        text-shadow: 0 0 24px rgba(45, 198, 255, 0.13);
        /* 제목 주변에 희미한 푸른빛을 추가합니다. */
    }

    /* .hero-subtitle은 메인 제목 아래의 부제목을 꾸밉니다. */
    .hero-subtitle {
        color: var(--cyan); /* 글자색 */
        font-size: clamp(11px, 1.5vw, 18px); /* 화면에 따라 11~18px로 조절 */
        letter-spacing: clamp(2px, 0.5vw, 6px); /* 화면에 따라 글자 간격 조절 */
        margin-top: 12px; /* 위쪽 여백 */
        font-weight: 600; /* 글자를 비교적 굵게 표시 */
    }

    /* .hero-tagline은 제목 아래의 한국어 소개 문구를 꾸밉니다. */
    .hero-tagline {
        color: #a6d9ed; /* 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글에 사용할 글꼴 */
        font-size: clamp(14px, 1.6vw, 19px); /* 화면에 따라 14~19px로 조절 */
        margin-top: 19px; /* 위쪽 여백 */
        line-height: 1.8; /* 줄 사이 간격 */
    }

    /* .cyan-divider는 구역 사이를 나누는 가로선입니다. */
    .cyan-divider {
        height: 1px; /* 가로선의 높이 */

        /* 왼쪽은 청록색으로 시작해 오른쪽으로 갈수록 어두워지고 투명해집니다. */
        background: linear-gradient(
            90deg,
            var(--cyan),
            #17546b 68%,
            transparent
        );

        margin: 26px 0;
        /* 위아래에는 26px, 좌우에는 0px의 바깥 여백을 둡니다. */
    }

    /* 상태 정보 */

    /* .status-panel은 작전 상태를 표시하는 상자입니다. */
    .status-panel {
        background: rgba(3, 16, 27, 0.7); /* 반투명한 어두운 배경 */
        border-left: 2px solid var(--cyan); /* 왼쪽에 청록색 테두리 */
        padding: 14px 18px; /* 위아래 14px, 좌우 18px의 안쪽 여백 */
        margin-bottom: 20px; /* 아래쪽 여백 */
    }

    /* .status-label은 OPERATION STATUS 같은 항목 이름을 꾸밉니다. */
    .status-label {
        color: var(--muted); /* 흐린 글자색 */
        font-size: 9px; /* 글자 크기 */
        letter-spacing: 1.5px; /* 글자 사이 간격 */
        margin-bottom: 8px; /* 아래쪽 여백 */
    }

    /* .status-value는 실제 상태 정보의 글자 디자인입니다. */
    .status-value {
        color: #bdefff; /* 글자색 */
        font-size: 12px; /* 글자 크기 */
        line-height: 1.9; /* 줄 사이 간격 */
    }

    /* ONLINE과 READY 같은 상태 문구를 초록색으로 표시합니다. */
    .online {
        color: #7ce5b4;
    }

    /* 작전 설명 */

    /* .section-label은 작전 개요 같은 구역 제목을 꾸밉니다. */
    .section-label {
        color: var(--cyan); /* 글자색 */
        font-size: 11px; /* 글자 크기 */
        letter-spacing: 2px; /* 글자 사이 간격 */
        margin-bottom: 17px; /* 아래쪽 여백 */
    }

    /* .welcome-title은 대원에게 전달하는 주요 안내 문구입니다. */
    .welcome-title {
        color: #e3f5ff; /* 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글 글꼴 */
        font-size: clamp(19px, 2vw, 27px); /* 화면에 따라 19~27px로 조절 */
        line-height: 1.6; /* 줄 사이 간격 */
        font-weight: 700; /* 굵은 글자 */
        margin-bottom: 16px; /* 아래쪽 여백 */
    }

    /* .briefing-text는 작전 내용을 설명하는 본문입니다. */
    .briefing-text {
        color: #9fc3d5; /* 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글 글꼴 */
        font-size: 14px; /* 글자 크기 */
        line-height: 2; /* 줄 사이 간격을 글자 크기의 2배로 설정 */
    }

    /* .final-directive는 작전 설명 마지막의 강조 문구입니다. */
    .final-directive {
        color: var(--cyan); /* 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글 글꼴 */
        font-size: 14px; /* 글자 크기 */
        font-weight: 700; /* 굵은 글자 */
        margin-top: 17px; /* 위쪽 여백 */
    }

    /* 임무 목표 */

    /* .objectives-panel은 세 가지 임무 목표를 담는 상자입니다. */
    .objectives-panel {
        background: rgba(4, 18, 30, 0.78); /* 반투명한 어두운 배경 */
        border: 1px solid #19536a; /* 상자 테두리 */
        padding: 22px; /* 안쪽 여백 */
        height: 100%; /* 부모 영역의 높이를 채움 */
        box-sizing: border-box; /* 여백과 테두리를 포함해 크기를 계산 */
    }

    /* .objective는 임무 하나의 번호와 설명을 묶는 영역입니다. */
    .objective {
        display: flex; /* 번호와 설명을 가로로 배치 */
        align-items: flex-start; /* 위쪽을 기준으로 정렬 */
        gap: 15px; /* 번호와 설명 사이 간격 */
        padding: 13px 0; /* 위아래 여백 */
        border-bottom: 1px solid rgba(33, 83, 104, 0.4);
        /* 각 임무 아래에 희미한 구분선을 추가합니다. */
    }

    /* 마지막 임무에는 아래쪽 구분선을 표시하지 않습니다. */
    .objective:last-child {
        border-bottom: none;
    }

    /* .objective-number는 01, 02, 03과 같은 임무 번호를 꾸밉니다. */
    .objective-number {
        color: var(--cyan); /* 번호 색상 */
        font-size: 22px; /* 번호 크기 */
        font-weight: 700; /* 굵은 번호 */
        min-width: 34px; /* 번호 영역의 최소 너비를 확보해 설명이 밀리지 않게 함 */
    }

    /* .objective-title은 각 임무의 이름을 꾸밉니다. */
    .objective-title {
        color: #d9eff9; /* 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글 글꼴 */
        font-size: 14px; /* 글자 크기 */
        font-weight: 600; /* 글자 굵기 */
    }

    /* .objective-description은 임무 이름 아래의 세부 설명입니다. */
    .objective-description {
        color: #789fb2; /* 본문보다 흐린 글자색 */
        font-family: 'Noto Sans KR', sans-serif; /* 한글 글꼴 */
        font-size: 11px; /* 글자 크기 */
        line-height: 1.8; /* 줄 사이 간격 */
        margin-top: 5px; /* 임무 이름과의 위쪽 간격 */
    }

    /* 시작 버튼 */

    /* Streamlit 버튼을 담는 영역의 너비와 위치를 설정합니다. */
    div[data-testid="stButton"] {
        margin: 0 auto;
        /* 좌우 바깥 여백을 자동으로 계산해 가운데에 배치합니다. */

        max-width: 600px;
        /* 버튼 영역이 600px보다 넓어지지 않도록 제한합니다. */
    }

    /* stButton 영역 안에 있는 실제 버튼을 선택합니다. */
    div[data-testid="stButton"] > button {
        width: 100%; /* 버튼이 부모 영역의 너비를 모두 사용 */
        min-height: 76px; /* 버튼의 최소 높이 */

        /* 버튼 배경을 왼쪽에서 가운데까지 밝아졌다가 다시 어두워지게 설정합니다. */
        background: linear-gradient(
            105deg,
            #06263a,
            #08415a 50%,
            #06263a
        ) !important;

        color: #40e4ff !important; /* 버튼 글자색 */
        border: 2px solid #19cbe9 !important; /* 테두리 두께와 색상 */
        border-radius: 0 !important; /* 모서리를 둥글게 하지 않음 */
        font-family: 'IBM Plex Mono', monospace !important; /* 버튼 글꼴 */
        font-size: clamp(15px, 2vw, 21px) !important; /* 화면에 따라 글자 크기를 15~21px로 조절 */
        font-weight: 700 !important; /* 굵은 글자 */
        letter-spacing: 3px !important; /* 글자 사이 간격 */

        /* 버튼 바깥과 안쪽에 은은한 빛 효과를 추가합니다. */
        box-shadow:
            0 0 12px rgba(0, 204, 245, 0.14),
            inset 0 0 18px rgba(0, 188, 230, 0.08);

        transition: all 0.2s ease;
        /* 버튼에 변화가 생기면 0.2초 동안 부드럽게 바뀌게 합니다. */
    }

    /* 마우스를 버튼 위에 올렸을 때 적용되는 디자인입니다. */
    div[data-testid="stButton"] > button:hover {
        background: #0c3c53 !important; /* 배경색을 변경 */
        color: #ffffff !important; /* 글자색을 흰색으로 변경 */
        border-color: #8cf2ff !important; /* 테두리를 더 밝게 변경 */

        /* 마우스를 올리면 빛 효과가 더 강해집니다. */
        box-shadow:
            0 0 25px rgba(0, 211, 255, 0.28),
            inset 0 0 20px rgba(0, 188, 230, 0.14);

        transform: translateY(-1px);
        /* 버튼을 세로 방향으로 1px 위로 움직입니다. */
    }

    /* 키보드로 버튼을 선택했을 때 적용되는 디자인입니다. */
    div[data-testid="stButton"] > button:focus {
        box-shadow: 0 0 0 2px #020810,
                    0 0 0 4px var(--cyan) !important;
        /* 버튼 바깥에 두 겹의 테두리처럼 보이는 효과를 추가합니다. */
    }

    /* 버튼 아래의 안내 문구를 꾸밉니다. */
    .button-caption {
        text-align: center; /* 가운데 정렬 */
        color: #66899c; /* 글자색 */
        font-size: 9px; /* 글자 크기 */
        letter-spacing: 2px; /* 글자 사이 간격 */
        margin-top: 12px; /* 버튼과의 위쪽 간격 */
    }

    /* 하단 정보 */

    /* .system-footer는 페이지 아래쪽의 프로젝트 이름과 날짜를 담는 영역입니다. */
    .system-footer {
        display: flex; /* 내부 요소를 가로로 배치 */
        justify-content: space-between; /* 왼쪽과 오른쪽 끝으로 배치 */
        align-items: center; /* 세로 가운데 정렬 */
        flex-wrap: wrap; /* 공간이 부족하면 다음 줄로 이동 */
        gap: 12px; /* 요소 사이 간격 */

        border-top: 1px solid #15394b; /* 위쪽 구분선 */
        padding: 15px 4px 0; /* 위쪽 15px, 좌우 4px, 아래쪽 0px */
        margin-top: 25px; /* 위쪽 바깥 여백 */

        color: #66889b; /* 글자색 */
        font-size: 9px; /* 글자 크기 */
        letter-spacing: 1.2px; /* 글자 간격 */
        line-height: 1.8; /* 줄 사이 간격 */
    }

    /* 하단 정보 중 강조할 글자의 색상을 지정합니다. */
    .footer-highlight {
        color: var(--cyan);
    }

    /* 화면 너비가 800px 이하일 때 적용되는 디자인입니다. */
    @media (max-width: 800px) {

        /* 작은 화면에서는 본문 좌우 여백을 줄입니다. */
        .block-container {
            padding: 0.7rem 1rem 1rem;
        }

        /* 상단 헤더 아래의 여백을 줄입니다. */
        .system-header {
            margin-bottom: 16px;
        }

        /* 브리핑 상자의 안쪽 여백을 줄입니다. */
        .briefing-frame {
            padding: 20px 16px;
        }

        /* 작은 화면에서는 제목의 글자 사이 간격을 줄입니다. */
        .hero-title {
            letter-spacing: 1px;
        }

        /* 작은 화면에서는 부제목의 글자 사이 간격을 줄입니다. */
        .hero-subtitle {
            letter-spacing: 2px;
        }

        /* 임무 목표 상자 위쪽에 12px의 여백을 추가합니다. */
        .objectives-panel {
            margin-top: 12px;
        }

        /* 작은 화면에서는 버튼 높이와 글자 사이 간격을 줄입니다. */
        div[data-testid="stButton"] > button {
            min-height: 64px;
            letter-spacing: 1.5px !important;
        }
    }
    </style>
    """,
    # HTML과 CSS 문자열을 실제 웹 페이지 디자인으로 적용합니다.
    unsafe_allow_html=True,
)

# =========================================================
# 3. 상단 시스템 헤더
# =========================================================

# datetime.now()로 현재 날짜와 시간을 가져옵니다.
# strftime("%Y.%m.%d")는 날짜를 연도.월.일 형식의 문자열로 바꿉니다.
# 예를 들어 2026년 11월 9일이면 "2026.11.09"가 됩니다.
current_time = datetime.now().strftime("%Y.%m.%d")

# 상단에 프로젝트 이름, 시스템 상태, 이용 모드를 표시합니다.
st.markdown(
    """
    <div class="system-header">
        <div>
            <!-- CELL VISION 로고에 .brand 디자인을 적용합니다. -->
            <span class="brand">
                <!-- 로고 앞의 기호에는 별도의 색상 디자인을 적용합니다. -->
                <span class="brand-symbol">⬡</span>CELL VISION
            </span>

            <!-- 로고 옆에 부대 이름을 표시합니다. -->
            <span class="brand-sub">
                BIOLOGICAL OPERATIONS UNIT
            </span>
        </div>

        <!-- 시스템 상태와 교육용 접근 모드를 오른쪽에 표시합니다. -->
        <div class="system-status">
            SYSTEM / <span class="online">ONLINE ●</span>
            &nbsp;&nbsp; | &nbsp;&nbsp;
            ACCESS MODE / EDUCATIONAL
        </div>
    </div>
    """,
    # HTML 태그를 단순한 글자가 아닌 실제 화면 요소로 표시합니다.
    unsafe_allow_html=True,
)

# =========================================================
# 4. 작전 브리핑 메인 화면
# =========================================================

# 작전 소개, 현재 상태, 임무 목표를 하나의 큰 브리핑 화면으로 표시합니다.
st.markdown(
    """
    <!-- 작전 브리핑 전체를 감싸는 큰 상자입니다. -->
    <div class="briefing-frame">

        <!-- 상단에 미션 번호와 기밀 분류 문구를 표시합니다. -->
        <div class="briefing-topline">
            <span>MISSION BRIEFING // 001</span>
            <span class="mission-index">CELL VISION / CLASSIFIED</span>
        </div>

        <!-- 가장 큰 제목을 표시합니다. -->
        <div class="hero-title">CELL VISION</div>

        <!-- 제목 아래에 부대 이름을 표시합니다. -->
        <div class="hero-subtitle">
            BIOLOGICAL OPERATIONS UNIT
        </div>

        <!-- 한국어 소개 문구를 표시합니다. -->
        <div class="hero-tagline">
            세포의 비밀을 탐색하는, 당신의 미션이 시작됩니다.
        </div>

        <!-- 위쪽 내용과 아래쪽 내용을 구분하는 가로선입니다. -->
        <div class="cyan-divider"></div>

        <!-- 작전 상태를 담는 상자입니다. -->
        <div class="status-panel">
            <div class="status-label">
                OPERATION STATUS / MISSION CONTROL
            </div>

            <!-- br은 줄바꿈을 의미합니다. -->
            <!-- &nbsp;는 공백, &amp;는 & 기호를 나타내는 HTML 표기입니다. -->
            <div class="status-value">
                TARGET &nbsp;&nbsp;&nbsp; / CELLULAR SYSTEM<br>
                OBJECTIVE / ANALYZE &amp; UNDERSTAND<br>
                STATUS &nbsp;&nbsp;&nbsp; / <span class="online">READY</span>
            </div>
        </div>

        <!-- 작전 개요 구역의 제목입니다. -->
        <div class="section-label">// 작전 개요</div>

        <!-- 대원에게 임무를 소개하는 주요 문구입니다. -->
        <div class="welcome-title">
            대원, 환영한다.<br>
            당신은 지금 세포 내부로 향하는 특별한 작전에 투입되었다.
        </div>

        <!-- 임무의 목적과 수행 방법을 설명합니다. -->
        <div class="briefing-text">
            이 임무의 목표는 세포를 구성하는 핵심 소기관들을 탐색하고,<br>
            각 구조의 기능과 상호작용을 분석하는 것이다.<br>
            제공된 분석 자료를 활용해 세포 시스템의 작동 원리를 파악하라.
        </div>

        <!-- 작전 설명 마지막에 강조 문구를 표시합니다. -->
        <div class="final-directive">
            지금부터, 세포의 세계로 들어가자.
        </div>

        <!-- 작전 설명과 임무 목표 사이에 구분선을 추가합니다. -->
        <div class="cyan-divider"></div>

        <!-- 임무 목표 구역의 제목입니다. -->
        <div class="section-label">// OPERATION OBJECTIVES</div>

        <!-- 세 가지 임무 목표를 하나의 상자 안에 배치합니다. -->
        <div class="objectives-panel">

            <!-- 첫 번째 임무 목표입니다. -->
            <div class="objective">
                <div class="objective-number">01</div>
                <div>
                    <div class="objective-title">세포 내부 구조 탐색</div>
                    <div class="objective-description">
                        9개의 소기관을 식별하고 각 구조의 특징을 파악할 것
                    </div>
                </div>
            </div>

            <!-- 두 번째 임무 목표입니다. -->
            <div class="objective">
                <div class="objective-number">02</div>
                <div>
                    <div class="objective-title">소기관별 기능 분석</div>
                    <div class="objective-description">
                        각 소기관의 역할과 작동 원리를 이해할 것
                    </div>
                </div>
            </div>

            <!-- 세 번째 임무 목표입니다. -->
            <div class="objective">
                <div class="objective-number">03</div>
                <div>
                    <div class="objective-title">세포 시스템 이해 완성</div>
                    <div class="objective-description">
                        소기관 사이의 연결 관계와 물질 이동을 분석할 것
                    </div>
                </div>
            </div>

        </div>

    </div>
    """,
    # HTML 태그를 실제 화면에 적용해 브리핑 화면을 만듭니다.
    unsafe_allow_html=True,
)

# =========================================================
# 5. START MISSION 버튼
# =========================================================

# st.write("")는 빈 내용을 출력합니다.
# 여기서는 두 번 사용해 브리핑 화면과 시작 버튼 사이에 세로 여백을 만듭니다.
st.write("")
st.write("")

# st.columns()는 화면을 여러 개의 세로 열로 나누는 기능입니다.
# [1, 2, 1]은 왼쪽, 가운데, 오른쪽 열의 너비 비율입니다.
# 가운데 열이 양쪽 열보다 두 배 넓게 만들어집니다.
button_col_left, button_col_center, button_col_right = st.columns(
    [1, 2, 1]
)

# with는 아래에 작성한 코드가 어느 영역에서 실행될지 지정합니다.
# 이 경우 버튼과 안내 문구를 가운데 열에 표시합니다.
with button_col_center:

    # st.button()으로 사용자가 클릭할 수 있는 버튼을 만듭니다.
    # 버튼을 누르면 True, 누르지 않으면 False가 반환됩니다.
    # 반환된 값은 start_mission 변수에 저장됩니다.
    start_mission = st.button(
        ">>>  START MISSION  <<<",  # 버튼에 표시할 문구
        use_container_width=True,   # 버튼이 가운데 열의 너비를 모두 사용하도록 설정
        type="primary",             # 주요 버튼 스타일을 적용
    )

    # 버튼 아래에 시스템 시작을 안내하는 문구를 표시합니다.
    # 두 문자열은 이어져 하나의 HTML 문구가 됩니다.
    st.markdown(
        '<div class="button-caption">'
        'INITIALIZE SYSTEM // ENTER CELLULAR ANALYSIS'
        '</div>',
        unsafe_allow_html=True,
    )

# if는 조건문입니다.
# start_mission이 True, 즉 버튼을 눌렀을 때만 아래 코드를 실행합니다.
if start_mission:

    # Streamlit의 페이지 이동 기능을 사용해 app.py로 이동합니다.
    # app.py가 프로젝트의 등록된 페이지여야 정상적으로 이동할 수 있습니다.
    st.switch_page("app.py")

# =========================================================
# 6. 하단 시스템 정보
# =========================================================

# 페이지 맨 아래에 프로젝트 이름과 현재 날짜를 표시합니다.
st.markdown(
    # f"""는 f-string이라는 문자열 작성 방식입니다.
    # {current_time} 부분에 위에서 저장한 현재 날짜가 들어갑니다.
    f"""
    <div class="system-footer">

        <!-- 왼쪽에 프로젝트 이름과 관련 문구를 표시합니다. -->
        <div>
            <span class="footer-highlight">CELL VISION</span>
            &nbsp; / BIOLOGICAL OPERATIONS UNIT<br>
            EXPLORE · ANALYZE · UNDERSTAND · SAVE LIFE
        </div>

        <!-- 오른쪽에 준비 상태와 현재 날짜를 표시합니다. -->
        <div>
            MISSION READY &nbsp; / &nbsp; {current_time}
        </div>

    </div>
    """,
    # HTML 태그와 CSS 디자인을 실제 화면에 적용합니다.
    unsafe_allow_html=True,
)
