
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Cell Explorer - 동물세포 탐구",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# 원형 소기관 버튼 디자인
st.markdown("""
<style>
.organelle-circle {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    margin: 8px auto 18px auto;
    width: 100%;
}

/* Streamlit 버튼을 실제 원형으로 설정 */
.organelle-circle div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
    width: 100%;
}

.organelle-circle div[data-testid="stButton"] > button {
    width: 100px !important;
    min-width: 100px !important;
    max-width: 100px !important;
    height: 100px !important;
    min-height: 100px !important;
    max-height: 100px !important;
    padding: 8px !important;
    border-radius: 50% !important;
    border: 2px solid #8BAFCF !important;
    background-color: #EDF5FC !important;
    color: #244766 !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    line-height: 1.25 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    box-sizing: border-box !important;
    flex: 0 0 100px !important;
    transition: background-color 0.2s ease;
}

.organelle-circle div[data-testid="stButton"] > button:hover {
    background-color: #D7E9F8 !important;
    border-color: #477BA8 !important;
    color: #173B5C !important;
}

/* 소기관 그림 크기 */
.organelle-circle img {
    object-fit: contain;
}

.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: 750;
    color: #244766;
}

.main-description {
    text-align: center;
    color: #64748b;
    margin-bottom: 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">Cell Explorer</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="main-description">'
    '중앙의 세포와 주변 소기관을 선택해 탐구해 보세요.'
    '</div>',
    unsafe_allow_html=True
)

organelles = {
    "핵": ("pages/1_핵.py", "nucleus.png"),
    "리보솜": ("pages/2_리보솜.py", "ribosome.png"),
    "미토콘드리아": ("pages/3_미토콘드리아.py", "mitochondria.png"),
    "소포체": ("pages/4_소포체.py", "er.png"),
    "골지체": ("pages/5_골지체.py", "golgi.png"),
    "리소좀": ("pages/6_리소좀.py", "lysosome.png"),
    "세포막": ("pages/7_세포막.py", "membrane.png"),
    "세포질": ("pages/8_세포질.py", "cytosol.png"),
    "세포골격": ("pages/9_세포골격.py", "cytoskeleton.png"),
}

def show_organelle(name):
    page, image_name = organelles[name]
    image_path = IMAGE_DIR / image_name

    st.markdown('<div class="organelle-circle">', unsafe_allow_html=True)

    if image_path.is_file():
        try:
            with Image.open(image_path) as img:
                img.load()
                icon_image = img.convert("RGBA")
                icon_image.thumbnail((72, 72), Image.Resampling.LANCZOS)

            st.image(icon_image, width=60)
        except Exception:
            st.caption("소기관 그림")

    if st.button(name, key=f"organelle_{name}"):
        st.switch_page(page)

    st.markdown("</div>", unsafe_allow_html=True)


# 위쪽 소기관 3개
top = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1])

with top[1]:
    show_organelle("핵")

with top[4]:
    show_organelle("리보솜")

with top[7]:
    show_organelle("미토콘드리아")

st.markdown("---")

# 가운데 세포 그림과 양옆 소기관
left, center, right = st.columns([1.2, 3, 1.2], gap="medium")

with left:
    show_organelle("소포체")
    show_organelle("골지체")
    show_organelle("리소좀")

with center:
    cell_path = IMAGE_DIR / "cell.png"

    if cell_path.is_file():
        try:
            with Image.open(cell_path) as img:
                img.load()
                cell_image = img.convert("RGBA")

            # 원본 전체가 보이도록 비율을 유지해 축소
            cell_image.thumbnail((650, 500), Image.Resampling.LANCZOS)

            st.image(
                cell_image,
                caption="동물세포의 전체 구조",
                width=500
            )
        except Exception as error:
            st.error(f"세포 이미지를 표시하지 못했습니다: {error}")
    else:
        st.warning(
            "전체 세포 그림을 images/cell.png 경로에 추가해 주세요."
        )

with right:
    show_organelle("세포막")
    show_organelle("세포질")
    show_organelle("세포골격")

st.markdown("---")
st.caption("원형 소기관 버튼을 누르면 해당 소기관의 상세 페이지로 이동합니다.")
