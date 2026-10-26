
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

# 소기관 이미지와 상세 페이지 경로
ORGANELLES = {
    "nucleus": {
        "name": "핵",
        "english": "Nucleus",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    "ribosome": {
        "name": "리보솜",
        "english": "Ribosome",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    "mitochondria": {
        "name": "미토콘드리아",
        "english": "Mitochondria",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    "er": {
        "name": "소포체",
        "english": "Endoplasmic Reticulum",
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    "golgi": {
        "name": "골지체",
        "english": "Golgi Apparatus",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    "lysosome": {
        "name": "리소좀",
        "english": "Lysosome",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    "membrane": {
        "name": "세포막",
        "english": "Cell Membrane",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    "cytosol": {
        "name": "세포질",
        "english": "Cytoplasm",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    "cytoskeleton": {
        "name": "세포골격",
        "english": "Cytoskeleton",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
}

# 전체 화면 디자인
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

    [data-testid="stMainBlockContainer"] {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label {
        color: #F1F5F9;
    }

    .main-title {
        font-size: 2.8rem;
        font-weight: 300;
        letter-spacing: -1.5px;
        line-height: 1.2;
        margin-bottom: 8px;
        color: #F5F8FC;
    }

    .main-subtitle {
        color: #9EADBF;
        font-size: 0.95rem;
        margin-bottom: 5px;
    }

    .main-description {
        color: #77899D;
        font-size: 0.85rem;
        margin-bottom: 24px;
    }

    .organ-name {
        text-align: center;
        color: #F1F5F9;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 3px;
        margin-bottom: 1px;
    }

    .organ-english {
        text-align: center;
        color: #9EADBF;
        font-size: 0.76rem;
        min-height: 24px;
        margin-bottom: 6px;
    }

    div.stButton > button {
        background-color: rgba(20, 35, 52, 0.65);
        color: #DCEBFA;
        border: 1px solid #29465F;
        border-radius: 18px;
        padding: 0.3rem 0.8rem;
        font-size: 0.82rem;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #1B344B;
        border-color: #64C9FF;
        color: #FFFFFF;
    }

    div.stButton > button:focus {
        border-color: #64C9FF;
        color: #FFFFFF;
        box-shadow: 0 0 0 1px #64C9FF;
    }

    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }

    .cell-caption {
        text-align: center;
        color: #A6C8E5;
        font-size: 0.9rem;
        letter-spacing: 1px;
        margin-top: 5px;
    }

    hr {
        border-color: rgba(110, 160, 200, 0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# 이미지 표시와 상세 페이지 이동 버튼
def show_organelle(key, image_width=105):
    item = ORGANELLES[key]
    image_path = IMAGE_DIR / item["image"]

    # 이미지가 없으면 안내 문구를 표시하고 앱은 계속 실행
    if image_path.exists():
        st.image(str(image_path), width=image_width)
    else:
        st.markdown(
            f"""
            <div style="
                width:{image_width}px;
                height:{image_width}px;
                margin:auto;
                border:1px solid #42647F;
                border-radius:50%;
                display:flex;
                align-items:center;
                justify-content:center;
                text-align:center;
                color:#A9C8E3;
                font-size:13px;
                background:#101C2A;
            ">
                {item["name"]}<br>
                이미지 없음
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="organ-name">{item["name"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="organ-english">{item["english"]}</div>',
        unsafe_allow_html=True,
    )

    if st.button(
        "자세히 보기",
        key=f"open_{key}",
        use_container_width=True,
    ):
        st.switch_page(item["page"])


# 상단 제목
st.markdown(
    """
    <div class="main-title">Cell Vision</div>
    <div class="main-subtitle">세포 속 작은 세계를 탐험하다</div>
    <div class="main-description">
        소기관을 선택해 구조와 기능을 자세히 알아보세요.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# 첫 번째 줄: 세포골격, 핵, 리보솜
top_left, top_center, top_right = st.columns(3, gap="large")

with top_left:
    show_organelle("cytoskeleton")

with top_center:
    show_organelle("nucleus")

with top_right:
    show_organelle("ribosome")

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# 두 번째 줄: 소기관 4개와 중앙의 세포 전체 이미지
middle_left_outer, middle_left_inner, cell_center, middle_right_inner, middle_right_outer = (
    st.columns([1, 1, 2.4, 1, 1], gap="small")
)

with middle_left_outer:
    show_organelle("cytosol", image_width=90)

with middle_left_inner:
    show_organelle("membrane", image_width=90)

with cell_center:
    cell_path = IMAGE_DIR / "cell.png"

    if cell_path.exists():
        st.image(str(cell_path), width=360)
        st.markdown(
            '<div class="cell-caption">CELL STRUCTURE</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "중앙 세포 이미지가 없습니다. "
            "images 폴더에 cell.png 파일이 있는지 확인해 주세요."
        )

with middle_right_inner:
    show_organelle("mitochondria", image_width=90)

with middle_right_outer:
    show_organelle("er", image_width=90)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# 세 번째 줄: 리소좀, 골지체
bottom_left, bottom_center, bottom_right = st.columns(3, gap="large")

with bottom_left:
    show_organelle("lysosome")

with bottom_center:
    st.markdown(
        """
        <div style="
            text-align:center;
            padding-top:25px;
            color:#60778D;
            font-size:0.8rem;
            line-height:1.8;
        ">
            CELL VISION<br>
            <span style="color:#8298AD;">
                Explore the cell
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with bottom_right:
    show_organelle("golgi")

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#718399;
        font-size:0.78rem;
        padding:8px 0 18px 0;
    ">
        CELL VISION · 세포소기관 탐구
    </div>
    """,
    unsafe_allow_html=True,
)
