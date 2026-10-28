
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CELL VISION | Cytoplasm", layout="wide", initial_sidebar_state="expanded")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "cytosol.png"

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

st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-08</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)
st.title("세포질 | CYTOPLASM")
st.caption("BIO-08 · 세포 내부에서 다양한 물질대사와 수송이 이루어지는 공간")
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")
st.divider()

left, right = st.columns([1, 1.6], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/cytosol.png")
with right:
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>세포질은 세포막 안쪽에서 핵을 제외한 영역을 가리키며, 세포질 기질과 여러 세포소기관을 포함한다. 세포질 기질에서는 해당 과정 등 여러 대사 반응이 일어나고 물질이 확산하거나 세포 내부에서 이동한다.</div>""", unsafe_allow_html=True)

st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>세포질 기질</h3>
<p>세포질 기질은 세포막 안쪽의 수용성 환경으로 물, 이온, 단백질, 영양소와 다양한 작은 분자를 포함한다. 여러 효소가 이곳에서 반응을 촉진하며, 해당 과정과 같은 대사 반응이 진행된다.</p>
<h3>세포소기관이 존재하는 공간</h3>
<p>세포질에는 리보솜과 미토콘드리아, 소포체 등 여러 세포 구성 요소가 존재한다. 이들은 각각의 기능을 수행하면서 서로 물질과 정보를 주고받는다.</p>
<h3>세포골격</h3>
<p>세포질 내부에는 미세소관, 미세섬유, 중간섬유로 이루어진 세포골격이 분포한다. 세포골격은 세포의 형태를 지지하고 세포소기관의 위치와 세포 내부 수송에 관여한다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>물질대사</h3>
<p>세포질 기질에서는 포도당이 분해되는 해당 과정과 같은 대사 반응이 일어난다. 이 과정에서 ATP와 전자 운반체가 생성되고, 생성물은 다른 대사 과정에 이용될 수 있다.</p>
<h3>물질의 확산과 이동</h3>
<p>작은 분자와 이온은 농도 차이에 따라 세포질 안에서 확산할 수 있다. 세포골격과 운동 단백질은 일부 물질과 소낭이 세포 내부의 특정 위치로 이동하도록 돕는다.</p>
<h3>세포 내부 환경 유지</h3>
<p>세포질의 이온 농도와 산성도, 물의 양은 효소의 작용과 세포의 정상적인 기능에 영향을 준다. 세포는 막 수송과 대사 조절 등을 통해 내부 환경을 유지한다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>해당 과정</h3>
<p>해당 과정은 세포질 기질에서 포도당을 단계적으로 분해하여 피루브산을 생성하는 과정이다. 이 과정에서 ATP와 NADH가 생성되며, 산소를 직접 사용하지 않는다.</p>
<h3>물질의 세포 내 이동</h3>
<p>물질은 확산이나 세포골격을 통한 수송 등 여러 방식으로 세포 내부에서 이동한다. 소낭은 세포소기관 사이에서 단백질과 지질 등의 물질을 운반할 수 있다.</p>
<h3>대사 과정의 연결</h3>
<p>세포질에서 만들어진 대사 산물은 미토콘드리아를 비롯한 다른 세포 구성 요소로 이동해 후속 반응에 사용될 수 있다. 이처럼 세포질의 대사는 세포 전체의 에너지 전환과 연결된다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포 구성 요소와의 관계</h2>
<h3>미토콘드리아</h3>
<p>세포질에서 해당 과정으로 생성된 피루브산은 조건에 따라 미토콘드리아로 이동해 세포 호흡의 다음 단계에 이용된다.</p>
<h3>리보솜</h3>
<p>리보솜은 세포질에서 단백질을 합성한다. 합성된 단백질 중 일부는 세포질에서 기능하고, 일부는 다른 세포소기관으로 이동한다.</p>
<h3>세포골격과 세포막</h3>
<p>세포골격은 세포질의 형태를 유지하고 내부 수송을 돕는다. 세포막은 물질이 세포 안팎으로 이동하는 것을 조절하여 세포질 환경 유지에 기여한다.</p>
</div>
""", unsafe_allow_html=True)
