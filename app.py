
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# 소기관 이미지와 연결할 상세 페이지
ORGANELLES = {
    "핵": {
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    "리보솜": {
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    "미토콘드리아": {
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    "소포체": {
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    "골지체": {
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    "리소좀": {
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    "세포막": {
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    "세포질": {
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    "세포골격": {
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
}

# 전체 세포 이미지
CELL_IMAGE = IMAGE_DIR / "cell.png"

# 전체 디자인
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

    [data-testid="stSidebar"] * {
        color: #F1F5F9;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label {
        color: #F1F5F9;
    }

    /* 소기관 이미지를 원형으로 표시 */
    [data-testid="stImage"] img {
        border-radius: 50%;
        object-fit: cover;
    }

    /* 소기관 이름을 일반 텍스트 링크처럼 표시 */
    [data-testid="stPageLink"] a {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #F1F5F9 !important;
        text-decoration: none !important;
        justify-content: center !important;
        padding: 0.15rem 0 !important;
        min-height: 0 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
    }

    [data-testid="stPageLink"] a:hover {
        color: #7DD3FC !important;
        background: transparent !important;
        text-decoration: underline !important;
    }

    [data-testid="stPageLink"] p {
        color: inherit !important;
        text-align: center !important;
    }

    /* 중앙 세포 이미지 */
    .cell-caption {
        text-align: center;
        color: #F1F5F9;
        font-size: 1rem;
        margin-top: 0.4rem;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }

        [data-testid="stPageLink"] a {
            font-size: 0.75rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 제목
st.title("Cell Vision")
st.write("세포를 구성하는 소기관을 선택해 구조와 기능을 알아보세요.")

st.divider()


def show_organelle(name):
    """소기관 이미지와 이름을 표시하고 이름에 상세 페이지를 연결합니다."""
    info = ORGANELLES[name]
    image_path = IMAGE_DIR / info["image"]

    if image_path.is_file():
        st.image(str(image_path), use_container_width=True)
    else:
        st.warning(f"이미지를 찾을 수 없습니다: images/{info['image']}")

    st.page_link(
        info["page"],
        label=name,
        icon=None,
        use_container_width=True,
    )


def show_empty():
    """배치에서 빈 공간을 유지합니다."""
    st.empty()


# 원형 배치
# 각 행에 5개 열을 두어 세포 이미지를 중심으로 소기관을 둘러 배치합니다.

# 위쪽 소기관 3개
row1 = st.columns(5, gap="small")

with row1[0]:
    show_empty()
with row1[1]:
    show_organelle("핵")
with row1[2]:
    show_organelle("리보솜")
with row1[3]:
    show_organelle("미토콘드리아")
with row1[4]:
    show_empty()

st.write("")

# 왼쪽과 오른쪽 위쪽 소기관
row2 = st.columns(5, gap="small")

with row2[0]:
    show_organelle("소포체")
with row2[1]:
    show_empty()
with row2[2]:
    show_empty()
with row2[3]:
    show_empty()
with row2[4]:
    show_organelle("골지체")

st.write("")

# 가운데 세포 이미지와 양쪽 소기관
row3 = st.columns(5, gap="small")

with row3[0]:
    show_organelle("리소좀")

with row3[1]:
    show_empty()

with row3[2]:
    if CELL_IMAGE.is_file():
        st.image(str(CELL_IMAGE), use_container_width=True)
        st.markdown(
            '<div class="cell-caption">동물세포</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "전체 세포 이미지를 찾을 수 없습니다. "
            "전체 세포 이미지를 images/cell.png 파일명으로 저장해 주세요."
        )

with row3[3]:
    show_empty()

with row3[4]:
    show_organelle("세포막")

st.write("")

# 아래쪽 소기관
row4 = st.columns(5, gap="small")

with row4[0]:
    show_empty()
with row4[1]:
    show_organelle("세포질")
with row4[2]:
    show_empty()
with row4[3]:
    show_organelle("세포골격")
with row4[4]:
    show_empty()
