
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CELL VISION | Endoplasmic Reticulum", layout="wide", initial_sidebar_state="expanded")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "er.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');
.stApp {background:radial-gradient(ellipse at top,#102433 0%,#050b12 58%);color:#dceaf0;font-family:'Noto Sans KR',sans-serif}
[data-testid="stSidebar"] {background:#07111b;border-right:1px solid #244454}
[data-testid="stHeader"] {background:#050b12}
.block-container {max-width:1800px;padding-top:1.2rem;padding-bottom:3rem}
h1,h2,h3,p,li,label {color:#dceaf0}
h1 {font-family:'IBM Plex Mono',monospace!important;letter-spacing:1px}
.stCaption,[data-testid="stCaptionContainer"] {color:#7993a3!important}
.stButton>button {background:#0b1c29;color:#dceaf0;border:1px solid #315568;border-radius:2px}
.stButton>button:hover {background:#123044;color:#57d9e8;border-color:#57d9e8}
[data-testid="stSidebarNav"] {display:none}
.side-brand {border-top:2px solid #6d95a7;border-bottom:1px solid #284655;padding:13px 6px;background:linear-gradient(110deg,#122533,#07111b);margin-bottom:20px}
.side-brand-title {font-family:'IBM Plex Mono',monospace;font-size:21px;font-weight:700;letter-spacing:2px;color:#dceaf0}
.side-brand-sub {font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:1px;color:#57d9e8;margin-top:5px}
.side-section {font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#57d9e8;border-bottom:1px solid #244454;padding-bottom:7px;margin:18px 0 10px}
.side-info {font-family:'IBM Plex Mono',monospace;font-size:10px;line-height:1.9;color:#7993a3}
[data-testid="stSidebar"] [data-testid="stPageLink"] a {border:1px solid transparent;border-radius:2px;padding:8px 10px}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {background:#0b1c29;border-color:#315568}
[data-testid="stSidebar"] [data-testid="stPageLink"] p {font-family:'IBM Plex Mono',monospace;font-size:12px}
.top-strip {display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid #315568;border-bottom:1px solid #244454;padding:9px 0;margin-bottom:25px;font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:1px;color:#7993a3}
.eyebrow {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:11px;letter-spacing:2px;margin-bottom:7px}
.overview {background:linear-gradient(110deg,#102533,#091722);border-left:3px solid #57d9e8;padding:18px 22px;line-height:1.9;color:#dceaf0;margin:18px 0;border-top:1px solid #244454;border-bottom:1px solid #244454}
.article-section {line-height:1.95;margin-top:28px}
.article-section h2 {font-family:'IBM Plex Mono','Noto Sans KR',sans-serif;border-bottom:1px solid #315568;padding-bottom:10px;color:#57d9e8!important;font-size:22px;margin-top:30px}
.article-section h3 {color:#8bd9b0!important;font-size:17px;margin-top:22px}
.article-section p,.article-section li {color:#c6d7e0}
.info-label {font-family:'IBM Plex Mono',monospace;color:#57d9e8;font-size:10px;letter-spacing:1px}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""<div class="side-brand"><div class="side-brand-title">CELL VISION</div><div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div></div><div class="side-section">01 / COMMAND MENU</div>""", unsafe_allow_html=True)
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")
    st.page_link("app.py", label="메인 화면")
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)
    pages = [("BIO-01 / 핵","pages/1_핵.py"),("BIO-02 / 리보솜","pages/2_리보솜.py"),("BIO-03 / 미토콘드리아","pages/3_미토콘드리아.py"),("BIO-04 / 소포체","pages/4_소포체.py"),("BIO-05 / 골지체","pages/5_골지체.py"),("BIO-06 / 리소좀","pages/6_리소좀.py"),("BIO-07 / 세포막","pages/7_세포막.py"),("BIO-08 / 세포질","pages/8_세포질.py"),("BIO-09 / 세포골격","pages/9_세포골격.py")]
    for label, path in pages:
        st.page_link(path, label=label)
    st.markdown("""<div class="side-section">03 / SYSTEM MONITOR</div><div class="side-info">SYSTEM STATUS · ONLINE<br>DATABASE · LOCAL FILES<br>SECURITY LEVEL · BIO-RESTRICTED<br>ACCESS MODE · EDUCATIONAL</div><br><hr><div class="side-info">CELL VISION / INTERNAL USE</div>""", unsafe_allow_html=True)

st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-04</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)
st.title("소포체 | ENDOPLASMIC RETICULUM")
st.caption("BIO-04 · 단백질과 지질의 합성 및 세포 내 물질 수송")
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")
st.divider()

left, right = st.columns([1, 1.6], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/er.png")
with right:
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>소포체는 막으로 이루어진 관 모양과 납작한 주머니 모양의 구조가 연결된 세포소기관이다. 거친면 소포체는 주로 단백질의 합성과 가공에 관여하고, 매끈면 소포체는 지질 합성과 해독, 칼슘 이온 저장 등에 관여한다.</div>""", unsafe_allow_html=True)

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
