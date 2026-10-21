
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


# ---------- 다크 테마 ----------
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
    color: #EAF3FF !important;
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
    margin: 7px auto 12px auto;
}

.orbit-label {
    color: #F4F8FF !important;
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    margin-top: 7px;
}

.orbit-en {
    color: #A9BCD5 !important;
    font-size: 11px;
    text-align: center;
}

.center-cell {
    border: 1px solid #244D7A;
    border-radius: 18px;
    padding: 8px;
    background: radial-gradient(
        circle,
        #11284688,
        #050B1500 72%
    );
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
    width: 100px !important;
    min-width: 100px !important;
    max-width: 100px !important;
    height: 100px !important;
    min-height: 100px !important;
    padding: 8px !important;
    margin: 0 auto !important;
    border-radius: 50% !important;
    border: 2px solid #4FBFFF !important;
    background: #0B192B !important;
    color: #F4F8FF !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    line-height: 1.25 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    box-shadow: 0 0 15px #259DFF44 !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stButton"] > button p,
div[data-testid="stButton"] > button span {
    color: #F4F8FF !important;
}

div[data-testid="stButton"] > button:hover {
    background: #193453 !important;
    border-color: #B3E7FF !important;
    box-shadow: 0 0 25px #259DFF99 !important;
}

hr {
    border-color: #263B56 !important;
}

[data-testid="stAlert"] {
    background: #0D192B !important;
    color: #F4F8FF !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- 제목 ----------
st.markdown(
    '<div class="cv-title">Cell Vision</div>',
    unsafe_allow_html=True
)


# ---------- 소기관 정보 ----------
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


# ---------- 이미지 불러오기 ----------
def load_image(image_path):
    """이미지 파일을 확인하고 PIL 이미지로 반환합니다."""
    if not image_path.is_file():
        return None

    try:
        with Image.open(image_path) as original:
            original.load()
            return original.convert("RGBA")
    except (OSError, ValueError):
        return None


# ---------- 소기관 표시 ----------
def show_organelle(name):
    item = organelles[name]
    image_path = IMG / item["image"]

    st.markdown('<div class="orbit-card">', unsafe_allow_html=True)

    organelle_image = load_image(image_path)

    if organelle_image is not None:
        # 긴 링크나 Base64 문자열을 만들지 않고 이미지 직접 표시
        st.image(
            organelle_image,
            width=78
        )
    else:
        st.markdown(
            '<div style="height:78px;"></div>',
            unsafe_allow_html=True
        )
        st.caption(f"이미지 확인 필요: {item['image']}")

    st.markdown(
        f'<div class="orbit-label">{name}</div>'
        f'<div class="orbit-en">{item["english"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button(
        f"{name} 탐구",
        key=f"open_{name}",
        help=f"{name} 상세 페이지로 이동"
    ):
        st.switch_page(item["page"])


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
    cell_path = IMG / "cell.png"
    cell_image = load_image(cell_path)

    if cell_image is not None:
        # 중앙 이미지도 직접 표시해 긴 링크가 출력되지 않도록 처리
        st.markdown(
            '<div class="center-cell">',
            unsafe_allow_html=True
        )

        st.image(
            cell_image,
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="center-caption">EXPLORE THE CELL</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning(
            "중앙 세포 이미지를 찾을 수 없습니다. "
            "GitHub의 images 폴더에 cell.png 파일이 있는지 확인해 주세요."
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


# ---------- 하단 문구 ----------
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
