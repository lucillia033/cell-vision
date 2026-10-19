
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Cell Explorer - 동물세포 탐구",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: 750;
    color: #244766;
}
.main-description {
    text-align: center;
    color: #64748b;
    margin-bottom: 20px;
}
.organelle-button div.stButton > button {
    border-radius: 50%;
    width: 100px;
    height: 100px;
    min-height: 100px;
    white-space: normal;
    border: 2px solid #9CB8D3;
    background: #F2F7FC;
    color: #244766;
    font-weight: 600;
    margin: auto;
}
.organelle-button div.stButton > button:hover {
    background: #DCEBFA;
    border-color: #477BA8;
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
    """소기관 이미지와 원형 이동 버튼을 표시합니다."""
    page, image_name = organelles[name]
    image_path = IMAGE_DIR / image_name

    if image_path.is_file():
        try:
            with Image.open(image_path) as img:
                img.load()
                icon_image = img.convert("RGBA")

            icon_image.thumbnail((90, 90), Image.Resampling.LANCZOS)
            st.image(icon_image, width=75)
        except Exception:
            st.caption("소기관 이미지")

    st.markdown('<div class="organelle-button">', unsafe_allow_html=True)

    if st.button(
        name,
        key=f"organelle_{name}",
        use_container_width=True
    ):
        st.switch_page(page)

    st.markdown("</div>", unsafe_allow_html=True)


# 첫 번째 줄: 핵, 리보솜, 미토콘드리아
top = st.columns(9, gap="small")

for col, name in zip(
    [top[0], top[4], top[8]],
    ["핵", "리보솜", "미토콘드리아"]
):
    with col:
        show_organelle(name)

# 두 번째 줄: 왼쪽 소기관 / 중앙 세포 / 오른쪽 소기관
left, center, right = st.columns([1, 3, 1], gap="medium")

with left:
    show_organelle("소포체")
    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    show_organelle("골지체")
    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    show_organelle("리소좀")

with center:
    cell_path = IMAGE_DIR / "cell.png"

    if cell_path.is_file():
        try:
            with Image.open(cell_path) as img:
                img.load()
                cell_image = img.convert("RGBA")

            # 전체 사진을 자르지 않고 최대 영역 안에 맞춥니다.
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
            "중앙 세포 그림이 없습니다. "
            "전체 세포 그림을 images/cell.png로 추가해 주세요."
        )

with right:
    show_organelle("세포막")
    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    show_organelle("세포질")
    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    show_organelle("세포골격")

# 네 번째 위치의 소기관을 포함해 모든 소기관이 중앙 주변에 표시되도록 배치
st.markdown("---")
st.caption(
    "각 소기관 버튼을 누르면 해당 소기관의 상세 탐구 페이지로 이동합니다."
)
