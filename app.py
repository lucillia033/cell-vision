
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

# 이미지 링크를 통해 전달된 소기관으로 이동
selected = st.query_params.get("organelle")

if selected in ORGANELLES:
    st.switch_page(ORGANELLES[selected]["page"])


# 전체 디자인
st.markdown(
    """
    <style>
    .stApp {
        background-color: #070B12;
        color: #F1F5F9;
    }

    [data-testid="stHeader"] {
        background-color: #070B12;
    }

    [data-testid="stSidebar"] {
        background-color: #111A27;
    }

    /* 사이드바의 선택하지 않은 페이지도 밝게 표시 */
    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] a span,
    [data-testid="stSidebarNav"] a p {
        color: #E6EDF5 !important;
        opacity: 1 !important;
    }

    /* 현재 선택한 페이지 */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: #263747 !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] span,
    [data-testid="stSidebarNav"] a[aria-current="page"] p {
        color: #FFFFFF !important;
    }

    /* 마우스를 올린 페이지 */
    [data-testid="stSidebarNav"] a:hover {
        background-color: #1B344B !important;
    }

    [data-testid="stSidebarNav"] a:hover span,
    [data-testid="stSidebarNav"] a:hover p {
        color: #FFFFFF !important;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .cv-title {
        color: #F5F8FC;
        font-size: 2.8rem;
        font-weight: 300;
        letter-spacing: -1.5px;
        line-height: 1.2;
        margin-bottom: 8px;
    }

    .cv-subtitle {
        color: #9EADBF;
        font-size: 0.95rem;
        margin-bottom: 5px;
    }

    .cv-description {
        color: #8295AA;
        font-size: 0.84rem;
        margin-bottom: 15px;
    }

    .organ-name {
        text-align: center;
        color: #F1F5F9;
        font-size: 0.95rem;
        font-weight: 600;
        line-height: 1.4;
        margin-top: -7px;
        margin-bottom: 8px;
        white-space: nowrap;
    }

    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }

    [data-testid="stImage"] img {
        object-fit: contain;
    }

    div[data-testid="stImage"] a {
        display: inline-block;
        border-radius: 50%;
        outline-offset: 4px;
    }

    div[data-testid="stImage"] a img {
        transition: filter 0.2s ease, transform 0.2s ease;
    }

    div[data-testid="stImage"] a:hover img {
        filter: drop-shadow(0 0 9px rgba(83, 193, 255, 0.65));
        transform: scale(1.04);
    }

    .cell-label {
        color: #A6C8E5;
        font-size: 0.75rem;
        text-align: center;
        letter-spacing: 2px;
        margin-top: -5px;
    }

    hr {
        border-color: rgba(110, 160, 200, 0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# 상단 제목
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


# 소기관 이미지 자체에 링크 연결
def show_organelle(key, width=100):
    item = ORGANELLES[key]
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        st.image(
            str(image_path),
            width=width,
            link=f"?organelle={key}",
            caption=None,
        )
    else:
        st.markdown(
            f"""
            <div style="
                width:{width}px;
                height:{width}px;
                margin:0 auto 8px auto;
                border:1px solid #52728D;
                border-radius:50%;
                display:flex;
                align-items:center;
                justify-content:center;
                text-align:center;
                color:#C5D9EA;
                background:#101C2A;
                font-size:13px;
            ">
                {item["name"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="organ-name">{item["name"]}</div>',
        unsafe_allow_html=True,
    )


# 화면을 원형에 가깝게 구성
# 위쪽: 세포골격, 핵, 리보솜
top_left, top_center, top_right = st.columns(
    [1, 1, 1],
    gap="small",
)

with top_left:
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    show_organelle("cytoskeleton", 100)

with top_center:
    show_organelle("nucleus", 100)

with top_right:
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    show_organelle("ribosome", 100)


# 중앙: 왼쪽과 오른쪽에 소기관, 가운데에 세포 전체 이미지
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

left_outer, left_inner, center, right_inner, right_outer = st.columns(
    [1.05, 1.05, 2.8, 1.05, 1.05],
    gap="small",
)

with left_outer:
    st.markdown("<div style='height:85px'></div>", unsafe_allow_html=True)
    show_organelle("cytosol", 90)

with left_inner:
    st.markdown("<div style='height:205px'></div>", unsafe_allow_html=True)
    show_organelle("membrane", 90)

with center:
    cell_path = IMAGE_DIR / "cell.png"

    if cell_path.exists():
        st.image(
            str(cell_path),
            width=390,
            caption=None,
        )
        st.markdown(
            '<div class="cell-label">CELL STRUCTURE</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "images 폴더에 cell.png 파일을 추가해 주세요."
        )

with right_inner:
    st.markdown("<div style='height:205px'></div>", unsafe_allow_html=True)
    show_organelle("mitochondria", 90)

with right_outer:
    st.markdown("<div style='height:85px'></div>", unsafe_allow_html=True)
    show_organelle("er", 90)


# 아래쪽: 리소좀과 골지체
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

bottom_left, bottom_center, bottom_right = st.columns(
    [1, 1, 1],
    gap="small",
)

with bottom_left:
    show_organelle("golgi", 100)

with bottom_center:
    show_organelle("lysosome", 100)

with bottom_right:
    st.markdown(
        """
        <div style="
            text-align:center;
            color:#71869B;
            font-size:0.8rem;
            padding-top:35px;
        ">
            CELL VISION
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
st.divider()
