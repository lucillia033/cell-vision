
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CELL VISION | Cell Membrane", layout="wide", initial_sidebar_state="expanded")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "membrane.png"

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

st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-07</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)
st.title("세포막 | CELL MEMBRANE")
st.caption("BIO-07 · 세포 내부와 외부의 경계를 형성하고 물질 이동을 조절")
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")
st.divider()

left, right = st.columns([1, 1.6], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/membrane.png")
with right:
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>세포막은 세포의 안팎을 구분하는 얇은 막이다. 인지질 이중층과 여러 막 단백질을 바탕으로 물질의 출입을 조절하고, 외부 신호를 받아들이며 세포 내부 환경을 유지한다.</div>""", unsafe_allow_html=True)

st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>인지질 이중층</h3>
<p>세포막의 기본 구조는 인지질 이중층이다. 인지질은 물과 잘 상호작용하는 친수성 머리 부분과 물을 피하는 소수성 꼬리 부분을 가진다. 친수성 머리는 세포 안팎의 수용액을 향하고, 소수성 꼬리는 막의 안쪽을 향해 배열된다.</p>
<h3>막 단백질</h3>
<p>막 단백질은 물질 수송, 신호 수용, 세포 간 인식과 부착 등 다양한 기능을 수행한다. 일부 단백질은 막을 가로질러 통로 또는 운반체로 작용하고, 다른 단백질은 막의 한쪽 면에 위치해 효소나 신호 전달 요소로 기능한다.</p>
<h3>콜레스테롤과 탄수화물</h3>
<p>동물 세포막의 콜레스테롤은 막의 유동성과 안정성을 조절한다. 막 표면의 탄수화물은 단백질이나 지질에 결합한 형태로 존재하며, 세포 간 인식과 상호작용에 관여한다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>선택적 투과성</h3>
<p>세포막은 모든 물질을 동일하게 통과시키지 않는다. 물질의 크기, 전하, 지용성, 농도 차이와 막 단백질의 존재 여부에 따라 이동 가능성이 달라진다. 이를 선택적 투과성이라고 한다.</p>
<h3>신호 전달</h3>
<p>막 수용체는 호르몬이나 다른 신호 분자와 결합해 세포 내부에 반응을 일으킨다. 이를 통해 세포는 외부 환경의 변화에 대응하고 다른 세포와 정보를 주고받는다.</p>
<h3>세포 경계와 항상성 유지</h3>
<p>세포막은 세포 내부의 물질과 이온 농도를 조절하고 외부 환경과의 차이를 유지한다. 이 기능은 세포의 생존과 정상적인 대사 활동에 중요하다.</p>

<h2>03 / OPERATION PROCESS · 물질 수송</h2>
<h3>단순 확산</h3>
<p>단순 확산은 물질이 농도가 높은 곳에서 낮은 곳으로 이동하는 현상이다. 산소와 이산화 탄소처럼 막의 지질층을 통과할 수 있는 일부 작은 분자가 이에 해당하며, ATP를 직접 사용하지 않는다.</p>
<h3>촉진 확산</h3>
<p>촉진 확산은 막 단백질의 도움을 받아 물질이 농도 기울기를 따라 이동하는 과정이다. 통로 단백질이나 운반체 단백질이 관여하며, 물질은 농도가 높은 곳에서 낮은 곳으로 이동한다. ATP를 직접 사용하지 않는다.</p>
<h3>삼투</h3>
<p>삼투는 선택적으로 투과하는 막을 사이에 두고 물이 이동하는 현상이다. 물은 용질 농도 차이에 따라 이동하며, 이 과정은 세포의 부피와 수분 균형에 영향을 준다.</p>
<h3>능동 수송</h3>
<p>능동 수송은 물질을 농도 기울기에 거슬러 이동시키는 과정이다. 에너지를 필요로 하며, 막 단백질이 ATP 등의 에너지를 이용해 특정 이온이나 분자를 이동시킬 수 있다.</p>
<h3>세포내 섭취와 세포외 배출</h3>
<p>세포내 섭취는 세포막이 바깥 물질을 둘러싸 소낭을 형성하며 세포 안으로 받아들이는 과정이다. 세포외 배출은 소낭이 세포막과 융합하여 내용물을 세포 밖으로 내보내는 과정이다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포 구성 요소와의 관계</h2>
<h3>세포골격</h3>
<p>세포골격은 세포막의 형태를 지지하고 세포막 단백질의 위치와 세포의 움직임에 영향을 준다.</p>
<h3>골지체</h3>
<p>골지체에서 가공되고 분류된 막 단백질과 지질은 소낭을 통해 세포막으로 전달될 수 있다.</p>
<h3>미토콘드리아</h3>
<p>미토콘드리아가 합성하는 ATP는 세포막의 능동 수송과 같이 에너지가 필요한 과정에 이용된다.</p>
</div>
""", unsafe_allow_html=True)
