
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CELL VISION | Golgi Apparatus", layout="wide", initial_sidebar_state="expanded")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "golgi.png"

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

st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-05</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)
st.title("골지체 | GOLGI APPARATUS")
st.caption("BIO-05 · 단백질과 지질의 가공, 분류 및 운반")
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")
st.divider()

left, right = st.columns([1, 1.6], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/golgi.png")
with right:
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>골지체는 소포체에서 전달된 단백질과 지질을 추가로 가공하고, 종류와 목적지에 따라 분류하여 운반하는 세포소기관이다. 납작한 막성 주머니인 시스터나가 여러 겹으로 쌓인 구조를 이룬다.</div>""", unsafe_allow_html=True)

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
