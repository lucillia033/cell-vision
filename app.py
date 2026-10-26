
import streamlit as st
import math
import base64
from pathlib import Path

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

    .cell-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 0.3rem;
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
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }

    .organelle {
        position: absolute;
        width: 19%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    .organelle img {
        display: block;
        width: 70%;
        aspect-ratio: 1 / 1;
        object-fit: contain;
        border-radius: 50%;
        margin: 0 auto 5px auto;
    }

    .organelle-name {
        display: block;
        color: #F1F5F9;
        font-size: 0.95rem;
        font-weight: 600;
        text-align: center;
        text-decoration: none;
        overflow-wrap: anywhere;
    }

    .organelle-name:hover {
        color: #9DD6F5;
        text-decoration: underline;
    }

    @media (max-width: 700px) {
        .cell-layout {
            max-width: 600px;
        }

        .organelle {
            width: 21%;
        }

        .organelle img {
            width: 78%;
        }

        .organelle-name {
            font-size: 0.72rem;
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
    if not image_path.exists():
        return None

    extension = image_path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(extension, "image/png")

    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def show_cell_layout():
    cell_image = image_to_base64(IMAGE_DIR / "cell.png")

    if cell_image is None:
        st.error(
            "images 폴더에 cell.png 파일이 없습니다. "
            "세포 전체 이미지를 해당 폴더에 넣어 주세요."
        )
        return

    organelle_elements = []
    count = len(ORGANELLES)
    orbit_radius = 43

    for index, organelle in enumerate(ORGANELLES):
        angle = -90 + index * (360 / count)
        radians = math.radians(angle)

        x = 50 + orbit_radius * math.cos(radians)
        y = 50 + orbit_radius * math.sin(radians)

        image_data = image_to_base64(
            IMAGE_DIR / organelle["image"]
        )

        if image_data is None:
            image_element = (
                '<div style="color:#B8C7D9;">이미지 없음</div>'
            )
        else:
            image_element = (
                f'<img src="{image_data}" '
                f'alt="{organelle["name"]}">'
            )

        # Streamlit의 내부 페이지 경로로 이동하는 링크
        page_url = "/" + organelle["page"]

        organelle_elements.append(
            f"""
            <div class="organelle"
                 style="left:{x:.2f}%;top:{y:.2f}%;">
                {image_element}
                <a class="organelle-name"
                   href="{page_url}"
                   target="_self">
                    {organelle["name"]}
                </a>
            </div>
            """
        )

    st.markdown(
        f"""
        <div class="cell-layout">
            <div class="cell-center">
                <img src="{cell_image}" alt="세포 전체 구조">
            </div>
            {''.join(organelle_elements)}
        </div>
        """,
        unsafe_allow_html=True,
    )


show_cell_layout()
