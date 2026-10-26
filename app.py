
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Cell Vision",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

ORGANELLES = {
    "nucleus": {
        "name": "핵",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    "ribosome": {
        "name": "리보솜",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    "mitochondria": {
        "name": "미토콘드리아",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    "er": {
        "name": "소포체",
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    "golgi": {
        "name": "골지체",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    "lysosome": {
        "name": "리소좀",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    "membrane": {
        "name": "세포막",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    "cytosol": {
        "name": "세포질",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    "cytoskeleton": {
        "name": "세포골격",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
}

# 이미지 링크를 통해 전달된 소기관을 상세 페이지로 연결
selected = st.query_params.get("organelle")

if selected in ORGANELLES:
    st.switch_page(ORGANELLES[selected]["page"])

# 디자인
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05080D;
        color: #F1F5F9;
    }

    [data-testid="stHeader"] {
        background-color: #05080D;
    }

    [data-testid="stSidebar"] {
        background-color: #101923;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1120px;
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

    .cv-title {
        color: #F5F8FC;
        font-size: 2.8rem;
        font-weight: 300;
        letter-spacing: -1.5px;
        margin-bottom: 8px;
    }

    .cv-subtitle {
        color: #A9BED2;
        font-size: 0.95rem;
        margin-bottom: 5px;
    }

    .cv-description {
        color: #778DA3;
        font-size: 0.83rem;
        margin-bottom: 15px;
    }

    .organ-name {
        text-align: center;
        color: #F1F5F9;
        font-size: 0.95rem;
        font-weight: 600;
        margin-top: -8px;
        margin-bottom: 8px;
    }

    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }

    [data-testid="stImage"] img {
        object-fit: contain;
    }

    hr {
        border-color: rgba(110, 160, 200, 0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 제목
st.markdown(
    """
    <div class="cv-title">Cell Vision</div>
    <div class="cv-subtitle">세포 속 작은 세계를 탐험하다</div>
    <div class="cv-description">
        소기관 이미지를 클릭해 구조와 기능을 알아보세요.
    </div>
    """,
    unsafe_allow_html=True,
)

# 소기관 이미지와 이름
def show_organelle(key, width=100):
    item = ORGANELLES[key]
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        # 이미지 자체에 상세 페이지 이동 링크 연결
        st.image(
            str(image_path),
            width=width,
            link=f"?organelle={key}",
        )
    else:
        st.warning(
            f'{item["name"]} 이미지 파일을 찾을 수 없습니다: '
            f'images/{item["image"]}'
        )

    st.markdown(
        f'<div class="organ-name">{item["name"]}</div>',
        unsafe_allow_html=True,
    )


# 상단: 세포골격, 핵, 리보솜
top_spacer1, top_left, top_center, top_right, top_spacer2 = st.columns(
    [1, 1.2, 1.2, 1.2, 1],
    gap="small",
)

with top_left:
    show_organelle("cytoskeleton", 95)

with top_center:
    show_organelle("nucleus", 95)

with top_right:
    show_organelle("ribosome", 95)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# 중앙: 왼쪽 소기관 2개, 중앙 세포, 오른쪽 소기관 2개
left_outer, left_inner, center, right_inner, right_outer = st.columns(
    [1, 1, 2.5, 1, 1],
    gap="small",
)

with left_outer:
    st.markdown("<div style='height:65px'></div>", unsafe_allow_html=True)
    show_organelle("cytosol", 85)

with left_inner:
    st.markdown("<div style='height:155px'></div>", unsafe_allow_html=True)
    show_organelle("membrane", 85)

with center:
    cell_path = IMAGE_DIR / "cell.png"

    if cell_path.exists():
        st.image(str(cell_path), width=380)
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "images/cell.png 파일을 확인해 주세요."
        )

with right_inner:
    st.markdown("<div style='height:155px'></div>", unsafe_allow_html=True)
    show_organelle("mitochondria", 85)

with right_outer:
    st.markdown("<div style='height:65px'></div>", unsafe_allow_html=True)
    show_organelle("er", 85)

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# 하단: 리소좀, 골지체
bottom_spacer1, bottom_left, bottom_right, bottom_spacer2 = st.columns(
    [1, 1.3, 1.3, 1],
    gap="small",
)

with bottom_left:
    show_organelle("lysosome", 95)

with bottom_right:
    show_organelle("golgi", 95)

st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

# 세포골격, 핵, 리보솜, 세포질, 세포막,
# 미토콘드리아, 소포체, 리소좀, 골지체 총 9개 표시
