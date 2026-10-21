
import streamlit as st
from pathlib import Path
from io import BytesIO
import base64
import html
from PIL import Image

st.set_page_config(
    page_title="Cell Explorer",
    page_icon="🔬",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# 소기관 정보
ORGANELLES = [
    {
        "key": "nucleus",
        "name": "핵",
        "english": "Nucleus",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "position": "top",
    },
    {
        "key": "ribosome",
        "name": "리보솜",
        "english": "Ribosome",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "position": "top",
    },
    {
        "key": "mitochondria",
        "name": "미토콘드리아",
        "english": "Mitochondria",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "position": "right",
    },
    {
        "key": "er",
        "name": "소포체",
        "english": "Endoplasmic Reticulum",
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "position": "right",
    },
    {
        "key": "golgi",
        "name": "골지체",
        "english": "Golgi Apparatus",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "position": "bottom",
    },
    {
        "key": "lysosome",
        "name": "리소좀",
        "english": "Lysosome",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "position": "bottom",
    },
    {
        "key": "membrane",
        "name": "세포막",
        "english": "Cell Membrane",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "position": "left",
    },
    {
        "key": "cytosol",
        "name": "세포질",
        "english": "Cytoplasm",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "position": "left",
    },
    {
        "key": "cytoskeleton",
        "name": "세포골격",
        "english": "Cytoskeleton",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "position": "bottom",
    },
]

# 이미지 파일을 HTML에서 사용할 수 있도록 변환
def image_to_base64(image_path):
    if not image_path.exists():
        return None

    try:
        with Image.open(image_path) as image:
            image = image.convert("RGBA")
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception:
        return None


# 이미지 클릭 시 페이지 이동 처리
PAGE_BY_KEY = {
    item["key"]: item["page"]
    for item in ORGANELLES
}

requested_page = st.query_params.get("go")

if requested_page in PAGE_BY_KEY:
    target_page = PAGE_BY_KEY[requested_page]

    # 반복 이동을 막기 위해 쿼리 매개변수 제거
    st.query_params.clear()
    st.switch_page(target_page)


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

    h1, h2, h3, h4, p, label {
        color: #F1F5F9;
    }

    [data-testid="stMarkdownContainer"] {
        color: #F1F5F9;
    }

    [data-testid="stCaptionContainer"] {
        color: #B8C5D1;
    }

    hr {
        border-color: #34495A;
    }

    .organelle-link {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        text-align: center;
        text-decoration: none !important;
        color: #FFFFFF !important;
        gap: 9px;
        padding: 12px 4px;
        border-radius: 16px;
        transition: background-color 0.2s ease,
                    transform 0.2s ease;
    }

    .organelle-link:hover {
        background-color: #1D2C39;
        transform: translateY(-3px);
    }

    .organelle-image {
        width: 104px;
        height: 104px;
        object-fit: contain;
        border-radius: 50%;
        border: 1px solid #405568;
        background-color: #1A2834;
        padding: 8px;
        box-sizing: border-box;
    }

    .organelle-name {
        color: #FFFFFF !important;
        font-size: 17px;
        font-weight: 700;
        line-height: 1.4;
    }

    .organelle-english {
        color: #B8C5D1 !important;
        font-size: 12px;
        line-height: 1.4;
    }

    .image-missing {
        width: 104px;
        height: 104px;
        border-radius: 50%;
        border: 1px dashed #64798B;
        background-color: #1A2834;
        color: #B8C5D1;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
    }

    .cell-image {
        display: block;
        width: 100%;
        max-width: 500px;
        max-height: 420px;
        object-fit: contain;
        margin: 0 auto;
    }

    .cell-placeholder {
        min-height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #B8C5D1;
        border: 1px dashed #405568;
        border-radius: 16px;
        background-color: #17232E;
        text-align: center;
        padding: 20px;
    }

    .center-caption {
        text-align: center;
        color: #B8C5D1;
        font-size: 13px;
        margin-top: 8px;
    }

    @media (max-width: 700px) {
        .organelle-image,
        .image-missing {
            width: 76px;
            height: 76px;
        }

        .organelle-name {
            font-size: 14px;
        }

        .organelle-english {
            font-size: 10px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 소기관 이미지와 이름을 함께 클릭할 수 있는 링크로 표시
def show_organelle(item):
    image_path = IMAGE_DIR / item["image"]
    encoded_image = image_to_base64(image_path)

    if encoded_image:
        image_html = (
            f'<img class="organelle-image" '
            f'src="data:image/png;base64,{encoded_image}" '
            f'alt="{html.escape(item["name"])}">'
        )
    else:
        image_html = (
            '<div class="image-missing">이미지 준비 중</div>'
        )

    name = html.escape(item["name"])
    english = html.escape(item["english"])
    key = html.escape(item["key"])

    st.markdown(
        f"""
        <a class="organelle-link" href="?go={key}">
            {image_html}
            <span class="organelle-name">{name}</span>
            <span class="organelle-english">{english}</span>
        </a>
        """,
        unsafe_allow_html=True
    )


# 메인 화면
st.markdown("# Cell Explorer")
st.markdown(
    "세포를 구성하는 소기관을 선택해 구조와 기능을 탐구해 보세요."
)

st.divider()

# 소기관 위치별 배치
top_items = [
    item for item in ORGANELLES
    if item["position"] == "top"
]

left_items = [
    item for item in ORGANELLES
    if item["position"] == "left"
]

right_items = [
    item for item in ORGANELLES
    if item["position"] == "right"
]

bottom_items = [
    item for item in ORGANELLES
    if item["position"] == "bottom"
]

# 상단 소기관
top_cols = st.columns(3, gap="medium")

for col, item in zip(top_cols, top_items):
    with col:
        show_organelle(item)

st.divider()

# 중앙 세포 이미지와 좌우 소기관
left_col, center_col, right_col = st.columns(
    [1, 2.2, 1],
    gap="medium"
)

with left_col:
    for item in left_items:
        show_organelle(item)

with center_col:
    cell_image_path = IMAGE_DIR / "cell.png"
    cell_image = image_to_base64(cell_image_path)

    if cell_image:
        st.markdown(
            f"""
            <img
                class="cell-image"
                src="data:image/png;base64,{cell_image}"
                alt="세포 전체 구조"
            >
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="center-caption">'
            '세포 전체 구조'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="cell-placeholder">
                <div>
                    <strong>세포 전체 이미지</strong><br><br>
                    images/cell.png 파일을 확인해 주세요.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

with right_col:
    for item in right_items:
        show_organelle(item)

st.divider()

# 하단 소기관
bottom_cols = st.columns(3, gap="medium")

for col, item in zip(bottom_cols, bottom_items):
    with col:
        show_organelle(item)

st.divider()

st.markdown(
    """
    <p style="text-align:center; color:#B8C5D1;">
        소기관의 원형 이미지를 클릭하면 해당 소기관의 상세 페이지로 이동합니다.
    </p>
    """,
    unsafe_allow_html=True
)
