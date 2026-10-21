
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Explorer",
    page_icon="🔬",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# 어두운 테마
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

    h1, h2, h3, h4, p {
        color: #F1F5F9;
    }

    [data-testid="stCaptionContainer"] {
        color: #B8C5D1;
    }

    div.stButton > button {
        background-color: #243746;
        color: #F1F5F9;
        border: 1px solid #405568;
        border-radius: 10px;
        min-height: 42px;
    }

    div.stButton > button:hover {
        background-color: #344D60;
        color: #FFFFFF;
        border-color: #7C9BB5;
    }

    hr {
        border-color: #34495A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 소기관 정보
ORGANELLES = [
    {
        "name": "핵",
        "english": "Nucleus",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    {
        "name": "리보솜",
        "english": "Ribosome",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    {
        "name": "미토콘드리아",
        "english": "Mitochondria",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    {
        "name": "소포체",
        "english": "Endoplasmic Reticulum",
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    {
        "name": "골지체",
        "english": "Golgi Apparatus",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    {
        "name": "리소좀",
        "english": "Lysosome",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    {
        "name": "세포막",
        "english": "Cell Membrane",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    {
        "name": "세포질",
        "english": "Cytoplasm",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    {
        "name": "세포골격",
        "english": "Cytoskeleton",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
]

# 메인 제목
st.title("Cell Explorer")
st.write(
    "세포를 구성하는 소기관을 선택해 "
    "각 구조와 기능을 탐구해 보세요."
)

st.divider()

# 중앙 세포 이미지
cell_image_path = IMAGE_DIR / "cell.png"

if cell_image_path.exists():
    _, center_col, _ = st.columns([1, 2, 1])

    with center_col:
        st.image(
            str(cell_image_path),
            use_container_width=True
        )

    st.caption("세포 전체 구조")
else:
    st.info(
        "세포 전체 이미지가 없습니다. "
        "`images/cell.png` 파일을 확인해 주세요."
    )

st.divider()
st.subheader("세포소기관 탐색")
st.write(
    "이미지 아래의 소기관 이름을 선택하면 "
    "해당 소기관의 상세 페이지로 이동합니다."
)

# 소기관 카드
columns_per_row = 3

for start in range(0, len(ORGANELLES), columns_per_row):
    row_items = ORGANELLES[
        start:start + columns_per_row
    ]

    columns = st.columns(columns_per_row, gap="medium")

    for col, item in zip(columns, row_items):
        with col:
            image_path = IMAGE_DIR / item["image"]

            if image_path.exists():
                st.image(
                    str(image_path),
                    width=120
                )
            else:
                st.caption(
                    f"이미지 없음: {item['image']}"
                )

            st.markdown(f"### {item['name']}")
            st.caption(item["english"])

            if st.button(
                f"{item['name']} 자세히 보기",
                key=f"open_{item['name']}",
                use_container_width=True
            ):
                st.switch_page(item["page"])

            st.write("")

st.divider()

st.caption(
    "소기관을 선택해 구조와 기능을 자세히 알아보세요."
)
