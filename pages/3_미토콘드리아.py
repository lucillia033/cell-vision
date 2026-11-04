
import streamlit as st
from pathlib import Path

# 페이지 제목과 화면 레이아웃, 사이드바의 초기 표시 상태를 설정합니다.
st.set_page_config(
    page_title="CELL VISION | Mitochondria",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 현재 파일의 상위 폴더를 기준으로 이미지 파일의 경로를 설정합니다.
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "mitochondria.png"

# CSS를 이용해 배경, 글꼴, 색상, 버튼 및 정보 패널의 디자인을 설정합니다.
# 다른 소기관 페이지와 통일된 CELL VISION의 전술 분석실 디자인을 적용합니다.
st.markdown("""
<style>
/* 외부 글꼴과 페이지 전체의 기본 배경 및 글자 스타일 */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');
.stApp {background:radial-gradient(ellipse at top,#102433 0%,#050b12 58%);color:#dceaf0;font-family:'Noto Sans KR',sans-serif}

/* 사이드바와 상단 헤더의 배경색 및 경계선 */
[data-testid="stSidebar"] {background:#07111b;border-right:1px solid #244454}
[data-testid="stHeader"] {background:#050b12}

/* 본문 영역의 최대 너비와 위아래 여백 */
.block-container {max-width:1800px;padding-top:1.2rem;padding-bottom:3rem}

/* 제목, 문단, 목록 및 입력 요소의 기본 글자색 */
h1,h2,h3,p,li,label {color:#dceaf0}
h1 {font-family:'IBM Plex Mono',monospace!important;letter-spacing:1px}
.stCaption,[data-testid="stCaptionContainer"] {color:#7993a3!important}

/* 버튼의 기본 디자인과 마우스를 올렸을 때의 디자인 */
.stButton>button {background:#0b1c29;color:#dceaf0;border:1px solid #315568;border-radius:2px}
.stButton>button:hover {background:#123044;color:#57d9e8;border-color:#57d9e8}

/* Streamlit 기본 페이지 탐색 메뉴를 숨깁니다. */
[data-testid="stSidebarNav"] {display:none}

/* 사이드바 브랜드 영역의 제목과 부제목 디자인 */
.side-brand {border-top:2px solid #6d95a7;border-bottom:1px solid #284655;padding:13px 6px;background:linear-gradient(110deg,#122533,#07111b);margin-bottom:20px}
.side-brand-title {font-family:'IBM Plex Mono',monospace;font-size:21px;font-weight:700;letter-spacing:2px;color:#dceaf0}
.side-brand-sub {font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:1px;color:#57d9e8;margin-top:5px}

/* 사이드바 메뉴 구분 제목과 시스템 정보의 글꼴 및 간격 */
.side-section {font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#57d9e8;border-bottom:1px solid #244454;padding-bottom:7px;margin:18px 0 10px}
.side-info {font-family:'IBM Plex Mono',monospace;font-size:10px;line-height:1.9;color:#7993a3}

/* 사이드바 페이지 이동 링크의 기본 상태와 마우스 반응 */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {border:1px solid transparent;border-radius:2px;padding:8px 10px}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {background:#0b1c29;border-color:#315568}
[data-testid="stSidebar"] [data-testid="stPageLink"] p {font-family:'IBM Plex Mono',monospace;font-size:12px}

/* 페이지 상단의 시스템 상태 표시줄 */
.top-strip {display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid #315568;border-bottom:1px solid #244454;padding:9px 0;margin-bottom:25px;font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#7993a3}

/* 페이지 상단의 작은 영문 분류 문구 */
.eyebrow {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:11px;letter-spacing:2px;margin-bottom:7px}

/* 미토콘드리아의 핵심 정보를 표시하는 개요 패널 */
.overview {background:linear-gradient(110deg,#102533,#091722);border-left:3px solid #57d9e8;padding:18px 22px;line-height:1.9;color:#dceaf0;margin:18px 0;border-top:1px solid #244454;border-bottom:1px solid #244454}

/* 상세 설명 영역의 줄 간격과 제목별 디자인 */
.article-section {line-height:1.95;margin-top:28px}
.article-section h2 {font-family:'IBM Plex Mono','Noto Sans KR',sans-serif;border-bottom:1px solid #315568;padding-bottom:10px;color:#57d9e8!important;font-size:22px;margin-top:30px}
.article-section h3 {color:#8bd9b0!important;font-size:17px;margin-top:22px}
.article-section p,.article-section li {color:#c6d7e0}

/* 개요 패널 내부의 분류 문구 스타일 */
.info-label {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:10px;letter-spacing:1px}
</style>
""", unsafe_allow_html=True)

# 사이드바에 프로젝트 브랜드, 메인 화면 이동 링크, 소기관 목록을 배치합니다.
with st.sidebar:
    # CELL VISION 브랜드와 첫 번째 메뉴 구분 영역을 표시합니다.
    st.markdown("""
    <div class="side-brand">
      <div class="side-brand-title">CELL VISION</div>
      <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
    </div>
    <div class="side-section">01 / COMMAND MENU</div>
    """, unsafe_allow_html=True)

    # 메인 화면으로 이동할 수 있는 링크를 표시합니다.
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")
    st.page_link("app.py", label="메인 화면")

    # 소기관별 분석 파일 목록의 구분 제목을 표시합니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)

    # 각 소기관의 화면 이름과 실제 파이썬 파일 경로를 연결합니다.
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

    # 목록의 페이지 이름과 경로를 하나씩 꺼내 사이드바 링크를 생성합니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 사이드바 하단에 시스템 상태와 데이터베이스 정보를 표시합니다.
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

# 현재 페이지의 시스템 분류, 상태, 파일 번호를 상단에 표시합니다.
st.markdown("""
<div class="top-strip">
<span>SYSTEM / CELLULAR INTELLIGENCE</span>
<span>STATUS / ONLINE</span>
<span>FILE / BIO-03</span>
</div>
<div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>
""", unsafe_allow_html=True)

# 페이지 제목과 미토콘드리아의 핵심 기능을 안내합니다.
st.title("미토콘드리아 | MITOCHONDRIA")
st.caption("BIO-03 · 세포 호흡과 ATP 합성을 담당하는 세포소기관")

# 버튼을 클릭하면 메인 화면으로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 상단 제목 영역과 본문을 구분하는 선을 표시합니다.
st.divider()

# 화면을 두 열로 나누어 왼쪽에는 이미지, 오른쪽에는 개요를 배치합니다.
# 열의 비율을 조절해 오른쪽 설명 영역을 더 넓게 설정합니다.
left, right = st.columns([1, 1.6], gap="large")

with left:
    # 이미지 파일이 존재하면 표시하고, 없으면 경고 메시지를 출력합니다.
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/mitochondria.png")

with right:
    # 미토콘드리아의 구조와 에너지 합성 기능을 개요 패널에 표시합니다.
    st.markdown("""
    <div class="overview">
    <div class="info-label">CORE INTELLIGENCE</div>
    미토콘드리아는 유기물을 분해하는 세포 호흡 과정에서 방출되는 에너지를
    이용해 ATP를 합성하는 세포소기관이다. 이중막 구조를 가지며,
    내막의 주름인 크리스타와 내부 공간인 기질에서 세포 호흡의 여러 과정이 진행된다.
    </div>
    """, unsafe_allow_html=True)

# 미토콘드리아의 구조, 기능, 작동 과정 및 다른 소기관과의 관계를 출력합니다.
# HTML의 h2는 주요 항목, h3는 세부 항목, p는 생물학 설명 문단을 나타냅니다.
st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>외막</h3>
<p>외막은 미토콘드리아의 바깥쪽을 둘러싸는 막으로, 미토콘드리아의 경계를 형성하고 물질의 출입을 조절한다.</p>
<h3>내막과 크리스타</h3>
<p>내막은 외막 안쪽에 위치하며 여러 겹으로 접혀 크리스타를 형성한다. 내막에는 전자 전달계의 단백질 복합체와 ATP 합성 효소가 존재한다. 크리스타는 내막의 표면적을 넓혀 ATP 합성에 필요한 반응이 효율적으로 일어나도록 한다.</p>
<h3>기질</h3>
<p>기질은 내막 안쪽의 공간으로, 여러 효소와 미토콘드리아 DNA, 리보솜 등이 존재한다. 피루브산에서 유래한 물질이 산화되고 시트르산 회로가 진행되는 주요 장소이다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>ATP 합성</h3>
<p>미토콘드리아는 세포 호흡을 통해 ATP를 합성한다. ATP는 세포의 물질 합성, 능동 수송, 운동 등 다양한 생명 활동에 필요한 에너지를 전달한다.</p>
<h3>세포 호흡</h3>
<p>세포 호흡은 유기물에 저장된 에너지를 단계적으로 방출하여 ATP 형태로 전환하는 과정이다. 해당 과정은 세포질에서 시작되며, 미토콘드리아에서는 시트르산 회로와 전자 전달 및 산화적 인산화가 진행된다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>시트르산 회로</h3>
<p>피루브산에서 유래한 아세틸-CoA는 기질에서 시트르산 회로에 들어간다. 이 과정에서 이산화 탄소가 방출되고, 전자 전달에 이용되는 NADH와 FADH₂가 생성된다.</p>
<h3>전자 전달계</h3>
<p>내막에 위치한 전자 전달계는 NADH와 FADH₂로부터 전자를 전달받는다. 전자가 여러 단백질 복합체를 거쳐 이동하는 동안 양성자가 막 사이 공간으로 이동하여 농도 기울기가 형성된다.</p>
<h3>화학 삼투와 ATP 합성</h3>
<p>양성자는 농도 기울기에 따라 ATP 합성 효소를 통과하여 기질 쪽으로 이동한다. 이때 방출되는 에너지를 이용해 ADP와 무기 인산으로부터 ATP가 합성된다. 이 과정을 산화적 인산화라고 한다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포소기관과의 관계</h2>
<h3>세포질</h3>
<p>세포질에서 일어나는 해당 과정은 포도당을 피루브산으로 분해한다. 생성된 물질은 미토콘드리아로 이동하여 세포 호흡의 다음 단계에 이용된다.</p>
<h3>핵</h3>
<p>미토콘드리아의 기능에 필요한 단백질 대부분은 핵의 유전 정보에 따라 합성된 뒤 미토콘드리아로 운반된다. 미토콘드리아는 자체 DNA도 가지고 있지만 모든 단백질을 스스로 만들지는 않는다.</p>
<h3>세포막</h3>
<p>세포막의 수송 단백질은 세포가 영양소와 이온을 받아들이고 내부 환경을 유지하도록 돕는다. 이러한 물질은 세포 호흡과 ATP 사용에 간접적으로 연결된다.</p>
</div>
""", unsafe_allow_html=True)
