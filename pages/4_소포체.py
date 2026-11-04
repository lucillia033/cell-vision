
import streamlit as st
from pathlib import Path

# 페이지 제목, 화면 레이아웃, 사이드바의 초기 표시 상태를 설정합니다.
st.set_page_config(page_title="CELL VISION | Endoplasmic Reticulum", layout="wide", initial_sidebar_state="expanded")

# 현재 파일의 상위 폴더를 기준으로 소포체 이미지의 경로를 설정합니다.
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "er.png"

# CSS를 사용해 페이지의 배경, 글꼴, 색상, 버튼과 정보 패널의 디자인을 설정합니다.
# 다른 소기관 페이지와 통일된 CELL VISION의 전술 분석실 디자인을 유지합니다.
st.markdown("""
<style>
/* 외부 글꼴과 페이지 전체의 기본 배경 및 글자 스타일 */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');
.stApp {background:radial-gradient(ellipse at top,#102433 0%,#050b12 58%);color:#dceaf0;font-family:'Noto Sans KR',sans-serif}

/* 사이드바와 상단 헤더의 배경 및 경계선 */
[data-testid="stSidebar"] {background:#07111b;border-right:1px solid #244454}
[data-testid="stHeader"] {background:#050b12}

/* 본문 영역의 최대 너비와 위아래 여백 */
.block-container {max-width:1800px;padding-top:1.2rem;padding-bottom:3rem}

/* 제목, 문단, 목록 및 입력 요소의 기본 글자색 */
h1,h2,h3,p,li,label {color:#dceaf0}
h1 {font-family:'IBM Plex Mono',monospace!important;letter-spacing:1px}
.stCaption,[data-testid="stCaptionContainer"] {color:#7993a3!important}

/* 버튼의 기본 상태와 마우스를 올렸을 때의 디자인 */
.stButton>button {background:#0b1c29;color:#dceaf0;border:1px solid #315568;border-radius:2px}
.stButton>button:hover {background:#123044;color:#57d9e8;border-color:#57d9e8}

/* Streamlit 기본 페이지 탐색 메뉴를 숨깁니다. */
[data-testid="stSidebarNav"] {display:none}

/* 사이드바 브랜드 영역의 제목과 부제목 */
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

/* 상단의 작은 영문 분류 문구 */
.eyebrow {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:11px;letter-spacing:2px;margin-bottom:7px}

/* 소포체의 핵심 정보를 표시하는 개요 패널 */
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

# 사이드바에 프로젝트 브랜드, 메인 화면 링크, 소기관별 페이지 목록을 배치합니다.
with st.sidebar:
    # 프로젝트 브랜드와 첫 번째 메뉴 구분 영역을 표시합니다.
    st.markdown("""<div class="side-brand"><div class="side-brand-title">CELL VISION</div><div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div></div><div class="side-section">01 / COMMAND MENU</div>""", unsafe_allow_html=True)

    # 메인 화면 이동 메뉴와 현재 화면 안내 문구를 표시합니다.
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")
    st.page_link("app.py", label="메인 화면")

    # 소기관별 분석 페이지 목록의 구분 제목을 표시합니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)

    # 소기관 이름과 실제 파이썬 파일 경로를 연결해 페이지 목록을 구성합니다.
    pages = [("BIO-01 / 핵","pages/1_핵.py"),("BIO-02 / 리보솜","pages/2_리보솜.py"),("BIO-03 / 미토콘드리아","pages/3_미토콘드리아.py"),("BIO-04 / 소포체","pages/4_소포체.py"),("BIO-05 / 골지체","pages/5_골지체.py"),("BIO-06 / 리소좀","pages/6_리소좀.py"),("BIO-07 / 세포막","pages/7_세포막.py"),("BIO-08 / 세포질","pages/8_세포질.py"),("BIO-09 / 세포골격","pages/9_세포골격.py")]

    # 각 페이지의 이름과 경로를 하나씩 꺼내 사이드바 이동 링크를 생성합니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 사이드바 하단에 시스템 상태와 데이터베이스 정보를 표시합니다.
    st.markdown("""<div class="side-section">03 / SYSTEM MONITOR</div><div class="side-info">SYSTEM STATUS · ONLINE<br>DATABASE · LOCAL FILES<br>SECURITY LEVEL · BIO-RESTRICTED<br>ACCESS MODE · EDUCATIONAL</div><br><hr><div class="side-info">CELL VISION / INTERNAL USE</div>""", unsafe_allow_html=True)

# 현재 페이지의 시스템 분류, 상태, 파일 번호를 상단에 표시합니다.
st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-04</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)

# 페이지 제목과 소포체의 핵심 기능을 안내합니다.
st.title("소포체 | ENDOPLASMIC RETICULUM")
st.caption("BIO-04 · 단백질과 지질의 합성 및 세포 내 물질 수송")

# 버튼을 클릭하면 메인 화면으로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 제목 영역과 본문을 구분하는 선을 표시합니다.
st.divider()

# 화면을 두 열로 나누어 왼쪽에는 이미지, 오른쪽에는 개요를 배치합니다.
# 열의 비율을 조절해 오른쪽 설명 영역을 더 넓게 설정합니다.
left, right = st.columns([1, 1.6], gap="large")

with left:
    # 이미지 파일이 존재하면 표시하고, 없으면 경고 메시지를 출력합니다.
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/er.png")

with right:
    # 소포체의 구조와 주요 기능을 개요 패널에 표시합니다.
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>소포체는 막으로 이루어진 관 모양과 납작한 주머니 모양의 구조가 연결된 세포소기관이다. 거친면 소포체는 주로 단백질의 합성과 가공에 관여하고, 매끈면 소포체는 지질 합성과 해독, 칼슘 이온 저장 등에 관여한다.</div>""", unsafe_allow_html=True)

# 소포체의 구조, 주요 기능, 작동 원리와 다른 소기관과의 관계를 출력합니다.
# HTML의 h2는 주요 항목, h3는 세부 항목, p는 생물학 설명 문단을 나타냅니다.
st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>거친면 소포체</h3>
<p>거친면 소포체의 바깥쪽 표면에는 리보솜이 붙어 있어 거칠게 보인다. 이곳의 리보솜은 분비 단백질과 막 단백질 등 세포 내 특정 경로로 보내질 단백질의 합성에 관여한다.</p>
<h3>매끈면 소포체</h3>
<p>매끈면 소포체에는 표면에 리보솜이 붙어 있지 않다. 지질과 인지질의 합성, 일부 물질의 해독, 칼슘 이온의 저장과 방출 등에 관여한다.</p>
<h3>소포체 내강</h3>
<p>소포체 내강은 소포체 막으로 둘러싸인 내부 공간이다. 새로 합성된 단백질이 접히고 변형되며, 단백질이 올바른 구조를 갖도록 품질 관리가 이루어진다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>단백질 합성과 가공</h3>
<p>거친면 소포체에 결합한 리보솜은 단백질을 합성하며, 합성 중인 단백질은 소포체 내강으로 들어가거나 막에 삽입된다. 소포체는 단백질의 접힘과 초기 가공을 돕고 제대로 접히지 않은 단백질을 관리한다.</p>
<h3>지질 합성</h3>
<p>매끈면 소포체는 인지질과 여러 지질의 합성에 관여한다. 이렇게 만들어진 지질은 세포막과 여러 세포소기관의 막을 구성하는 데 이용된다.</p>
<h3>해독과 칼슘 저장</h3>
<p>일부 세포의 매끈면 소포체는 약물이나 유해 물질의 해독에 관여한다. 또한 칼슘 이온을 저장했다가 필요한 상황에 방출하여 세포의 신호 전달과 근육 수축 등 여러 과정에 영향을 준다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>단백질의 합성과 이동</h3>
<p>단백질을 만드는 리보솜은 합성되는 단백질의 특성에 따라 소포체와 연결될 수 있다. 단백질은 소포체 내강으로 들어가거나 막에 삽입되고, 접힘과 가공을 거친 뒤 운반 소낭에 실려 다음 장소로 이동한다.</p>
<h3>소낭을 통한 수송</h3>
<p>소포체에서 출발한 운반 소낭은 세포 내 막성 구조 사이에서 물질을 운반한다. 소낭은 골지체와 융합해 단백질과 지질을 전달하며, 이후 물질은 추가 가공이나 분류를 거친다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포소기관과의 관계</h2>
<h3>핵</h3>
<p>핵막의 바깥막은 소포체와 연결되어 있다. 핵의 유전 정보에 따라 만들어진 mRNA는 리보솜에서 번역되고, 특정 단백질은 소포체를 통해 이동한다.</p>
<h3>리보솜</h3>
<p>거친면 소포체 표면의 리보솜은 분비 단백질과 막 단백질 등을 합성한다. 단백질이 합성되는 동안 소포체 내부로 들어가거나 막에 삽입될 수 있다.</p>
<h3>골지체</h3>
<p>소포체에서 합성되고 초기 가공된 단백질과 지질은 운반 소낭을 통해 골지체로 이동한다. 골지체는 이를 추가로 가공하고 분류한다.</p>
</div>
""", unsafe_allow_html=True)
