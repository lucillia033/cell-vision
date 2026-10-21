
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
        min-height: 38px;
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
    </style>
    """,
    unsafe_allow_html=True
)

ORGANELLES = [
    {
        "name": "핵",
        "english": "Nucleus",
        "image": "nucleus.png",
        "page": "pages/1_핵.py"
    },
    {
        "name": "리보솜",
        "english": "Ribosome",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py"
    },
    {
        "name": "미토콘드리아",
        "english": "Mitochondria",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py"
    },
    {
        "name": "소포체",
        "english": "Endoplasmic Reticulum",
        "image": "er.png",
        "page": "pages/4_소포체.py"
    },
    {
        "name": "골지체",
        "english": "Golgi Apparatus",
        "image": "golgi.png",
        "page": "pages/5_골지체.py"
    },
    {
        "name": "리소좀",
        "english": "Lysosome",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py"
    },
    {
        "name": "세포막",
        "english": "Cell Membrane",
        "image": "membrane.png",
        "page": "pages/7_세포막.py"
    },
    {
        "name": "세포질",
        "english": "Cytoplasm",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py"
    },
    {
        "name": "세포골격",
        "english": "Cytoskeleton",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py"
    },
]


def show_organelle(item, image_width=105):
    """소기관 이미지, 이름, 상세 페이지 이동 버튼을 표시합니다."""
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        st.image(str(image_path), width=image_width)
    else:
        st.caption(f"이미지 없음: {item['image']}")

    st.markdown(
        f"<div style='text-align:center; font-weight:600;'>"
        f"{item['name']}</div>",
        unsafe_allow_html=True
    )

    st.caption(item["english"])

    if st.button(
        "자세히 보기",
        key=f"open_{item['name']}",
        use_container_width=True
    ):
        st.switch_page(item["page"])


# 제목
st.title("Cell Explorer")
st.write("세포를 구성하는 소기관을 탐색하고 각 구조와 기능을 알아보세요.")
st.divider()

# 위쪽 소기관 3개
top = st.columns(5, gap="small")

with top[1]:
    show_organelle(ORGANELLES[0])

with top[2]:
    show_organelle(ORGANELLES[1])

with top[3]:
    show_organelle(ORGANELLES[2])

st.write("")

# 가운데: 주변 소기관 + 중앙의 세포 전체 이미지
middle = st.columns([1, 1, 2, 1, 1], gap="small")

with middle[0]:
    show_organelle(ORGANELLES[3])

with middle[1]:
    show_organelle(ORGANELLES[4])

with middle[2]:
    cell_image_path = IMAGE_DIR / "cell.png"

    if cell_image_path.exists():
        st.image(
            str(cell_image_path),
            use_container_width=True
        )
        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:20px;
                font-weight:700;
                color:#F1F5F9;
                margin-top:8px;
            ">
                세포 전체 구조
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "`images/cell.png` 파일을 확인해 주세요."
        )

with middle[3]:
    show_organelle(ORGANELLES[5])

with middle[4]:
    show_organelle(ORGANELLES[6])

st.write("")

# 아래쪽 소기관 2개
bottom = st.columns(5, gap="small")

with bottom[1]:
    show_organelle(ORGANELLES[7])

with bottom[3]:
    show_organelle(ORGANELLES[8])

st.divider()
st.caption(
    "각 소기관의 자세히 보기 버튼을 누르면 "
    "해당 소기관의 상세 페이지로 이동합니다."
)
