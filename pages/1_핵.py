
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CELL VISION | Nucleus",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "nucleus.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');
.stApp {background:radial-gradient(ellipse at top,#102433 0%,#050b12 58%);color:#dceaf0;font-family:'Noto Sans KR',sans-serif}
[data-testid="stSidebar"] {background:#07111b;border-right:1px solid #244454}
[data-testid="stHeader"] {background:#050b12}
.block-container {max-width:1800px;padding-top:1.2rem;padding-bottom:3rem}
h1,h2,h3,p,li,label {color:#dceaf0}
h1 {font-family:'IBM Plex Mono',monospace!important;letter-spacing:1px}
.stCaption, [data-testid="stCaptionContainer"] {color:#7993a3!important}
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
    st.markdown("""
    <div class="side-brand">
      <div class="side-brand-title">CELL VISION</div>
      <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
    </div>
    <div class="side-section">01 / COMMAND MENU</div>
    """, unsafe_allow_html=True)
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")
    st.page_link("app.py", label="메인 화면")
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)
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
    for label, path in pages:
        st.page_link(path, label=label)
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

st.markdown("""
<div class="top-strip">
<span>SYSTEM / CELLULAR INTELLIGENCE</span>
<span>STATUS / ONLINE</span>
<span>FILE / BIO-01</span>
</div>
<div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>
""", unsafe_allow_html=True)

st.title("핵 | NUCLEUS")
st.caption("BIO-01 · 유전 정보의 보관과 세포 활동 조절")

if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

st.divider()

left, right = st.columns([1, 1.6], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/nucleus.png")
with right:
    st.markdown("""
    <div class="overview">
    <div class="info-label">CORE INTELLIGENCE</div>
    핵은 DNA를 보관하고 유전자 발현을 조절하여 세포의 구조와 기능을 통제하는 세포소기관이다.
    핵에서 전사된 유전 정보는 RNA 형태로 전달되며, 이를 바탕으로 필요한 단백질이 합성된다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>핵막</h3>
<p>핵막은 핵을 세포질과 구분하는 이중막 구조이다. 핵 내부의 유전 물질을 보호하고 핵과 세포질 사이의 물질 이동을 조절한다.</p>
<h3>핵공</h3>
<p>핵공은 핵막에 존재하는 통로이다. RNA와 단백질 등 여러 물질이 핵과 세포질 사이를 오갈 수 있도록 선택적으로 조절한다.</p>
<h3>염색질</h3>
<p>염색질은 DNA와 단백질이 결합한 물질이다. 세포가 분열할 때에는 염색체 형태로 응축되며, DNA에 저장된 유전 정보는 세포의 특성과 기능을 결정하는 데 관여한다.</p>
<h3>인</h3>
<p>인은 리보솜을 구성하는 rRNA가 합성되고 리보솜 소단위체가 조립되는 장소이다.</p>
<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<ul>
<li><b>유전 정보 보관:</b> DNA를 보관하여 세포의 유전 정보를 유지한다.</li>
<li><b>유전자 발현 조절:</b> 어떤 유전자가 언제 발현될지 조절하는 데 관여한다.</li>
<li><b>유전 정보 전달:</b> 세포 분열 과정에서 DNA가 복제되고 딸세포에 전달되도록 한다.</li>
</ul>
<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<p>단백질 합성에 필요한 유전 정보는 DNA의 특정 부분을 주형으로 RNA를 합성하는 전사 과정을 통해 전달된다. 생성된 mRNA는 핵공을 통해 세포질로 이동하고, 리보솜에서 번역되어 단백질 합성에 이용된다.</p>
<h2>04 / SYSTEM CONNECTIONS · 다른 소기관과의 관계</h2>
<ul>
<li><b>리보솜:</b> 핵의 인에서 리보솜 소단위체가 만들어진다.</li>
<li><b>소포체:</b> 핵막의 바깥막은 거친면 소포체와 연결되어 있다.</li>
<li><b>골지체:</b> 핵의 유전 정보에 따라 합성된 단백질 중 일부는 소포체와 골지체를 거쳐 이동한다.</li>
</ul>
</div>
""", unsafe_allow_html=True)
