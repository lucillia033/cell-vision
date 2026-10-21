
import base64
import html
import math
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

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

    hr {
        border-color: #34495A;
    }

    iframe {
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

ORGANELLES = [
    {
        "name": "핵",
        "image": "nucleus.png",
        "page": "pages/1_핵.py"
    },
    {
        "name": "리보솜",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py"
    },
    {
        "name": "미토콘드리아",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py"
    },
    {
        "name": "소포체",
        "image": "er.png",
        "page": "pages/4_소포체.py"
    },
    {
        "name": "골지체",
        "image": "golgi.png",
        "page": "pages/5_골지체.py"
    },
    {
        "name": "리소좀",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py"
    },
    {
        "name": "세포막",
        "image": "membrane.png",
        "page": "pages/7_세포막.py"
    },
    {
        "name": "세포질",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py"
    },
    {
        "name": "세포골격",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py"
    },
]


def image_to_data_uri(image_path):
    """이미지를 HTML에서 표시할 수 있는 데이터 URI로 변환합니다."""
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

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def build_orbit_html():
    """중앙 세포 이미지와 원형으로 배치된 소기관을 생성합니다."""
    canvas_size = 760
    center = canvas_size / 2

    orbit_radius = 285
    organelle_size = 100
    center_size = 240

    cell_uri = image_to_data_uri(IMAGE_DIR / "cell.png")

    if cell_uri:
        center_image = f"""
            <img
                class="cell-image"
                src="{cell_uri}"
                alt="세포 전체 구조"
            />
        """
    else:
        center_image = """
            <div class="missing-cell">
                중앙 세포 이미지가 없습니다.
            </div>
        """

    organelle_elements = []

    for index, item in enumerate(ORGANELLES):
        angle = -90 + index * (360 / len(ORGANELLES))
        radians = math.radians(angle)

        x = center + orbit_radius * math.cos(radians)
        y = center + orbit_radius * math.sin(radians)

        image_path = IMAGE_DIR / item["image"]
        image_uri = image_to_data_uri(image_path)

        if image_uri:
            image_element = f"""
                <img
                    class="organelle-image"
                    src="{image_uri}"
                    alt="{html.escape(item['name'])}"
                />
            """
        else:
            image_element = f"""
                <div class="missing-organelle">
                    이미지 없음
                </div>
            """

        # HTML 내부에서 Streamlit의 페이지 경로를 임의로 조작하지 않습니다.
        # 이 링크는 아래의 페이지 이동 연결 단계에서 처리합니다.
        page_name = html.escape(item["page"], quote=True)

        organelle_elements.append(f"""
            <a
                class="organelle"
                href="?page={page_name}"
                aria-label="{html.escape(item['name'])} 상세 페이지"
                style="
                    left: {x}px;
                    top: {y}px;
                    width: {organelle_size}px;
                    transform: translate(-50%, -50%);
                "
            >
                {image_element}
                <span class="organelle-name">
                    {html.escape(item['name'])}
                </span>
            </a>
        """)

    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <style>
            * {{
                box-sizing: border-box;
            }}

            html, body {{
                margin: 0;
                padding: 0;
                background: #101820;
                color: #F1F5F9;
                font-family: Arial, sans-serif;
            }}

            .orbit-wrapper {{
                width: 100%;
                display: flex;
                justify-content: center;
                overflow: visible;
            }}

            .orbit {{
                position: relative;
                width: {canvas_size}px;
                height: {canvas_size}px;
                flex: 0 0 {canvas_size}px;
            }}

            .cell-center {{
                position: absolute;
                left: {center}px;
                top: {center}px;
                width: {center_size}px;
                height: {center_size}px;
                transform: translate(-50%, -50%);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }}

            .cell-image {{
                width: 100%;
                height: 100%;
                object-fit: contain;
            }}

            .missing-cell {{
                color: #B8C5D1;
                text-align: center;
                font-size: 14px;
            }}

            .organelle {{
                position: absolute;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 7px;
                text-decoration: none;
                color: #F1F5F9;
                cursor: pointer;
                z-index: 2;
            }}

            .organelle-image {{
                display: block;
                width: {organelle_size}px;
                height: {organelle_size}px;
                object-fit: contain;
                border-radius: 50%;
                transition: transform 0.18s ease;
            }}

            .organelle:hover .organelle-image {{
                transform: scale(1.08);
            }}

            .organelle-name {{
                display: block;
                width: 125px;
                text-align: center;
                color: #F1F5F9;
                font-size: 15px;
                font-weight: 600;
                line-height: 1.4;
                white-space: nowrap;
            }}

            .missing-organelle {{
                width: {organelle_size}px;
                height: {organelle_size}px;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 50%;
                background: #243746;
                color: #B8C5D1;
                font-size: 12px;
            }}

            @media (max-width: 800px) {{
                .orbit-wrapper {{
                    justify-content: flex-start;
                    overflow-x: auto;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="orbit-wrapper">
            <div class="orbit">
                <div class="cell-center">
                    {center_image}
                </div>

                {''.join(organelle_elements)}
            </div>
        </div>
    </body>
    </html>
    """


st.title("Cell Explorer")
st.write("세포를 구성하는 소기관을 탐색하고 각 구조와 기능을 알아보세요.")
st.divider()

components.html(
    build_orbit_html(),
    height=780,
    scrolling=False
)

st.divider()
st.caption("소기관 이미지를 선택해 각 구조와 기능을 탐색할 수 있습니다.")
