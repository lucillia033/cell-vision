
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

st.markdown(
    """
    <style>
    .stApp {
        background-color: #101820;
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] {
        background-color: #17232E;
    }

    h1, h2, h3, p, label {
        color: #F1F5F9;
    }

    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .main-description {
        text-align: center;
        color: #B8C7D9;
        margin-bottom: 2rem;
    }

    [data-testid="stImage"] img {
        border-radius: 50%;
        aspect-ratio: 1 / 1;
        object-fit: cover;
    }

    div.stButton > button {
        width: 100%;
        color: #F1F5F9;
        background-color: #17232E;
        border: 1px solid #405367;
        border-radius: 8px;
    }

    div.stButton > button:hover {
        border-color: #7FB3D5;
        color: #FFFFFF;
        background-color: #223446;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">Cell Vision</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="main-description">'
    '세포의 구조와 세포소기관의 기능을 탐구해 보세요.'
    '</div>',
    unsafe_allow_html=True,
)

ORGANELLES = [
    {
        "name": "핵",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    {
        "name": "리보솜",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    {
        "name": "미토콘드리아",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    {
        "name": "소포체",
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    {
        "name": "골지체",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    {
        "name": "리소좀",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    {
        "name": "세포막",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    {
        "name": "세포질",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    {
        "name": "세포골격",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
]


def show_organelle(item, image_width=105):
    """소기관 이미지와 이름을 표시하고 해당 상세 페이지로 이동한다."""
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        st.image(str(image_path), width=image_width)
    else:
        st.warning(f"이미지를 찾을 수 없습니다: {item['image']}")

    st.markdown(
        f"<p style='text-align:center; font-weight:600;'>"
        f"{item['name']}</p>",
        unsafe_allow_html=True,
    )

    if st.button(
        f"{item['name']} 탐구",
        key=f"open_{item['name']}",
        use_container_width=True,
    ):
        st.switch_page(item["page"])


# 위쪽: 원형 배치의 윗부분
top_left, top_mid, top_right = st.columns(3, gap="large")

with top_left:
    show_organelle(ORGANELLES[0])

with top_mid:
    show_organelle(ORGANELLES[1])

with top_right:
    show_organelle(ORGANELLES[2])


# 가운데: 소기관 - 중앙 세포 이미지 - 소기관
left_side, center, right_side = st.columns(
    [1.1, 2.4, 1.1],
    gap="large",
)

with left_side:
    st.write("")
    st.write("")
    show_organelle(ORGANELLES[3])

with center:
    cell_image = IMAGE_DIR / "cell.png"

    if cell_image.exists():
        st.image(str(cell_image), use_container_width=True)
    else:
        st.error(
            "images/cell.png 파일이 없습니다. "
            "세포 전체 이미지를 해당 경로에 넣어 주세요."
        )

with right_side:
    st.write("")
    st.write("")
    show_organelle(ORGANELLES[4])


# 아래쪽: 원형 배치의 아랫부분
bottom_columns = st.columns(4, gap="medium")

for column, item in zip(
    bottom_columns,
    ORGANELLES[5:9],
):
    with column:
        show_organelle(item, image_width=95)
