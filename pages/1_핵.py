import streamlit as st
from pathlib import Path  # 파일 및 폴더 경로를 운영체제에 맞게 다루기 위한 모듈

# =========================================================
# 1. 기본 설정
# =========================================================

# Streamlit 페이지의 기본 정보를 설정합니다.
st.set_page_config(
    page_title="CELL VISION | Nucleus",  # 브라우저 탭에 표시되는 페이지 제목
    layout="wide",  # 화면을 넓게 사용하는 레이아웃
    initial_sidebar_state="expanded",  # 처음 접속했을 때 사이드바를 펼친 상태로 설정
)

# 현재 실행 중인 파일의 위치를 기준으로 프로젝트의 상위 폴더 경로를 구합니다.
# __file__은 현재 Python 파일의 경로를 의미합니다.
# resolve()는 절대 경로로 변환하고, parent.parent는 두 단계 위의 폴더를 가리킵니다.
ROOT_DIR = Path(__file__).resolve().parent.parent

# 프로젝트 상위 폴더 안의 images 폴더에 있는 핵 이미지의 경로를 지정합니다.
IMAGE_PATH = ROOT_DIR / "images" / "nucleus.png"

# =========================================================
# 2. 전체 페이지 디자인 설정
# =========================================================

# CSS를 사용하여 페이지의 배경, 글꼴, 색상, 버튼, 사이드바 등의 디자인을 설정합니다.
# unsafe_allow_html=True는 HTML과 CSS 코드가 화면에 적용되도록 허용합니다.
st.markdown("""
<style>
/* 웹페이지에서 사용할 외부 글꼴을 가져옵니다. */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

/* 앱 전체의 배경, 글자 색상, 기본 글꼴을 설정합니다. */
.stApp {background:radial-gradient(ellipse at top,#102433 0%,#050b12 58%);color:#dceaf0;font-family:'Noto Sans KR',sans-serif}

/* 왼쪽 사이드바의 배경색과 오른쪽 테두리를 설정합니다. */
[data-testid="stSidebar"] {background:#07111b;border-right:1px solid #244454}

/* Streamlit 상단 헤더의 배경색을 설정합니다. */
[data-testid="stHeader"] {background:#050b12}

/* 메인 콘텐츠 영역의 최대 너비와 위아래 여백을 설정합니다. */
.block-container {max-width:1800px;padding-top:1.2rem;padding-bottom:3rem}

/* 제목, 본문, 목록, 입력 항목 등의 기본 글자 색상을 설정합니다. */
h1,h2,h3,p,li,label {color:#dceaf0}

/* h1 제목에 고정폭 글꼴과 글자 간격을 적용합니다. */
h1 {font-family:'IBM Plex Mono',monospace!important;letter-spacing:1px}

/* 캡션으로 표시되는 보조 설명의 색상을 설정합니다. */
.stCaption, [data-testid="stCaptionContainer"] {color:#7993a3!important}

/* Streamlit 버튼의 기본 배경, 글자, 테두리 디자인을 설정합니다. */
.stButton>button {background:#0b1c29;color:#dceaf0;border:1px solid #315568;border-radius:2px}

/* 버튼에 마우스를 올렸을 때 배경과 글자 색상을 변경합니다. */
.stButton>button:hover {background:#123044;color:#57d9e8;border-color:#57d9e8}

/* Streamlit이 자동으로 생성하는 사이드바 페이지 이동 메뉴를 숨깁니다. */
[data-testid="stSidebarNav"] {display:none}

/* 사이드바의 CELL VISION 로고 영역을 디자인합니다. */
.side-brand {border-top:2px solid #6d95a7;border-bottom:1px solid #284655;padding:13px 6px;background:linear-gradient(110deg,#122533,#07111b);margin-bottom:20px}

/* 사이드바의 CELL VISION 제목 글꼴과 크기를 설정합니다. */
.side-brand-title {font-family:'IBM Plex Mono',monospace;font-size:21px;font-weight:700;letter-spacing:2px;color:#dceaf0}

/* 사이드바의 소속 부제목 디자인입니다. */
.side-brand-sub {font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:1px;color:#57d9e8;margin-top:5px}

/* 사이드바의 메뉴 구역 제목을 디자인합니다. */
.side-section {font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#57d9e8;border-bottom:1px solid #244454;padding-bottom:7px;margin:18px 0 10px}

/* 사이드바의 시스템 상태 정보 글꼴과 색상을 설정합니다. */
.side-info {font-family:'IBM Plex Mono',monospace;font-size:10px;line-height:1.9;color:#7993a3}

/* 사이드바 페이지 이동 링크의 기본 테두리와 여백을 설정합니다. */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {border:1px solid transparent;border-radius:2px;padding:8px 10px}

/* 사이드바 페이지 이동 링크에 마우스를 올렸을 때의 디자인입니다. */
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {background:#0b1c29;border-color:#315568}

/* 사이드바 페이지 이동 링크의 글꼴과 크기를 설정합니다. */
[data-testid="stSidebar"] [data-testid="stPageLink"] p {font-family:'IBM Plex Mono',monospace;font-size:12px}

/* 페이지 상단의 시스템 상태 표시 영역을 디자인합니다. */
.top-strip {display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid #315568;border-bottom:1px solid #244454;padding:9px 0;margin-bottom:25px;font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#7993a3}

/* TACTICAL BIOLOGY INTERFACE 문구의 디자인입니다. */
.eyebrow {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:11px;letter-spacing:2px;margin-bottom:7px}

/* 핵의 핵심 정보를 요약해서 보여주는 영역입니다. */
.overview {background:linear-gradient(110deg,#102533,#091722);border-left:3px solid #57d9e8;padding:18px 22px;line-height:1.9;color:#dceaf0;margin:18px 0;border-top:1px solid #244454;border-bottom:1px solid #244454}

/* 생물학 설명이 들어가는 본문 영역의 줄 간격과 위쪽 여백을 설정합니다. */
.article-section {line-height:1.95;margin-top:28px}

/* 본문 안의 h2 제목을 디자인합니다. */
.article-section h2 {font-family:'IBM Plex Mono','Noto Sans KR',sans-serif;border-bottom:1px solid #315568;padding-bottom:10px;color:#57d9e8!important;font-size:22px;margin-top:30px}

/* 본문 안의 h3 소제목을 디자인합니다. */
.article-section h3 {color:#8bd9b0!important;font-size:17px;margin-top:22px}

/* 본문 안의 문단과 목록 글자 색상을 설정합니다. */
.article-section p,.article-section li {color:#c6d7e0}

/* 핵심 정보 영역의 작은 분류 제목을 디자인합니다. */
.info-label {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:10px;letter-spacing:1px}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 3. 사이드바 구성
# =========================================================

# with st.sidebar를 사용하면 아래에 작성한 요소들이 왼쪽 사이드바에 배치됩니다.
with st.sidebar:

    # 사이드바 상단에 프로젝트 이름과 소속을 표시합니다.
    st.markdown("""
    <div class="side-brand">
      <div class="side-brand-title">CELL VISION</div>
      <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
    </div>
    <div class="side-section">01 / COMMAND MENU</div>
    """, unsafe_allow_html=True)

    # 현재 페이지가 작전 지휘 통제실임을 표시합니다.
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")

    # 메인 화면으로 이동할 수 있는 링크를 생성합니다.
    st.page_link("app.py", label="메인 화면")

    # 소기관별 자료 페이지를 표시할 메뉴 제목입니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)

    # 각 소기관의 페이지 이름과 실제 Python 파일 경로를 리스트로 저장합니다.
    pages = [
        ("BIO-01 / 핵", "pages/1_핵.py"),
        ("BIO-02 / 리보솜", "pages/2_리보솜.py"),
        ("BIO-03 / 미토콘드리아", "pages/3_미토콘드리아.py"),
        ("BIO-04 / 소포체", "pages/4_소포체.py"),
        ("BIO-05 / 골지체", "pages/5_골지체.py"),
        ("BIO-06 / 리소좀", "pages/6_리소좀.py"),
        ("BIO-07 / 세포막", "pages/7_세포막.py"),
        ("BIO-08 / 세포질", "pages/8_세포질.py"),
        ("BIO-09 / 세포골격", "pages/9_세포골격.py"),
    ]

    # 리스트에 저장된 페이지 정보를 하나씩 꺼내 사이드바에 링크를 생성합니다.
    # label에는 화면에 표시할 이름이, path에는 이동할 파일 경로가 들어갑니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 사이드바 하단에 시스템 상태와 보안 정보를 표시합니다.
    st.markdown("""
    <div class="side-section">03 / SYSTEM MONITOR</div>
    <div class="side-info">
    SYSTEM STATUS · ONLINE<br>
    DATABASE · LOCAL FILES<br>
    SECURITY LEVEL · BIO-RESTRICTED<br>
    ACCESS MODE · EDUCATIONAL
    </div>
    <br><hr>
    <div class="side-info">CELL VISION / INTERNAL USE</div>
    """, unsafe_allow_html=True)

# =========================================================
# 4. 페이지 상단 정보 표시
# =========================================================

# 현재 페이지의 시스템 종류, 작동 상태, 자료 번호를 표시합니다.
st.markdown("""
<div class="top-strip">
<span>SYSTEM / CELLULAR INTELLIGENCE</span>
<span>STATUS / ONLINE</span>
<span>FILE / BIO-01</span>
</div>
<div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>
""", unsafe_allow_html=True)

# 핵 페이지의 메인 제목을 표시합니다.
st.title("핵 | NUCLEUS")

# 핵의 주요 역할을 한 줄로 요약한 설명을 표시합니다.
st.caption("BIO-01 · 유전 정보의 보관과 세포 활동 조절")

# =========================================================
# 5. 메인 화면 이동 버튼
# =========================================================

# 사용자가 버튼을 누르면 메인 페이지(app.py)로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 화면에 구분선을 표시합니다.
st.divider()

# =========================================================
# 6. 핵 이미지와 핵심 정보 배치
# =========================================================

# 화면을 왼쪽과 오른쪽 두 열로 나눕니다.
# [1, 1.6]은 오른쪽 열이 왼쪽 열보다 1.6배 넓다는 의미입니다.
# gap="large"는 두 열 사이의 간격을 넓게 설정합니다.
left, right = st.columns([1, 1.6], gap="large")

# 왼쪽 열에는 핵 이미지를 표시합니다.
with left:

    # IMAGE_PATH에 지정된 위치에 이미지 파일이 실제로 존재하는지 확인합니다.
    if IMAGE_PATH.exists():

        # 이미지 파일이 존재하면 화면 너비에 맞춰 표시합니다.
        st.image(str(IMAGE_PATH), use_container_width=True)

    else:

        # 이미지 파일이 없으면 오류 안내 문구를 표시합니다.
        st.warning("이미지를 찾을 수 없습니다: images/nucleus.png")

# 오른쪽 열에는 핵의 핵심 정보를 표시합니다.
with right:

    # 핵의 핵심 역할을 요약한 설명 상자를 HTML로 구성합니다.
    st.markdown("""
    <div class="overview">
    <div class="info-label">CORE INTELLIGENCE</div>
    핵은 DNA를 보관하고 유전자 발현을 조절하여 세포의 구조와 기능을 통제하는 세포소기관이다.
    핵에서 전사된 유전 정보는 RNA 형태로 전달되며, 이를 바탕으로 필요한 단백질이 합성된다.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 7. 핵의 구조와 기능에 관한 상세 설명
# =========================================================

# 핵의 구조, 주요 기능, 작동 원리, 다른 소기관과의 관계를 설명합니다.
# HTML의 h2는 큰 제목, h3는 소제목, p는 문단, li는 목록 항목을 의미합니다.
st.markdown("""
<div class="article-section">

<!-- 핵의 주요 구조를 설명하는 부분입니다. -->
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>

<h3>핵막</h3>
<p>핵막은 핵을 세포질과 구분하는 이중막 구조이다. 핵 내부의 유전 물질을 보호하고 핵과 세포질 사이의 물질 이동을 조절한다.</p>

<h3>핵공</h3>
<p>핵공은 핵막에 존재하는 통로이다. RNA와 단백질 등 여러 물질이 핵과 세포질 사이를 오갈 수 있도록 선택적으로 조절한다.</p>

<h3>염색질</h3>
<p>염색질은 DNA와 단백질이 결합한 물질이다. 세포가 분열할 때에는 염색체 형태로 응축되며, DNA에 저장된 유전 정보는 세포의 특성과 기능을 결정하는 데 관여한다.</p>

<h3>인</h3>
<p>인은 리보솜을 구성하는 rRNA가 합성되고 리보솜 소단위체가 조립되는 장소이다.</p>

<!-- 핵이 수행하는 주요 기능을 설명하는 부분입니다. -->
<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<ul>
<li><b>유전 정보 보관:</b> DNA를 보관하여 세포의 유전 정보를 유지한다.</li>
<li><b>유전자 발현 조절:</b> 어떤 유전자가 언제 발현될지 조절하는 데 관여한다.</li>
<li><b>유전 정보 전달:</b> 세포 분열 과정에서 DNA가 복제되고 딸세포에 전달되도록 한다.</li>
</ul>

<!-- DNA의 유전 정보가 단백질 합성으로 이어지는 과정을 설명합니다. -->
<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<p>단백질 합성에 필요한 유전 정보는 DNA의 특정 부분을 주형으로 RNA를 합성하는 전사 과정을 통해 전달된다. 생성된 mRNA는 핵공을 통해 세포질로 이동하고, 리보솜에서 번역되어 단백질 합성에 이용된다.</p>

<!-- 핵과 다른 세포소기관 사이의 연결 관계를 설명합니다. -->
<h2>04 / SYSTEM CONNECTIONS · 다른 소기관과의 관계</h2>
<ul>
<li><b>리보솜:</b> 핵의 인에서 리보솜 소단위체가 만들어진다.</li>
<li><b>소포체:</b> 핵막의 바깥막은 거친면 소포체와 연결되어 있다.</li>
<li><b>골지체:</b> 핵의 유전 정보에 따라 합성된 단백질 중 일부는 소포체와 골지체를 거쳐 이동한다.</li>
</ul>
</div>
""", unsafe_allow_html=True)
