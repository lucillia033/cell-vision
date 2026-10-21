
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Cell Vision",
    page_icon="🔬",
    layout="wide"
)

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"

# ---------- 디자인 ----------
st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: radial-gradient(
        ellipse at 50% 40%,
        #10213a 0%,
        #070d18 55%,
        #03060c 100%
    ) !important;
    color: #F4F7FF !important;
}

[data-testid="stHeader"] {
    background: #050A13 !important;
}

[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"],
[data-testid="stSidebarNav"] {
    background: #080F1C !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] a {
    color: #EAF3FF !important;
}

[data-testid="stSidebarNav"] a {
    background: #0D192B !important;
    border-radius: 8px !important;
    margin: 4px 0 !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: #1B3150 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #183454 !important;
    border-left: 3px solid #55BFFF !important;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, h5, h6, p, label, li {
    color: #F4F7FF;
}

.cv-title {
    text-align: center;
    font-size: clamp(34px, 4vw, 54px);
    font-weight: 300;
    letter-spacing: 5px;
    color: #F4F8FF;
    margin: 0 0 28px 0;
    text-shadow: 0 0 24px #3B82F655;
}

.orbit-card {
    text-align: center;
    margin: 8px auto 20px auto;
}

.orbit-image {
    width: 88px;
    height: 88px;
    object-fit: contain;
    border-radius: 50%;
    padding: 5px;
    box-sizing: border-box;
    background: radial-gradient(circle, #132641, #07101F);
    border: 2px solid #4FBFFF;
    box-shadow: 0 0 14px #36AAFF55;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.orbit-image:hover {
    transform: scale(1.06);
    box-shadow: 0 0 24px #259DFF99;
}

.orbit-label {
    color: #FFFFFF !important;
    font-size: 15px;
    font-weight: 600;
    text-align: center;
    margin-top: 10px;
}

.orbit-en {
    color: #A9BCD5 !important;
    font-size: 11px;
    text-align: center;
    margin-top: 3px;
}

.center-cell {
    border: 1px solid #244D7A;
    border-radius: 18px;
    padding: 8px;
    background: #07101F;
    box-shadow: 0 0 35px #168BFF22;
}

.center-caption {
    text-align: center;
    color: #A9BCD5 !important;
    font-size: 12px;
    letter-spacing: 2px;
    margin-top: 8px;
}

div[data-testid="stButton"] > button {
    background: #0B192B !important;
    color: #F4F8FF !important;
    border: 1px solid #4FBFFF !important;
}

div[data-testid="stButton"] > button p {
    color: #F4F8FF !important;
}

hr {
    border-color: #263B56 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- 제목 ----------
st.markdown(
    '<div class="cv-title">Cell Vision</div>',
    unsafe_allow_html=True
)


# ---------- 소기관 데이터 ----------
organelles = {
    "핵": {
        "page": "pages/1_핵.py",
        "image": "nucleus.png",
        "english": "Nucleus"
    },
    "세포골격": {
        "page": "pages/9_세포골격.py",
        "image": "cytoskeleton.png",
        "english": "Cytoskeleton"
    },
    "리보솜": {
        "page": "pages/2_리보솜.py",
        "image": "ribosome.png",
        "english": "Ribosome"
    },
    "미토콘드리아": {
        "page": "pages/3_미토콘드리아.py",
        "image": "mitochondria.png",
        "english": "Mitochondria"
    },
    "소포체": {
        "page": "pages/4_소포체.py",
        "image": "er.png",
        "english": "Endoplasmic Reticulum"
    },
    "골지체": {
        "page": "pages/5_골지체.py",
        "image": "golgi.png",
        "english": "Golgi Apparatus"
    },
    "리소좀": {
        "page": "pages/6_리소좀.py",
        "image": "lysosome.png",
        "english": "Lysosome"
    },
    "세포막": {
        "page": "pages/7_세포막.py",
        "image": "membrane.png",
        "english": "Cell Membrane"
    },
    "세포질": {
        "page": "pages/8_세포질.py",
        "image": "cytosol.png",
        "english": "Cytoplasm"
    }
}


# ---------- 이미지 읽기 ----------
def load_image(image_path):
    if not image_path.is_file():
        return None

    try:
        with Image.open(image_path) as original:
            original.load()
            return original.convert("RGBA")
    except (OSError, ValueError):
        return None


# ---------- 소기관 카드 ----------
def show_organelle(name):
    item = organelles[name]
    image = load_image(IMG / item["image"])

    st.markdown('<div class="orbit-card">', unsafe_allow_html=True)

    # 이미지를 표시합니다.
    if image is not None:
        st.image(image, width=88)
    else:
        st.warning(f"{name} 이미지 파일을 찾을 수 없습니다.")

    # 이미지 아래에 소기관 이름을 표시합니다.
    st.markdown(
        f'<div class="orbit-label">{name}</div>'
        f'<div class="orbit-en">{item["english"]}</div>',
        unsafe_allow_html=True
    )

    # 버튼은 흰색 배경 문제를 피하기 위해 표시하지 않습니다.
    # 상세 페이지는 왼쪽 페이지 탐색 메뉴에서 열 수 있습니다.

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- 위쪽 소기관 ----------
top1, top2, top3, top4, top5 = st.columns(5)

with top1:
    show_organelle("세포골격")

with top3:
    show_organelle("핵")

with top5:
    show_organelle("리보솜")


# ---------- 중앙 세포와 양옆 소기관 ----------
left, center, right = st.columns(
    [1.15, 2.7, 1.15],
    gap="medium",
    vertical_alignment="center"
)

with left:
    show_organelle("세포질")
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    show_organelle("세포막")

with center:
    cell_image = load_image(IMG / "cell.png")

    if cell_image is not None:
        st.markdown(
            '<div class="center-cell">',
            unsafe_allow_html=True
        )
        st.image(cell_image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="center-caption">EXPLORE THE CELL</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "images 폴더에 cell.png 파일이 있는지 확인해 주세요."
        )

with right:
    show_organelle("미토콘드리아")
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    show_organelle("소포체")


# ---------- 아래쪽 소기관 ----------
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

bottom1, bottom2, bottom3, bottom4, bottom5 = st.columns(5)

with bottom2:
    show_organelle("리소좀")

with bottom4:
    show_organelle("골지체")


# ---------- 하단 ----------
st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#9EB2CD;
        font-size:11px;
        letter-spacing:2px;
    ">
        CELL STRUCTURE · INTERACTIVE BIOLOGY
    </div>
    """,
    unsafe_allow_html=True
)
