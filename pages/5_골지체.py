
import streamlit as st
from pathlib import Path

# 페이지 제목, 화면 너비, 사이드바의 초기 표시 상태를 설정합니다.
st.set_page_config(page_title="CELL VISION | Golgi Apparatus", layout="wide", initial_sidebar_state="expanded")

# 현재 파일의 상위 폴더를 기준으로 프로젝트 루트와 골지체 이미지 경로를 설정합니다.
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "golgi.png"

# CSS를 이용해 페이지의 배경, 글꼴, 색상, 버튼 및 정보 패널 디자인을 설정합니다.
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

/* 골지체의 핵심 정보를 표시하는 개요 패널 */
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

# 사이드바에 프로젝트 브랜드, 메인 화면 이동 링크, 소기관별 탐색 메뉴를 배치합니다.
with st.sidebar:
    # 프로젝트 브랜드와 첫 번째 메뉴 구분 영역을 표시합니다.
    st.markdown("""<div class="side-brand"><div class="side-brand-title">CELL VISION</div><div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div></div><div class="side-section">01 / COMMAND MENU</div>""", unsafe_allow_html=True)

    # 메인 화면 이동 링크와 현재 메뉴의 안내 문구를 표시합니다.
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")
    st.page_link("app.py", label="메인 화면")

    # 소기관별 분석 파일 목록의 구분 제목을 표시합니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)

    # 각 소기관의 화면 이름과 실제 파이썬 파일 경로를 연결합니다.
    pages = [("BIO-01 / 핵","pages/1_핵.py"),("BIO-02 / 리보솜","pages/2_리보솜.py"),("BIO-03 / 미토콘드리아","pages/3_미토콘드리아.py"),("BIO-04 / 소포체","pages/4_소포체.py"),("BIO-05 / 골지체","pages/5_골지체.py"),("BIO-06 / 리소좀","pages/6_리소좀.py"),("BIO-07 / 세포막","pages/7_세포막.py"),("BIO-08 / 세포질","pages/8_세포질.py"),("BIO-09 / 세포골격","pages/9_세포골격.py")]

    # 목록의 페이지 이름과 경로를 하나씩 꺼내 사이드바 링크를 생성합니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 사이드바 하단에 시스템 상태와 데이터베이스 정보를 표시합니다.
    st.markdown("""<div class="side-section">03 / SYSTEM MONITOR</div><div class="side-info">SYSTEM STATUS · ONLINE<br>DATABASE · LOCAL FILES<br>SECURITY LEVEL · BIO-RESTRICTED<br>ACCESS MODE · EDUCATIONAL</div><br><hr><div class="side-info">CELL VISION / INTERNAL USE</div>""", unsafe_allow_html=True)

# 현재 페이지의 시스템 분류, 온라인 상태, 파일 번호를 상단에 표시합니다.
st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-05</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)

# 페이지 제목과 골지체의 주요 기능을 안내합니다.
st.title("골지체 | GOLGI APPARATUS")
st.caption("BIO-05 · 단백질과 지질의 가공, 분류 및 운반")

# 버튼을 클릭하면 메인 화면으로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 제목 영역과 본문을 구분하는 선을 표시합니다.
st.divider()

# 화면을 두 열로 나누어 왼쪽에는 이미지, 오른쪽에는 개요를 배치합니다.
# 열의 비율을 조정해 설명 영역을 이미지 영역보다 넓게 설정합니다.
left, right = st.columns([1, 1.6], gap="large")

with left:
    # 이미지 파일이 존재하면 표시하고, 없으면 경고 메시지를 출력합니다.
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/golgi.png")

with right:
    # 골지체의 구조와 물질 가공 및 운반 기능을 개요 패널에 표시합니다.
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>골지체는 소포체에서 전달된 단백질과 지질을 추가로 가공하고, 종류와 목적지에 따라 분류하여 운반하는 세포소기관이다. 납작한 막성 주머니인 시스터나가 여러 겹으로 쌓인 구조를 이룬다.</div>""", unsafe_allow_html=True)

# 골지체의 구조, 주요 기능, 작동 과정 및 다른 소기관과의 관계를 출력합니다.
# HTML의 h2는 주요 항목, h3는 세부 항목, p는 설명 문단을 나타냅니다.
st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>시스면</h3>
<p>시스면은 소포체에서 온 운반 소낭이 융합하는 골지체의 유입 쪽이다. 소포체에서 전달된 단백질과 지질이 골지체 안으로 들어오는 첫 단계에 해당한다.</p>
<h3>시스터나</h3>
<p>시스터나는 골지체를 이루는 납작한 막성 주머니이다. 여러 시스터나를 지나면서 단백질과 지질은 다양한 효소의 작용을 받아 단계적으로 가공된다.</p>
<h3>트랜스면</h3>
<p>트랜스면은 가공된 물질이 골지체를 떠나는 출구 쪽이다. 단백질과 지질은 목적지에 따라 분류된 뒤 운반 소낭에 담겨 이동한다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>단백질 가공</h3>
<p>골지체는 단백질의 당화와 같은 화학적 변형을 수행하여 단백질의 기능과 이동 경로에 영향을 준다. 모든 단백질이 동일한 방식으로 가공되는 것은 아니며, 단백질의 종류에 따라 가공 과정이 달라진다.</p>
<h3>분류와 포장</h3>
<p>골지체는 가공된 단백질과 지질을 목적지에 따라 분류하고 운반 소낭에 포장한다. 이 물질들은 세포막, 리소좀, 분비 소낭 등 서로 다른 장소로 전달될 수 있다.</p>
<h3>세포 분비</h3>
<p>세포 밖으로 분비될 물질은 소낭에 실려 세포막으로 이동한다. 소낭이 세포막과 융합하면 내용물이 세포 밖으로 방출되는데, 이를 세포외 배출이라고 한다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>소포체로부터 물질 전달</h3>
<p>소포체에서 가공된 물질은 운반 소낭에 담겨 골지체의 시스면으로 이동한다. 소낭은 골지체 막과 융합하여 내용물을 전달한다.</p>
<h3>단계적 가공과 이동</h3>
<p>물질은 골지체의 여러 시스터나를 지나면서 효소에 의해 가공된다. 가공 과정은 단백질의 종류와 최종 목적지에 따라 달라진다.</p>
<h3>분류와 목적지 전달</h3>
<p>트랜스면에서는 물질이 분류되어 서로 다른 운반 소낭에 포장된다. 소낭은 세포막이나 리소좀 등 목적지로 이동해 물질을 전달한다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포소기관과의 관계</h2>
<h3>소포체</h3>
<p>소포체는 단백질과 지질을 합성하고 초기 가공을 수행한다. 이 물질들은 운반 소낭을 통해 골지체로 전달된다.</p>
<h3>리소좀</h3>
<p>리소좀에서 작용하는 일부 소화 효소는 골지체에서 가공되고 분류된 뒤 리소좀으로 운반된다.</p>
<h3>세포막</h3>
<p>골지체에서 포장된 소낭은 세포막과 융합해 막 성분을 공급하거나 세포 밖으로 물질을 분비한다.</p>
</div>
""", unsafe_allow_html=True)
