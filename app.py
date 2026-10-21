
import streamlit as st
from pathlib import Path
from PIL import Image
import base64
from io import BytesIO

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
.stApp {
    background:
        radial-gradient(ellipse at 50% 44%, #0a1a32 0%, #050b15 48%, #02050a 100%);
    color: #f4f8ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

h1, h2, h3, p, label, span {
    color: #f4f8ff;
}

.cv-title {
    text-align: center;
    font-size: clamp(34px, 4vw, 54px);
    font-weight: 300;
    letter-spacing: 5px;
    color: #f4f8ff;
    margin: 0 0 22px 0;
    text-shadow: 0 0 24px #3b82f655;
}

.cv-subtitle {
    text-align: center;
    font-size: 13px;
    letter-spacing: 2px;
    color: #91a8c7;
    margin-top: -16px;
    margin-bottom: 25px;
}

.orbit-card {
    text-align: center;
    margin: 7px auto 18px auto;
}

.orbit-card img {
    width: 78px;
    height: 78px;
    object-fit: contain;
    border-radius: 50%;
    padding: 7px;
    background: radial-gradient(circle, #132641, #07101f);
    border: 2px solid #55bfff;
    box-shadow: 0 0 12px #36aaff88, inset 0 0 12px #36aaff22;
}

.orbit-label {
    color: #f4f8ff;
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    margin-top: 7px;
}

.orbit-en {
    color: #8ca4c3;
    font-size: 11px;
    text-align: center;
}

.center-cell {
    border: 1px solid #244d7a;
    border-radius: 50%;
    padding: 8px;
    background: radial-gradient(circle, #11284688, #050b1500 72%);
    box-shadow: 0 0 35px #168bff22;
}

.center-caption {
    text-align: center;
    color: #8ca4c3;
    font-size: 12px;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* 버튼은 원형이며 소기관 이름을 표시 */
div[data-testid="stButton"] > button {
    border-radius: 50% !important;
    width: 100px !important;
    min-width: 100px !important;
    max-width: 100px !important;
    height: 100px !important;
    min-height: 100px !important;
    padding: 8px !important;
    margin: 0 auto !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    background: #08172a !important;
    color: #f4f8ff !important;
    border: 2px solid #4fbfff !important;
    box-shadow: 0 0 15px #259dff44 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    transition: 0.2s ease;
}

div[data-testid="stButton"] > button:hover {
    background: #142e4b !important;
    border-color: #b3e7ff !important;
    box-shadow: 0 0 25px #259dff99 !important;
    transform: scale(1.04);
}

div[data-testid="stButton"] > button p {
    color: #f4f8ff !important;
}

hr {
    border-color: #20334d;
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

def show_organelle(name):
    item = organelles[name]
    image_path = IMG / item["image"]

    st.markdown('<div class="orbit-card">', unsafe_allow_html=True)

    if image_path.is_file():
        try:
            with Image.open(image_path) as im:
                im.load()
                im = im.convert("RGBA")
                im.thumbnail((150, 150), Image.Resampling.LANCZOS)

                buffer = BytesIO()
                im.save(buffer, format="PNG")
                encoded = base64.b64encode(
                    buffer.getvalue()
                ).decode("utf-8")

            st.markdown(
                f'<img src="data:image/png;base64,{encoded}" '
                f'alt="{name}" style="width:78px;height:78px;'
                f'object-fit:contain;border-radius:50%;'
                f'padding:7px;background:#10213a;'
                f'border:2px solid #55bfff;'
                f'box-shadow:0 0 14px #36aaff88;">',
                unsafe_allow_html=True
            )
        except Exception:
            st.markdown(
                '<div style="height:78px;"></div>',
                unsafe_allow_html=True
            )
    else:
        st.markdown(
            '<div style="height:78px;"></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="orbit-label">{name}</div>'
        f'<div class="orbit-en">{item["english"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button(
        f"{name} 탐구",
        key=f"open_{name}",
        help=f"{name} 상세 페이지로 이동"
    ):
        st.switch_page(item["page"])


# ---------- 상단 아이콘 ----------
top1, top2, top3, top4, top5 = st.columns(5)

with top1:
    show_organelle("세포골격")

with top3:
    show_organelle("핵")

with top5:
    show_organelle("리보솜")

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ---------- 중앙 세포 + 좌우 소기관 ----------
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

    if cell_path.is_file():
        try:
            with Image.open(cell_path) as im:
                im.load()
                cell_image = im.convert("RGBA")
                cell_image.thumbnail(
                    (650, 650),
                    Image.Resampling.LANCZOS
                )

            st.markdown('<div class="center-cell">', unsafe_allow_html=True)
            st.image(cell_image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown(
                '<div class="center-caption">'
                'EXPLORE THE CELL'
                '</div>',
                unsafe_allow_html=True
            )
        except Exception as error:
            st.error(f"세포 이미지를 불러오지 못했습니다: {error}")
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "전체 세포 그림을 images/cell.png로 추가해 주세요."
        )

with right:
    show_organelle("미토콘드리아")
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    show_organelle("소포체")

# ---------- 하단 아이콘 ----------
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

bottom1, bottom2, bottom3, bottom4, bottom5 = st.columns(5)

with bottom2:
    show_organelle("리소좀")

with bottom4:
    show_organelle("골지체")

# 세포막, 세포질, 세포골격, 핵, 리보솜, 미토콘드리아,
# 소포체, 골지체, 리소좀까지 9개 모두 연결됩니다.
st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:#647d9d;'
    'font-size:11px;letter-spacing:2px;">'
    'CELL STRUCTURE · INTERACTIVE BIOLOGY'
    '</div>',
    unsafe_allow_html=True
)
