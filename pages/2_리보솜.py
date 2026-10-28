
import streamlit as st
from pathlib import Path

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="CELL VISION | 리보솜",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "ribosome.png"

# =========================================================
# 2. 메인 화면과 통일된 전술형 디자인
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top, #102433 0%, #050b12 58%);
    color: #dceaf0;
    font-family: 'Noto Sans KR', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #07111b;
    border-right: 1px solid #244454;
}

[data-testid="stSidebar"] * {
    color: #dceaf0;
}

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #e8f5fa !important;
}

p, li, label {
    color: #c6d8e1;
    line-height: 1.9;
}

code, .system-label {
    font-family: 'IBM Plex Mono', monospace;
}

.system-label {
    color: #57d9e8;
    font-size: 0.76rem;
    letter-spacing: 0.12em;
}

.top-status {
    border-bottom: 1px solid #244454;
    padding-bottom: 12px;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
}

.overview {
    background: rgba(16, 36, 51, 0.75);
    border: 1px solid #244454;
    border-left: 3px solid #57d9e8;
    padding: 20px 22px;
    line-height: 1.95;
    color: #dceaf0;
}

.article-section {
    margin-top: 30px;
    line-height: 1.95;
}

.article-section h2 {
    border-bottom: 1px solid #244454;
    padding-bottom: 10px;
    margin-top: 35px;
    margin-bottom: 18px;
}

.article-section h3 {
    color: #8bd9e8 !important;
    margin-top: 23px;
    margin-bottom: 9px;
}

.section-label {
    color: #7993a3;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
}

div.stButton > button {
    background: #0b1b27;
    color: #dceaf0;
    border: 1px solid #315364;
    border-radius: 2px;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: #153546;
    color: #ffffff;
    border-color: #57d9e8;
}

div[data-testid="stSidebar"] a {
    color: #c6d8e1 !important;
    text-decoration: none;
}

div[data-testid="stSidebar"] a:hover {
    color: #57d9e8 !important;
}

hr {
    border-color: #244454;
}

[data-testid="stImage"] img {
    border: 1px solid #244454;
}

.footer-label {
    border-top: 1px solid #244454;
    padding-top: 14px;
    margin-top: 45px;
    color: #7993a3;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 3. 사이드바
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div style="padding: 12px 0 24px 0;">
            <div style="
                color:#57d9e8;
                font-family:'IBM Plex Mono',monospace;
                font-size:1.35rem;
                font-weight:700;
                letter-spacing:0.08em;">
                CELL VISION
            </div>
            <div style="
                color:#7993a3;
                font-family:'IBM Plex Mono',monospace;
                font-size:0.67rem;
                letter-spacing:0.08em;
                margin-top:5px;">
                BIOLOGICAL OPERATIONS UNIT
            </div>
        </div>
        <div style="
            color:#7993a3;
            font-family:'IBM Plex Mono',monospace;
            font-size:0.72rem;
            border-bottom:1px solid #244454;
            padding-bottom:8px;
            margin-bottom:10px;">
            01 / COMMAND MENU
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.page_link("app.py", label="메인 화면")

    st.markdown(
        """
        <div style="
            color:#7993a3;
            font-family:'IBM Plex Mono',monospace;
            font-size:0.72rem;
            border-bottom:1px solid #244454;
            padding-bottom:8px;
            margin-top:22px;
            margin-bottom:10px;">
            02 / INTELLIGENCE FILES
        </div>
        """,
        unsafe_allow_html=True,
    )

    organelle_pages = [
        ("pages/1_핵.py", "BIO-01 / 핵"),
        ("pages/2_리보솜.py", "BIO-02 / 리보솜"),
        ("pages/3_미토콘드리아.py", "BIO-03 / 미토콘드리아"),
        ("pages/4_소포체.py", "BIO-04 / 소포체"),
        ("pages/5_골지체.py", "BIO-05 / 골지체"),
        ("pages/6_리소좀.py", "BIO-06 / 리소좀"),
        ("pages/7_세포막.py", "BIO-07 / 세포막"),
        ("pages/8_세포질.py", "BIO-08 / 세포질"),
        ("pages/9_세포골격.py", "BIO-09 / 세포골격"),
    ]

    for page_path, page_label in organelle_pages:
        st.page_link(page_path, label=page_label)

    st.markdown(
        """
        <div style="
            color:#7993a3;
            font-family:'IBM Plex Mono',monospace;
            font-size:0.72rem;
            border-bottom:1px solid #244454;
            padding-bottom:8px;
            margin-top:24px;
            margin-bottom:12px;">
            03 / SYSTEM MONITOR
        </div>
        <div style="
            font-family:'IBM Plex Mono',monospace;
            font-size:0.72rem;
            line-height:2.1;">
            <div><span style="color:#8bd9b0;">●</span> SYSTEM STATUS ONLINE</div>
            <div style="color:#7993a3;">DATABASE LOCAL FILES</div>
            <div style="color:#7993a3;">SECURITY LEVEL BIO-RESTRICTED</div>
            <div style="color:#7993a3;">ACCESS MODE EDUCATIONAL</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 4. 페이지 상단
# =========================================================

st.markdown(
    """
    <div class="top-status">
        <span class="system-label">CELL VISION / INTELLIGENCE FILES</span>
        <span class="system-label">BIO-02 / RIBOSOME</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-label">BIOLOGICAL STRUCTURE DATABASE / 02</div>',
    unsafe_allow_html=True,
)

st.title("리보솜")
st.caption("Ribosome · 유전 정보를 바탕으로 단백질을 합성하는 세포 구조")

if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

st.divider()

# =========================================================
# 5. 이미지 및 개요
# =========================================================

image_col, overview_col = st.columns([1, 1.25], gap="large")

with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("images/ribosome.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    리보솜은 전령 RNA에 저장된 유전 정보를 읽고 아미노산을 연결하여
    단백질을 합성하는 구조이다. 리보솜은 리보솜 RNA와 단백질로
    이루어지며, 큰 소단위체와 작은 소단위체가 결합하여 기능한다.
    세포질에서 자유롭게 존재하거나 거친면 소포체에 붙어 작용한다.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 6. 기존 설명 내용
# =========================================================

st.markdown("---")

st.markdown("""
<div class="article-section">

## 구조

### 작은 소단위체

작은 소단위체는 전령 RNA와 결합하고 유전 암호를 읽는 데 관여한다.
전령 RNA의 염기 서열은 세 개씩 묶여 코돈을 형성하며, 각 코돈은
특정 아미노산이나 번역의 시작·종결 신호를 지정한다.

### 큰 소단위체

큰 소단위체는 아미노산 사이의 펩타이드 결합이 형성되도록 돕는다.
리보솜 내부에는 전령 RNA의 코돈에 맞는 운반 RNA가 자리 잡는
공간이 있으며, 아미노산이 차례대로 연결되어 폴리펩타이드가 만들어진다.

### 리보솜 RNA

리보솜 RNA(rRNA)는 리보솜의 구조를 이루는 동시에 단백질 합성의
핵심적인 반응에도 관여한다. 따라서 리보솜은 단순히 단백질만으로
구성된 구조가 아니라 RNA가 중요한 기능을 담당하는 복합체이다.

## 주요 기능

### 단백질 합성

리보솜은 세포가 생명 활동에 필요한 단백질을 만들도록 한다.
단백질은 효소, 수용체, 운반체, 세포 구조 구성 요소 등 다양한
역할을 담당하므로 리보솜의 작용은 세포의 성장과 유지에 필수적이다.

### 자유 리보솜과 결합 리보솜

세포질의 자유 리보솜에서 합성되는 단백질 중 상당수는 세포질에서
기능하거나 특정 세포 내 장소로 이동한다. 반면 거친면 소포체에
결합한 리보솜은 주로 분비 단백질, 막 단백질, 일부 소기관으로
보내지는 단백질의 합성에 관여한다. 두 리보솜은 기본적인 합성
기능이 같으며, 합성되는 단백질의 목적지에 따라 작용 위치가 달라진다.

## 작동 원리

### 번역의 시작

전령 RNA가 리보솜의 작은 소단위체와 결합하고 시작 코돈을 인식하면
번역이 시작된다. 시작 코돈은 일반적으로 메티오닌을 지정하며,
이후 리보솜은 전령 RNA의 정보를 차례대로 읽는다.

### 아미노산 연결

운반 RNA(tRNA)는 특정 아미노산을 리보솜으로 가져온다. 운반 RNA의
안티코돈은 전령 RNA의 코돈과 상보적으로 결합한다. 리보솜은 가져온
아미노산 사이의 펩타이드 결합 형성을 촉진하며, 폴리펩타이드 사슬을
점차 길게 만든다.

### 번역의 종결

리보솜이 종결 코돈에 도달하면 종결 인자가 작용하여 합성이 끝난다.
완성된 폴리펩타이드는 방출된 뒤 접히거나 추가적인 가공을 거쳐
기능적인 단백질이 된다.

## 다른 세포소기관과의 관계

### 핵

핵의 DNA에 저장된 정보는 전사 과정을 통해 전령 RNA로 전달된다.
전령 RNA가 핵공을 통과해 세포질로 이동하면 리보솜이 그 정보를
읽어 단백질을 합성한다.

### 소포체

분비되거나 막에 삽입될 단백질을 합성하는 리보솜은 거친면 소포체와
연결되어 작용한다. 새로 합성되는 단백질은 소포체 내부로 들어가거나
막에 삽입되며, 접힘과 품질 관리 등의 과정을 거친다.

### 골지체

소포체에서 가공된 단백질 중 일부는 운반 소낭을 통해 골지체로
이동한다. 골지체는 단백질을 추가로 가공하고 분류하여 세포막,
분비 소낭 또는 다른 목적지로 보낸다.

</div>
""", unsafe_allow_html=True)

# =========================================================
# 7. 페이지 하단
# =========================================================

st.markdown(
    """
    <div class="footer-label">
        CELL VISION / INTERNAL USE
    </div>
    """,
    unsafe_allow_html=True,
)
