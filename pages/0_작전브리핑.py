import streamlit as st

# =========================================================
# 1. 기본 설정
# =========================================================

# Streamlit 페이지의 제목, 화면 배치, 사이드바의 초기 상태를 설정합니다.
st.set_page_config(
    page_title="TASK FORCE BIO | Operation Cell Vision",  # 브라우저 탭에 표시될 페이지 제목
    layout="wide",  # 화면을 넓게 사용하는 레이아웃 설정
    initial_sidebar_state="collapsed",  # 처음 접속했을 때 사이드바를 접힌 상태로 설정
)

# =========================================================
# 2. 작전 브리핑 디자인
# =========================================================

# st.html()을 사용해 HTML과 CSS를 Streamlit 페이지에 적용합니다.
# CSS는 웹페이지의 색상, 글꼴, 크기, 배치 등 디자인을 담당합니다.
st.html("""
<style>
/* 외부 웹 폰트를 가져옵니다. */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;900&display=swap');

/* :root는 CSS 전체에서 사용할 색상 변수를 정의하는 영역입니다. */
:root {
    --bg: #040910;       /* 기본 배경색 */
    --panel: #091521;    /* 패널 배경색 */
    --line: #294554;     /* 테두리 색상 */
    --cyan: #57d9e8;     /* 청록색 강조 색상 */
    --white: #edf8fc;    /* 기본 글자 색상 */
    --muted: #8ca5b4;    /* 보조 글자 색상 */
    --red: #e36b72;      /* 경고 및 보안 표시 색상 */
}

/* HTML 문서와 Streamlit 내부 요소에 기본 글꼴을 적용합니다. */
html, body, [class*="css"] {
    font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
}

/* Streamlit 앱 전체의 배경과 글자 색상을 설정합니다. */
.stApp {
    background:
        /* 오른쪽 위에 청록색 계열의 은은한 빛을 추가합니다. */
        radial-gradient(ellipse at 76% 12%, rgba(20,76,100,.24), transparent 38%),
        /* 왼쪽 아래에도 어두운 청색 계열의 빛을 추가합니다. */
        radial-gradient(ellipse at 8% 90%, rgba(13,47,67,.24), transparent 40%),
        /* 전체 배경에 어두운 남색 그라데이션을 적용합니다. */
        linear-gradient(135deg, #040910 0%, #07111b 55%, #040910 100%);
    color: var(--white);
}

/* Streamlit의 메인 화면 영역을 투명하게 만들어 배경이 보이도록 합니다. */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

/* Streamlit 상단 헤더의 배경을 투명하게 설정합니다. */
[data-testid="stHeader"] {
    background: transparent;
}

/* 왼쪽 사이드바의 배경색과 오른쪽 테두리를 설정합니다. */
[data-testid="stSidebar"] {
    background: #07111b;
    border-right: 1px solid var(--line);
}

/* Streamlit이 자동으로 생성하는 페이지 이동 메뉴를 숨깁니다. */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* 메인 콘텐츠 영역의 최대 너비와 여백을 설정합니다. */
.block-container {
    max-width: 100% !important;
    width: 100% !important;
    padding: 1.2rem 4vw 2rem 4vw !important;
}

/* 페이지 맨 위의 보안 상태 표시 영역입니다. */
.top-strip {
    display: flex;                  /* 내부 요소를 가로 방향으로 배치합니다. */
    justify-content: space-between; /* 요소 사이의 간격을 균등하게 배분합니다. */
    align-items: center;            /* 요소를 세로 가운데에 정렬합니다. */
    flex-wrap: wrap;                /* 화면이 좁아지면 다음 줄로 이동시킵니다. */
    gap: 12px;                      /* 요소 사이의 간격입니다. */
    width: 100%;
    box-sizing: border-box;         /* 여백과 테두리를 너비 계산에 포함합니다. */
    padding: 12px 18px;             /* 내부 여백입니다. */
    border-top: 2px solid #7897a8;  /* 위쪽 테두리를 설정합니다. */
    border-bottom: 1px solid var(--line); /* 아래쪽 테두리를 설정합니다. */
    background: linear-gradient(90deg, #132431, #07111b 75%);
    color: #9cb7c4;
    font-size: 10px;
    letter-spacing: 1.5px;          /* 글자 사이의 간격을 넓힙니다. */
}

/* 상단 상태 표시 영역에서 strong 태그로 강조한 글자의 색상입니다. */
.top-strip strong {
    color: var(--cyan);
}

/* MISSION BRIEFING 위에 표시되는 분류 문구의 디자인입니다. */
.briefing-label {
    color: #43B9FF;
    font-size: 12px;
    letter-spacing: 4px;
    font-weight: 700;   /* 글자를 굵게 표시합니다. */
    margin-top: 30px;   /* 위쪽 바깥 여백입니다. */
    margin-bottom: 14px;
}

/* MISSION BRIEFING 제목의 디자인입니다. */
.briefing-title {
    color: #F1F5F9;
    font-size: clamp(38px, 6vw, 66px); /* 화면 크기에 따라 글자 크기를 조절합니다. */
    line-height: 1.1;                 /* 줄 사이의 간격을 설정합니다. */
    font-weight: 900;
    letter-spacing: -2px;
    margin-bottom: 12px;
}

/* OPERATION CELL VISION 부제목의 디자인입니다. */
.briefing-subtitle {
    color: #43B9FF;
    font-size: 17px;
    letter-spacing: 2px;
    margin-bottom: 24px;
}

/* 메인 작전 브리핑을 감싸는 큰 영역입니다. */
.hero {
    position: relative; /* 내부 요소의 위치를 기준으로 삼습니다. */
    overflow: hidden;   /* 영역 밖으로 나가는 내용을 숨깁니다. */
    width: 100%;
    box-sizing: border-box;
    padding: clamp(28px, 5vw, 70px); /* 화면 크기에 따라 내부 여백을 조절합니다. */
    margin-top: 22px;
    border: 1px solid #2d5063;
    border-top: 3px solid var(--cyan); /* 위쪽에 강조 테두리를 추가합니다. */
    background: linear-gradient(
        110deg,
        rgba(7,18,29,.98) 0%,
        rgba(9,27,41,.95) 57%,
        rgba(7,17,27,.97) 100%
    );
}

/* hero 영역 오른쪽에 사선 무늬를 추가하는 가상 요소입니다. */
.hero::before {
    content: ""; /* 가상 요소를 생성하기 위한 속성입니다. */
    position: absolute;
    top: 0;
    right: 0;
    width: 32%;
    height: 100%;
    /* 반복되는 사선 무늬를 배경으로 만듭니다. */
    background: repeating-linear-gradient(
        135deg,
        transparent 0px,
        transparent 17px,
        rgba(87,217,232,.035) 18px,
        rgba(87,217,232,.035) 19px
    );
    pointer-events: none; /* 장식 영역이 마우스 입력을 방해하지 않도록 합니다. */
}

/* hero 내부의 실제 콘텐츠를 장식 요소보다 앞에 표시합니다. */
.hero-inner {
    position: relative;
    z-index: 1; /* 요소가 겹칠 때 표시되는 앞뒤 순서를 지정합니다. */
}

/* CLASSIFIED 보안 표시 문구의 디자인입니다. */
.classification {
    display: inline-block;
    color: #ff9da2;
    border: 1px solid rgba(227,107,114,.55);
    background: rgba(112,28,38,.17);
    padding: 8px 12px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 26px;
}

/* TASK FORCE BIO 문구의 디자인입니다. */
.hero-kicker {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

/* OPERATION CELL VISION 메인 제목의 디자인입니다. */
.hero-title {
    color: var(--white);
    font-family: 'IBM Plex Mono', monospace;
    font-size: clamp(40px, 7vw, 88px); /* 화면 크기에 따라 제목 크기를 조절합니다. */
    font-weight: 700;
    line-height: .98;
    letter-spacing: -2px;
    margin: 0;
    overflow-wrap: anywhere; /* 긴 단어가 화면 밖으로 나가지 않도록 줄바꿈합니다. */
}

/* 메인 제목 안의 span 태그에 별도의 강조 색상을 적용합니다. */
.hero-title span {
    color: var(--cyan);
}

/* 메인 제목 아래에 표시되는 부제목의 디자인입니다. */
.hero-subtitle {
    color: #9ab3c2;
    font-size: clamp(12px, 1.5vw, 16px);
    letter-spacing: 2px;
    margin-top: 22px;
}

/* 제목과 설명 사이를 구분하는 가로 선입니다. */
.hero-rule {
    width: 100%;
    height: 1px;
    margin: 30px 0;
    background: linear-gradient(90deg, var(--cyan), #294554 65%, transparent);
}

/* 작전의 주요 내용을 표시하는 본문 영역입니다. */
.briefing-copy {
    max-width: 1050px;
    color: #d0dfe7;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: clamp(14px, 1.35vw, 17px);
    line-height: 2.05; /* 본문 줄 사이의 간격을 넓혀 가독성을 높입니다. */
}

/* 본문에서 strong 태그로 강조한 문장의 색상을 설정합니다. */
.briefing-copy strong {
    color: #ffffff;
}

/* 지휘관의 지시를 표시하는 영역입니다. */
.directive {
    display: grid; /* 내부 요소를 격자 형태로 배치합니다. */
    grid-template-columns: minmax(130px, .7fr) 3fr; /* 왼쪽 제목과 오른쪽 설명의 비율입니다. */
    gap: 20px;
    align-items: start;
    padding: 22px 25px;
    margin-top: 24px;
    background: rgba(10,26,39,.78);
    border: 1px solid var(--line);
    border-left: 4px solid var(--cyan); /* 왼쪽에 청록색 강조선을 추가합니다. */
}

/* 지휘관 지시 영역의 왼쪽 제목 디자인입니다. */
.directive-label {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

/* 지휘관 지시 영역의 본문 디자인입니다. */
.directive-text {
    color: #d0dfe7;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 14px;
    line-height: 1.9;
}

/* 페이지 맨 아래의 상태 표시 영역입니다. */
.bottom-strip {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    padding-top: 16px;
    margin-top: 28px;
    border-top: 1px solid var(--line);
    color: #688696;
    font-size: 9px;
    letter-spacing: 1.3px;
}

/* Streamlit 버튼의 기본 디자인을 변경합니다. */
div[data-testid="stButton"] > button {
    min-height: 54px; /* 버튼의 최소 높이입니다. */
    width: 100%;
    background: linear-gradient(90deg, #116c8e, #1284a0) !important;
    color: #ffffff !important;
    border: 1px solid var(--cyan) !important;
    border-radius: 0 !important; /* 버튼 모서리를 둥글지 않게 설정합니다. */
    font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    transition: .18s ease-in-out; /* 버튼 상태가 바뀔 때 부드럽게 전환합니다. */
}

/* 마우스를 버튼 위에 올렸을 때 적용되는 디자인입니다. */
div[data-testid="stButton"] > button:hover {
    background: #1598b5 !important;
    border-color: #b3f6ff !important;
    box-shadow: 0 0 24px rgba(87,217,232,.17); /* 버튼 주변에 빛나는 효과를 추가합니다. */
    color: #ffffff !important;
}

/* Streamlit의 기본 메뉴와 페이지 하단 정보를 숨깁니다. */
#MainMenu, footer {
    visibility: hidden;
}

/* 화면 너비가 700px 이하일 때 적용되는 모바일 화면용 디자인입니다. */
@media (max-width: 700px) {
    /* 모바일에서는 메인 콘텐츠의 좌우 여백을 줄입니다. */
    .block-container {
        padding: .8rem 4vw 1.5rem !important;
    }

    /* 모바일에서는 브리핑 영역의 내부 여백을 줄입니다. */
    .hero {
        padding: 25px 20px;
    }

    /* 모바일에서는 제목의 글자 간격을 조정합니다. */
    .hero-title {
        letter-spacing: -1px;
    }

    /* 모바일에서는 지휘관 지시의 제목과 내용을 세로로 배치합니다. */
    .directive {
        grid-template-columns: 1fr;
        gap: 12px;
    }
}
</style>
""")

# =========================================================
# 3. 상단 보안 상태
# =========================================================

# 작전의 보안 등급, 통신 채널, 현재 상태를 화면에 표시합니다.
# st.html() 안에 작성한 HTML 태그를 이용해 각 문구의 위치와 강조 부분을 지정합니다.
st.html("""
<div class="top-strip">
    <span>TASK FORCE BIO // SPECIAL OPERATIONS</span>
    <span>SECURITY: <strong>RESTRICTED</strong></span>
    <span>CHANNEL: <strong>COMMAND BRIEFING</strong></span>
    <span>STATUS: <strong>AWAITING DEPLOYMENT</strong></span>
</div>

<!-- 브리핑의 보안 분류와 메인 제목을 표시합니다. -->
<div class="briefing-label">CLASSIFIED // PERSONNEL ONLY</div>
<div class="briefing-title">MISSION BRIEFING</div>
<div class="briefing-subtitle">OPERATION CELL VISION</div>
""")

# =========================================================
# 4. 메인 작전 브리핑
# =========================================================

# 작전의 배경, 적의 목표, 대원의 임무 등을 설명하는 메인 콘텐츠입니다.
st.html("""
<div class="hero">
    <div class="hero-inner">

        <!-- 기밀 문서임을 나타내는 보안 표시입니다. -->
        <div class="classification">
            CLASSIFIED // AUTHORIZED PERSONNEL ONLY
        </div>

        <!-- 브리핑의 소속과 문서 종류를 표시합니다. -->
        <div class="hero-kicker">
            TASK FORCE BIO // PERSONNEL BRIEFING
        </div>

        <!-- 작전의 메인 제목입니다. br 태그는 줄바꿈을 의미합니다. -->
        <h1 class="hero-title">
            OPERATION<br>
            <span>CELL VISION</span>
        </h1>

        <!-- 작전의 핵심 문구를 표시합니다. -->
        <div class="hero-subtitle">
            KNOW THE CELL. STOP THE THREAT.
        </div>

        <!-- 제목 영역과 본문을 구분하는 장식용 선입니다. -->
        <div class="hero-rule"></div>

        <!-- 작전의 배경과 수행해야 할 임무를 설명하는 본문입니다. -->
        <div class="briefing-copy">
            대원, 브리핑에 집중해라.<br><br>

            최근 우리 정보부가 적대 세력의 비밀 작전 자료를 확보했다.
            분석 결과, 그들은 세포 내부의 생명 유지 시스템을 장악하고
            전체 기능을 마비시키려는 계획을 추진하고 있다.<br><br>

            적의 표적은 세포를 구성하는 핵심 소기관들이다.
            유전 정보를 관리하는 핵부터 단백질을 합성하는 리보솜,
            에너지를 생산하는 미토콘드리아까지.
            각 소기관은 서로 긴밀하게 연결되어 있다.
            한 부분의 기능이 무너지면 다른 시스템까지 연쇄적으로 영향을 받는다.<br><br>

            우리가 확보한 자료에는 적의 작전 계획을 파악할 수 있는
            중요한 정보가 담겨 있다. 하지만 자료는 아직 완전히 분석되지 않았다.
            소기관의 구조와 기능을 정확히 이해해야만 숨겨진 정보를 해독하고
            적의 다음 행동을 예측할 수 있다.<br><br>

            <strong>네 임무는 명확하다.</strong><br><br>

            먼저 분석실에 진입해 우리가 확보한 기밀 자료를 조사해라.
            세포 소기관의 구조와 기능, 그리고 소기관 사이의 상호작용을 학습해라.
            이 지식은 적의 계획을 분석하기 위한 핵심 정보다.<br><br>

            모든 분석을 마친 뒤 최종 작전에 투입되어라.
            학습한 지식을 활용해 적의 계략을 무너뜨리고
            세포 시스템을 지켜내는 것이 최종 목표다.<br><br>

            <strong>정보 없이 돌입하지 마라.</strong>
            준비되지 않은 채 진입하면 임무는 실패한다.
            충분한 정보를 확보하고, 정확하게 분석하고,
            마지막 순간까지 판단력을 유지해라.<br><br>

            <strong>TASK FORCE BIO는 네 분석 능력을 믿는다.</strong>
        </div>

    </div>
</div>
""")

# =========================================================
# 5. 지휘관의 최종 지시
# =========================================================

# 메인 브리핑 아래에 지휘관의 마지막 지시 사항을 별도 영역으로 표시합니다.
st.html("""
<div class="directive">
    <!-- 지시 사항 영역의 제목입니다. -->
    <div class="directive-label">COMMAND DIRECTIVE</div>

    <!-- 대원이 최종 작전에 들어가기 전에 확인해야 할 지시 내용입니다. -->
    <div class="directive-text">
        적의 이름은 CELL REQUIEM이다.
        그들의 계획을 저지하려면 먼저 우리가 확보한 자료부터 분석해야 한다.
        분석실에서 소기관 정보를 학습하고, 모든 준비를 마친 뒤 최종 작전에 진입해라.
        명심해라, 대원. 정확한 분석 없이는 임무를 완수할 수 없다.
    </div>
</div>
""")

# Streamlit 화면에 빈 줄을 추가해 다음 버튼과의 간격을 만듭니다.
st.write("")
st.write("")

# =========================================================
# 6. 작전 시작
# =========================================================

# 화면을 세 개의 열로 나눕니다.
# [1, 2, 1]은 가운데 열을 양옆 열보다 두 배 넓게 만든다는 의미입니다.
button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

# 가운데 열 안에 작전 개시 버튼을 배치합니다.
with button_col2:

    # 사용자가 버튼을 누르면 아래의 코드가 실행됩니다.
    if st.button(
        "ACKNOWLEDGE BRIEFING  /  작전 개시",
        use_container_width=True,  # 버튼이 열의 너비를 모두 사용하도록 설정합니다.
        type="primary",            # 주요 동작 버튼으로 설정합니다.
    ):
        # 세션 상태에 브리핑 완료 여부를 저장합니다.
        # session_state는 페이지 이동 후에도 유지되는 Streamlit의 상태 저장 공간입니다.
        st.session_state["briefing_completed"] = True

        # 브리핑 페이지에서 메인 페이지(app.py)로 이동합니다.
        st.switch_page("app.py")

# =========================================================
# 7. 하단 상태 표시
# =========================================================

# 브리핑 페이지의 가장 아래에 소속, 작전명, 종료 문구를 표시합니다.
st.html("""
<div class="bottom-strip">
    <span>TASK FORCE BIO // SPECIAL OPERATIONS</span>
    <span>OPERATION CELL VISION</span>
    <span>END OF BRIEFING</span>
</div>
""")
