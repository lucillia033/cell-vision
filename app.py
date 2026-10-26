
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

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

CELL_IMAGE = IMAGE_DIR / "cell.png"

# 전체 화면 디자인
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
        max-width: 1500px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p {
        color: #F1F5F9;
    }

    /* 소기관 이름은 흰색으로 표시 */
    [data-testid="stPageLink"] a,
    [data-testid="stPageLink"] a p {
        color: #FFFFFF !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        text-decoration: none !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 0.1rem 0 !important;
        min-height: 0 !important;
    }

    [data-testid="stPageLink"] a:hover,
    [data-testid="stPageLink"] a:hover p {
        color: #7DD3FC !important;
        text-decoration: underline !important;
    }

    /* 소기관 이미지는 작고 원형으로 */
    .organelle-image img {
        border-radius: 50%;
        object-fit: cover;
    }

    /* 중앙 전체 세포 이미지 */
    .cell-caption {
        color: #FFFFFF;
        text-align: center;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.4rem;
            padding-right: 0.4rem;
        }

        [data-testid="stPageLink"] a,
        [data-testid="stPageLink"] a p {
            font-size: 0.75rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Cell Vision")
st.write("세포를 구성하는 소기관을 선택해 구조와 기능을 알아보세요.")
st.divider()


def show_organelle(name):
    """작은 소기관 이미지와 흰색 이름을 표시합니다."""
    info = ORGANELLES[name]
    image_path = IMAGE_DIR / info["image"]

    # 이미지 크기를 중앙 세포 이미지보다 작게 유지
    if image_path.is_file():
        st.markdown('<div class="organelle-image">', unsafe_allow_html=True)
        st.image(str(image_path), width=95)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"이미지를 찾을 수 없습니다: images/{info['image']}")

    # 이름을 누르면 해당 상세 페이지로 이동
    st.page_link(
        info["page"],
        label=name,
        icon=None,
        use_container_width=True,
    )


# 위쪽 소기관
top = st.columns(5, gap="small")

with top[0]:
    st.empty()
with top[1]:
    show_organelle("핵")
with top[2]:
    show_organelle("리보솜")
with top[3]:
    show_organelle("미토콘드리아")
with top[4]:
    st.empty()

st.write("")

# 중앙 위쪽 양옆 소기관
upper_sides = st.columns(5, gap="small")

with upper_sides[0]:
    show_organelle("소포체")
with upper_sides[1]:
    st.empty()
with upper_sides[2]:
    st.empty()
with upper_sides[3]:
    st.empty()
with upper_sides[4]:
    show_organelle("골지체")

st.write("")

# 중앙: 양쪽 소기관과 크게 표시한 전체 세포 이미지
middle = st.columns([1.1, 0.35, 3.2, 0.35, 1.1], gap="small")

with middle[0]:
    show_organelle("리소좀")

with middle[1]:
    st.empty()

with middle[2]:
    if CELL_IMAGE.is_file():
        # 중앙 이미지 영역을 넓게 사용
        st.image(str(CELL_IMAGE), use_container_width=True)
        st.markdown(
            '<div class="cell-caption">동물세포</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "전체 세포 이미지를 찾을 수 없습니다. "
            "전체 세포 이미지를 images/cell.png로 저장해 주세요."
        )

with middle[3]:
    st.empty()

with middle[4]:
    show_organelle("세포막")

st.write("")

# 아래쪽 소기관
bottom = st.columns(5, gap="small")

with bottom[0]:
    st.empty()
with bottom[1]:
    show_organelle("세포질")
with bottom[2]:
    st.empty()
with bottom[3]:
    show_organelle("세포골격")
with bottom[4]:
    st.empty()
