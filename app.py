
import streamlit as st
import math
import base64
from pathlib import Path
from streamlit.components.v1 import html

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

    h1, h2, h3, p {
        color: #F1F5F9;
    }

    .cell-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .cell-description {
        text-align: center;
        color: #B8C7D9;
        margin-bottom: 1rem;
    }

    .cell-layout {
        position: relative;
        width: 100%;
        max-width: 900px;
        aspect-ratio: 1 / 1;
        margin: 0 auto;
    }

    .cell-center {
        position: absolute;
        width: 42%;
        height: 42%;
        top: 29%;
        left: 29%;
        border-radius: 50%;
        overflow: hidden;
    }

    .cell-center img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
        display: block;
    }

    .organelle {
        position: absolute;
        width: 18%;
        transform: translate(-50%, -50%);
        text-align: center;
        text-decoration: none;
        color: #F1F5F9;
    }

    .organelle img {
        display: block;
        width: 72%;
        aspect-ratio: 1 / 1;
        object-fit: contain;
        border-radius: 50%;
        margin: 0 auto 6px auto;
        transition: transform 0.2s ease;
    }

    .organelle:hover img {
        transform: scale(1.08);
    }

    .organelle-name {
        display: block;
        font-size: 0.95rem;
        font-weight: 600;
        color: #F1F5F9;
        overflow-wrap: anywhere;
    }

    .organelle:hover .organelle-name {
        color: #9DD6F5;
    }

    @media (max-width: 700px) {
        .cell-layout {
            max-width: 600px;
        }

        .organelle-name {
            font-size: 0.72rem;
        }

        .organelle img {
            width: 82%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="cell-title">Cell Vision</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="cell-description">'
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


def image_to_base64(image_path):
    """이미지 파일을 HTML에 표시할 수 있는 Base64 문자열로 변환한다."""
    if not image_path.exists():
        return None

    suffix = image_path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }
    mime_type = mime_types.get(suffix, "application/octet-stream")

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def build_cell_layout():
    """중앙 세포 이미지와 주변 소기관을 원형으로 배치한다."""
    cell_image_path = IMAGE_DIR / "cell.png"
    cell_image = image_to_base64(cell_image_path)

    if cell_image is None:
        st.error(
            "images/cell.png 파일을 찾을 수 없습니다. "
            "세포 전체 이미지를 images 폴더에 넣어 주세요."
        )
        return

    organelle_html = []

    # 첫 번째 소기관을 위쪽에 놓고 나머지는 원 둘레에 균등 배치한다.
    orbit_radius = 43
    count = len(ORGANELLES)

    for index, item in enumerate(ORGANELLES):
        angle = -90 + (360 / count) * index
        radians = math.radians(angle)

        x = 50 + orbit_radius * math.cos(radians)
        y = 50 + orbit_radius * math.sin(radians)

        organelle_image = image_to_base64(
            IMAGE_DIR / item["image"]
        )

        if organelle_image is None:
            organelle_html.append(
                f"""
                <div class="organelle"
                     style="left:{x:.2f}%;top:{y:.2f}%;">
                    <span class="organelle-name">{item["name"]}</span>
                </div>
                """
            )
            continue

        page_url = "/" + item["page"]

        organelle_html.append(
            f"""
            <a class="organelle"
               href="{page_url}"
               target="_self"
               style="left:{x:.2f}%;top:{y:.2f}%;"
               aria-label="{item["name"]}">
                <img src="{organelle_image}"
                     alt="{item["name"]}">
                <span class="organelle-name">{item["name"]}</span>
            </a>
            """
        )

    layout_html = f"""
    <div class="cell-layout">
        <div class="cell-center">
            <img src="{cell_image}" alt="세포 전체 구조">
        </div>
        {''.join(organelle_html)}
    </div>
    """

    html(layout_html, height=920, scrolling=False)


build_cell_layout()
