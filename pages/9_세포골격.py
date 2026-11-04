
import streamlit as st
from pathlib import Path

# 페이지 제목과 화면 레이아웃, 사이드바의 초기 상태를 설정합니다.
st.set_page_config(page_title="CELL VISION | Cytoskeleton", layout="wide", initial_sidebar_state="expanded")

# 현재 파일의 위치를 기준으로 프로젝트 최상위 폴더와 이미지 경로를 설정합니다.
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "cytoskeleton.png"

# 페이지 전체에 적용할 글꼴, 배경색, 글자색, 버튼 및 각 영역의 디자인을 설정합니다.
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
""", unsafe_allow_html=True)  # CSS 스타일을 HTML로 화면에 적용합니다.

# 왼쪽 사이드바에 프로젝트 이름, 페이지 이동 링크, 시스템 상태 정보를 표시합니다.
with st.sidebar:
    # 사이드바 상단에 프로젝트 이름과 메뉴 제목을 표시합니다.
    st.markdown("""<div class="side-brand"><div class="side-brand-title">CELL VISION</div><div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div></div><div class="side-section">01 / COMMAND MENU</div>""", unsafe_allow_html=True)
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")

    # 메인 화면으로 이동할 수 있는 링크를 만듭니다.
    st.page_link("app.py", label="메인 화면")

    # 각 세포소기관 페이지의 이름과 파일 경로를 목록으로 정리합니다.
    st.markdown('<div class="side-section">02 / INTELLIGENCE FILES</div>', unsafe_allow_html=True)
    pages = [("BIO-01 / 핵","pages/1_핵.py"),("BIO-02 / 리보솜","pages/2_리보솜.py"),("BIO-03 / 미토콘드리아","pages/3_미토콘드리아.py"),("BIO-04 / 소포체","pages/4_소포체.py"),("BIO-05 / 골지체","pages/5_골지체.py"),("BIO-06 / 리소좀","pages/6_리소좀.py"),("BIO-07 / 세포막","pages/7_세포막.py"),("BIO-08 / 세포질","pages/8_세포질.py"),("BIO-09 / 세포골격","pages/9_세포골격.py")]

    # 목록에 있는 페이지를 하나씩 꺼내 사이드바에 이동 링크로 표시합니다.
    for label, path in pages:
        st.page_link(path, label=label)

    # 시스템 상태와 데이터베이스, 보안 등급 정보를 사이드바 하단에 표시합니다.
    st.markdown("""<div class="side-section">03 / SYSTEM MONITOR</div><div class="side-info">SYSTEM STATUS · ONLINE<br>DATABASE · LOCAL FILES<br>SECURITY LEVEL · BIO-RESTRICTED<br>ACCESS MODE · EDUCATIONAL</div><br><hr><div class="side-info">CELL VISION / INTERNAL USE</div>""", unsafe_allow_html=True)

# 페이지 상단에 시스템 상태와 현재 자료의 번호를 표시합니다.
st.markdown("""<div class="top-strip"><span>SYSTEM / CELLULAR INTELLIGENCE</span><span>STATUS / ONLINE</span><span>FILE / BIO-09</span></div><div class="eyebrow">TACTICAL BIOLOGY INTERFACE // INTELLIGENCE FILE</div>""", unsafe_allow_html=True)

# 세포골격 페이지의 제목과 간단한 설명을 표시합니다.
st.title("세포골격 | CYTOSKELETON")
st.caption("BIO-09 · 세포 형태 유지와 세포 내부 수송 및 운동")

# 버튼을 누르면 메인 화면으로 이동합니다.
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

# 구분선을 표시해 상단 영역과 본문을 나눕니다.
st.divider()

# 화면을 왼쪽과 오른쪽 두 영역으로 나눕니다.
left, right = st.columns([1, 1.6], gap="large")

# 왼쪽 영역에는 세포골격 이미지를 표시합니다.
with left:
    # 이미지 파일이 존재하면 화면에 표시하고, 없으면 경고 메시지를 보여줍니다.
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다: images/cytoskeleton.png")

# 오른쪽 영역에는 세포골격의 핵심 정보를 요약해 표시합니다.
with right:
    st.markdown("""<div class="overview"><div class="info-label">CORE INTELLIGENCE</div>세포골격은 세포 내부에 그물처럼 분포하는 단백질 섬유 구조이다. 세포의 형태를 유지하고 세포소기관의 위치를 지지하며, 세포 내부의 물질 수송과 세포 분열 및 운동에 관여한다.</div>""", unsafe_allow_html=True)

# 세포골격의 구조와 기능, 작동 원리, 다른 세포 구성 요소와의 관계를 설명합니다.
# HTML로 작성된 각 제목과 문단은 위에서 설정한 CSS 디자인을 적용받습니다.
st.markdown("""
<div class="article-section">
<h2>01 / STRUCTURE ANALYSIS · 구조</h2>
<h3>미세소관</h3>
<p>미세소관은 튜불린 단백질로 이루어진 속이 빈 관 모양의 구조이다. 세포 내부에서 소낭과 세포소기관이 이동하는 경로가 되며, 세포 분열 때 방추사를 형성해 염색체의 이동에 관여한다.</p>
<h3>미세섬유</h3>
<p>미세섬유는 주로 액틴 단백질로 이루어진 가느다란 섬유이다. 세포의 형태 변화, 세포 이동, 근육 수축, 세포질 분열 등에 관여한다.</p>
<h3>중간섬유</h3>
<p>중간섬유는 여러 단백질로 이루어진 섬유 구조로, 세포에 기계적인 강도를 제공한다. 세포가 물리적인 힘을 받을 때 구조가 쉽게 손상되지 않도록 지지하며, 일부 세포에서는 핵의 형태 유지에도 관여한다.</p>

<h2>02 / PRIMARY FUNCTIONS · 주요 기능</h2>
<h3>세포 형태 유지</h3>
<p>세포골격은 세포 내부의 구조를 지지하고 세포의 형태를 유지하도록 돕는다. 세포의 종류와 기능에 따라 각 섬유의 분포와 배열이 달라질 수 있다.</p>
<h3>세포 내부 수송</h3>
<p>미세소관과 액틴 섬유는 운동 단백질과 함께 소낭 및 세포소기관의 이동에 관여한다. 이를 통해 세포 내부의 필요한 위치로 물질을 전달할 수 있다.</p>
<h3>세포 분열과 운동</h3>
<p>세포 분열에서는 미세소관으로 이루어진 방추사가 염색체를 분리하는 데 관여한다. 액틴 미세섬유는 세포질 분열 과정에서 세포가 나뉘는 데 중요한 역할을 한다. 세포골격은 일부 세포의 이동과 형태 변화에도 관여한다.</p>

<h2>03 / OPERATION PROCESS · 작동 원리</h2>
<h3>섬유의 조립과 해체</h3>
<p>세포골격 섬유는 단백질 소단위체가 결합하거나 분리되면서 구조가 바뀔 수 있다. 이러한 변화는 세포가 모양을 바꾸거나 내부 구조를 재배치하는 데 중요하다.</p>
<h3>운동 단백질을 통한 이동</h3>
<p>운동 단백질은 세포골격 섬유를 따라 이동하면서 소낭이나 세포소기관을 운반할 수 있다. 이동에는 ATP의 에너지가 이용되며, 세포 내부의 물질이 적절한 장소로 전달되도록 돕는다.</p>
<h3>세포 분열에서의 역할</h3>
<p>세포 분열 시 미세소관이 재구성되어 방추사를 형성한다. 방추사는 염색체에 연결되어 염색체가 딸세포로 분리되도록 돕고, 액틴 미세섬유는 세포질 분열에 관여한다.</p>

<h2>04 / SYSTEM CONNECTIONS · 다른 세포 구성 요소와의 관계</h2>
<h3>핵</h3>
<p>세포골격은 핵 주변의 구조를 지지하고 세포 분열 과정에서 염색체의 이동에 관여한다.</p>
<h3>소포체와 골지체</h3>
<p>소포체와 골지체 사이를 이동하는 운반 소낭은 세포골격과 운동 단백질의 도움을 받아 세포 내부에서 이동할 수 있다.</p>
<h3>세포막</h3>
<p>세포골격은 세포막의 형태와 일부 막 단백질의 위치를 지지한다. 세포의 이동이나 형태 변화가 일어날 때에도 세포막과 세포골격이 함께 작용한다.</p>
<h3>미토콘드리아</h3>
<p>미토콘드리아가 생산하는 ATP는 운동 단백질의 활동과 세포골격의 재구성 등 에너지가 필요한 세포 과정에 이용된다.</p>
</div>
""", unsafe_allow_html=True)  # HTML 문서의 내용을 화면에 표시합니다.
