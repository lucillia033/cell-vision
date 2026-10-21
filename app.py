
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Explorer",
    page_icon="🔬",
    layout="wide"
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

    [data-testid="stHeader"] {
        background-color: #101820;
    }

    [data-testid="stSidebar"] {
        background-color: #17232E;
    }

    h1, h2, h3, p, label {
        color: #F1F5F9;
    }

    [data-testid="stCaptionContainer"] {
        color: #B8C5D1;
    }

    div.stButton > button {
        background-color: #243746;
        color: #F1F5F9;
        border: 1px solid #405568;
        border-radius: 12px;
        min-height: 34px;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #344D60;
        border-color: #7C9BB5;
        color: #FFFFFF;
    }

    .stImage img {
        border-radius: 50%;
    }

    hr {
        border-color: #34495A;
    }

    .organelle-name {
        text-align: center;
        font-weight: 600;
        color: #F1F5F9;
        margin: 5px 0;
    }

    .cell-label {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #F1F5F9;
        margin-top: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

ORGANELLES = [
    {"name": "핵", "image": "nucleus.png", "page": "pages/1_핵.py"},
    {"name": "리보솜", "image": "ribosome.png", "page": "pages/2_리보솜.py"},
    {"name": "미토콘드리아", "image": "mitochondria.png", "page": "pages/3_미토콘드리아.py"},
    {"name": "소포체", "image": "er.png", "page": "pages/4_소포체.py"},
    {"name": "골지체", "image": "golgi.png", "page": "pages/5_골지체.py"},
    {"name": "리소좀", "image": "lysosome.png", "page": "pages/6_리소좀.py"},
    {"name": "세포막", "image": "membrane.png", "page": "pages/7_세포막.py"},
    {"name": "세포질", "image": "cytosol.png", "page": "pages/8_세포질.py"},
    {"name": "세포골격", "image": "cytoskeleton.png", "page": "pages/9_세포골격.py"},
]


def show_organelle(item, image_width=90):
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        st.image(str(image_path), width=image_width)
    else:
        st.caption(f"이미지 없음: {item['image']}")

    st.markdown(
        f"<div class='organelle-name'>{item['name']}</div>",
        unsafe_allow_html=True
    )

    if st.button(
        item["name"] + " 열기",
        key=f"open_{item['name']}",
        use_container_width=True
    ):
        st.switch_page(item["page"])


st.title("Cell Explorer")
st.write("세포를 구성하는 소기관을 탐색하고 각 구조와 기능을 알아보세요.")
st.divider()

# 넓은 중앙 영역과 양옆 소기관 영역
left, center, right = st.columns([1.2, 3.6, 1.2], gap="large")

with center:
    cell_image_path = IMAGE_DIR / "cell.png"

    if cell_image_path.exists():
        st.image(
            str(cell_image_path),
            width=560
        )
        st.markdown(
            "<div class='cell-label'>세포 전체 구조</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("images/cell.png 파일을 확인해 주세요.")

# 중앙 이미지 양옆 소기관
with left:
    show_organelle(ORGANELLES[3], image_width=85)
    st.write("")
    show_organelle(ORGANELLES[4], image_width=85)
    st.write("")
    show_organelle(ORGANELLES[7], image_width=85)

with right:
    show_organelle(ORGANELLES[5], image_width=85)
    st.write("")
    show_organelle(ORGANELLES[6], image_width=85)
    st.write("")
    show_organelle(ORGANELLES[8], image_width=85)

# 위쪽 소기관
top = st.columns(5, gap="medium")

with top[1]:
    show_organelle(ORGANELLES[0], image_width=85)

with top[2]:
    show_organelle(ORGANELLES[1], image_width=85)

with top[3]:
    show_organelle(ORGANELLES[2], image_width=85)

st.divider()
st.caption("소기관을 선택하면 해당 상세 페이지로 이동합니다.")
