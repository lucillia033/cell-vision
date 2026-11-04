
import streamlit as st
from pathlib import Path  # 파일이나 폴더의 위치를 다루는 기능

# 페이지 제목과 화면 크기, 처음 열었을 때 사이드바 상태를 설정합니다.
st.set_page_config(page_title="CELL VISION | Lysosome", layout="wide", initial_sidebar_state="expanded")

# 현재 파이썬 파일이 있는 폴더를 기준으로 프로젝트의 최상위 폴더 위치를 찾습니다.
ROOT_DIR = Path(__file__).resolve().parent.parent

# 리소좀 이미지 파일이 저장된 위치를 지정합니다.
IMAGE_PATH = ROOT_DIR / "images" / "lysosome.png"

# 화면의 전체적인 디자인을 설정합니다.
# 배경색, 글자색, 글꼴, 버튼 모양, 여백 등을 CSS로 꾸밉니다.
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
""", unsafe_allow_html=True)  # 위의 HTML과 CSS를 실제 화면에 적용합니다.

# 왼쪽 사이드바에 프로젝트 이름, 메뉴, 시스템 정보를 표시합니다.
with st.sidebar:
    # 프로젝트 이름과 메뉴 구역의 제목을 표시합니다.
    st.markdown("""<div class="side-brand"><div class="side-brand-title">CELL VISION</div><div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div></div><div class="side-section">01 / COMMAND MENU</div>""", unsafe_allow_html=True)
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")

    # 누르면 메인 화면으로 이동하는 링크를 만듭니다.
    st.page_link("app.py", label="메인 화면")

    # 각 세포소기관 페이지로 이동할 수 있도록 페이지 이름과 파일 경로를 목록에 저장합니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)
    pages = [("BIO-01 / 핵","pages/1_핵.py"),("BIO-02 / 리보솜","pages/2_리보솜.py"),("BIO-03 / 미토콘드리아","pages/3_미토콘드리아.py"),("BIO-04 / 소포체","pages/4_소포체.py"),("BIO-05 / 골지체","pages/5_골지체.py"),("BIO-06 / 리소좀","pages/6_리소좀.py"),("BIO-07 / 세포막","pages/7_세포막.py"),("BIO-08 / 세포질","pages/8_세포질.py"),("BIO-09 / 세포골격","pages/9_세포골격.py")]

    # 목록에 있는 페이지를 하나씩 꺼내 사이드바에 이동 링크로 표시합니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 시스템 상태와 보안 등급 등의 정보를 사이드바 아래쪽에 표시합니다.
    st.markdown("""<div class="side-section">03 / SYSTEM MONITOR</div><div class="side-info">SYSTEM STATUS · ONLINE<br>DATABASE · LOCAL FILES<br>SECURITY LEVEL · BIO-RESTRICTED<br>ACCESS MODE · EDUCATIONAL</div><br><hr><div class="side-info">CELL VISION / INTERNAL USE</div>""", unsafe_allow_html=True)

# 페이지 상단에 시스템 상태와 현재 자료의 번호를 표시합니다.
st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-06</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)

# 리소좀 페이지의 제목과 간단한 설명을 표시합니다.
st.title("리소좀 | LYSOSOME")
st.caption("BIO-06 · 세포 내 소화와 물질 재활용")

# 버튼을 누르면 메인 화면으로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 제목 영역과 본문 사이에 구분선을 표시합니다.
st.divider()

# 화면을 왼쪽과 오른쪽 두 영역으로 나눕니다.
# 왼쪽은 이미지, 오른쪽은 리소좀의 핵심 설명을 보여줍니다.
left, right = st.columns([1, 1.6], gap="large")

with left:
    # 리소좀 이미지 파일이 존재하면 화면에 표시합니다.
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        # 이미지 파일이 없으면 문제를 알려주는 메시지를 표시합니다.
        st.warning("이미지를 찾을 수 없습니다: images/lysosome.png")

with right:
    # 리소좀의 핵심 역할을 요약한 설명 상자를 표시합니다.
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>리소좀은 소화 효소를 이용해 세포 안으로 들어온 물질과 손상된 세포 구성 요소를 분해하는 막성 세포소기관이다. 분해된 작은 분자는 세포가 다시 이용할 수 있으며, 이를 통해 세포 내부 환경과 구성 요소를 유지한다.</div>""", unsafe_allow_html=True)

# 리소좀의 구조, 기능, 작동 원리, 다른 세포소기관과의 관계를 설명합니다.
# 아래 HTML은 화면에 표시되는 생물학 학습 내용이므로 원문을 그대로 유지합니다.
st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>리소좀 막</h3>
<p>리소좀은 하나의 막으로 둘러싸여 있어 내부의 소화 효소와 분해 중인 물질이 세포질과 직접 섞이지 않도록 한다. 막에는 물질의 이동과 내부 환경 유지에 관여하는 단백질이 존재한다.</p>
<h3>가수 분해 효소</h3>
<p>리소좀 내부에는 단백질, 핵산, 지질, 탄수화물 등을 분해하는 다양한 가수 분해 효소가 들어 있다. 이 효소들은 큰 분자를 더 작은 분자로 분해한다.</p>
<h3>산성 내부 환경</h3>
<p>리소좀 내부는 세포질보다 산성인 환경을 유지한다. 이 환경은 리소좀 효소가 효과적으로 작용하는 데 중요하며, 막의 수송 단백질이 수소 이온의 이동에 관여한다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>세포 내 소화</h3>
<p>세포가 받아들인 물질은 소낭을 통해 세포 안으로 들어올 수 있다. 소화 대상이 리소좀과 만나면 효소가 물질을 분해하고, 생성된 작은 분자는 세포가 다시 이용할 수 있다.</p>
<h3>손상된 구성 요소의 분해</h3>
<p>세포 안에서 기능이 떨어지거나 손상된 구성 요소는 분해 경로를 통해 제거될 수 있다. 이를 통해 불필요한 물질이 축적되는 것을 줄이고 세포 구성 요소를 재활용한다.</p>
<h3>자가 포식과 재활용</h3>
<p>자가 포식은 세포 내부의 일부 구성 요소를 막으로 둘러싸 분해 경로로 보내는 과정이다. 리소좀은 이 과정에서 전달된 물질을 분해하여 구성 성분을 재활용하도록 돕는다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>물질의 유입</h3>
<p>세포 내로 들어온 물질이나 분해할 세포 구성 요소는 막성 소낭에 담겨 리소좀의 분해 경로로 전달된다.</p>
<h3>효소에 의한 분해</h3>
<p>리소좀 내부의 산성 환경에서 가수 분해 효소가 큰 분자를 작은 분자로 분해한다. 단백질은 아미노산으로, 핵산은 뉴클레오타이드와 그 구성 성분으로 분해될 수 있다.</p>
<h3>분해 산물의 재사용</h3>
<p>분해로 생성된 작은 분자는 리소좀 막을 통과해 세포질로 이동할 수 있으며, 세포는 이를 새로운 물질을 합성하거나 에너지 대사에 활용한다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포소기관과의 관계</h2>
<h3>소포체</h3>
<p>리소좀에서 작용하는 효소는 단백질 합성 및 가공 경로를 거쳐 만들어진다. 소포체는 단백질의 합성과 초기 가공에 관여한다.</p>
<h3>골지체</h3>
<p>골지체는 일부 소화 효소를 가공하고 분류하여 리소좀으로 보내는 데 관여한다.</p>
<h3>세포막</h3>
<p>세포막은 세포외 물질을 소낭으로 받아들이는 세포내 섭취 과정에 관여한다. 유입된 물질은 이후 세포 내 소화 경로로 전달될 수 있다.</p>
</div>
""", unsafe_allow_html=True)  # HTML 설명을 웹 화면에 표시합니다.
