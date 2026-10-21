
import base64
import html
import math
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cell Explorer",
    page_icon="🔬",
    layout="wide",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

ORGANELLES = [
    {"name": "핵", "image": "nucleus.png", "page": "pages/1_핵.py"},
    {"name": "리보솜", "image": "ribosome.png", "page": "pages/2_리보솜.py"},
    {"name": "미토콘드리아", "image": "mitochondria.png", "page": "pages/3_미토콘드리아.py"},
    {"name": "소포체", "image": "er.png", "page": "pages/4_소포체.py"},
    {"name": "골지체", "image": "golgi.png", "page": "pages/5_골지체.py"},
    {"name": "리소좀", "image": "lysosome.png", "page": "pages/6_리소좀.py"},
    {"name": "세포막", "image": "membrane.png", "page": "pages/7_세포막.py"},
    {"name": "세포질", "image": "cytosol.png", "page": "pages/8_세포질.py"},
    {"name": "세포골격", "image": "cytoskeleton.png", "page": "pages/9_세포골격.py"},
]

# 허용된 상세 페이지로 이동
page_lookup = {item["page"]: item["page"] for item in ORGANELLES}
requested_page = st.query_params.get("go")

if requested_page in page_lookup:
    st.query_params.clear()
    st.switch_page(page_lookup[requested_page])


def image_to_data_uri(image_path):
    """이미지를 HTML에 직접 포함할 수 있는 URI로 변환합니다."""
    if not image_path.is_file():
        return None

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    mime_type = mime_types.get(image_path.suffix.lower())
    if mime_type is None:
        return None

    try:
        encoded = base64.b64encode(
            image_path.read_bytes()
        ).decode("ascii")
        return f"data:{mime_type};base64,{encoded}"
    except OSError:
        return None


# 현재 앱 주소를 확보하고 쿼리 문자열은 제거합니다.
# components.html 내부의 상대 주소를 사용하지 않기 위한 처리입니다.
try:
    current_url = st.context.url
except (AttributeError, RuntimeError):
    current_url = ""

if not current_url:
    st.error(
        "현재 앱 주소를 확인할 수 없습니다. "
        "페이지를 새로고침한 뒤 다시 시도해 주세요."
    )
    st.stop()

parsed_url = urlsplit(current_url)
APP_BASE_URL = urlunsplit(
    (
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        "",
        "",
    )
)


# 어두운 테마
st.markdown(
    """
    <style>
    .stApp {
        background: #101820;
        color: #F1F5F9;
    }

    [data-testid="stHeader"] {
        background: #101820;
    }

    [data-testid="stSidebar"] {
        background: #17232E;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

    h1, p {
        color: #F1F5F9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Cell Explorer")

st.markdown(
    """
    <p style="
        color:#B8C5D1;
        text-align:center;
        margin-bottom:4px;
    ">
        세포를 둘러싼 소기관을 선택해 구조와 기능을 탐색해 보세요.
    </p>
    <p style="
        color:#8FA8BA;
        text-align:center;
        font-size:13px;
        margin-top:0;
    ">
        소기관 이미지를 클릭하면 해당 상세 페이지로 이동합니다.
    </p>
    """,
    unsafe_allow_html=True,
)


# 중앙 세포 이미지
cell_image = image_to_data_uri(IMAGE_DIR / "cell.png")

if cell_image:
    center_html = f"""
        <div class="cell-center">
            <img src="{cell_image}" alt="세포 전체 구조">
        </div>
    """
else:
    center_html = """
        <div class="cell-center cell-placeholder">
            <span>세포 전체 이미지</span>
            <small>images/cell.png 파일을 확인해 주세요.</small>
        </div>
    """


# 소기관을 원주에 같은 간격으로 배치
orbit_items = []

for index, item in enumerate(ORGANELLES):
    angle = -90 + index * (360 / len(ORGANELLES))
    radians = math.radians(angle)

    x = 50 + 36 * math.cos(radians)
    y = 50 + 36 * math.sin(radians)

    image_uri = image_to_data_uri(IMAGE_DIR / item["image"])
    name = html.escape(item["name"])

    # 이미지가 없을 때도 해당 소기관의 링크는 유지합니다.
    if image_uri:
        image_html = (
            f'<img class="organelle-image" '
            f'src="{image_uri}" alt="{name}">'
        )
    else:
        image_html = (
            f'<span class="missing-image">'
            f'{name}<br>이미지 없음</span>'
        )

    # URL은 iframe 주소가 아닌 앱 주소를 기준으로 생성합니다.
    destination = (
        APP_BASE_URL
        + "?go="
        + quote(item["page"], safe="")
    )

    orbit_items.append(
        f"""
        <a class="organelle"
           href="{html.escape(destination, quote=True)}"
           target="_top"
           aria-label="{name} 상세 페이지로 이동"
           style="left:{x:.4f}%;top:{y:.4f}%;">
            <span class="image-circle">
                {image_html}
            </span>
            <span class="organelle-name">{name}</span>
        </a>
        """
    )


orbit_html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    background: #101820;
    color: #F1F5F9;
    font-family: Arial, "Malgun Gothic", sans-serif;
}}

.orbit {{
    position: relative;
    width: min(100%, 760px);
    aspect-ratio: 1 / 1;
    margin: 0 auto;
    overflow: visible;
    background: radial-gradient(
        circle,
        rgba(48, 75, 95, 0.18) 0%,
        rgba(16, 24, 32, 0) 67%
    );
}}

.orbit-ring {{
    position: absolute;
    width: 72%;
    height: 72%;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid rgba(142, 174, 198, 0.25);
    border-radius: 50%;
    pointer-events: none;
}}

.cell-center {{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 34%;
    height: 34%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    overflow: hidden;
    background: #17232E;
    border: 1px solid #405568;
    box-shadow: 0 0 28px rgba(103, 155, 190, 0.15);
    z-index: 1;
}}

.cell-center img {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

.cell-placeholder {{
    flex-direction: column;
    gap: 8px;
    text-align: center;
    padding: 12px;
}}

.cell-placeholder small {{
    color: #B8C5D1;
    font-size: 10px;
}}

.organelle {{
    position: absolute;
    width: 15%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    color: #F1F5F9;
    text-decoration: none;
    z-index: 2;
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
}}

.image-circle {{
    display: flex;
    width: 100%;
    aspect-ratio: 1 / 1;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 50%;
    background: #1B2A36;
    border: 2px solid #607D92;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    transition: transform 0.18s ease, border-color 0.18s ease;
}}

.organelle:hover .image-circle,
.organelle:focus-visible .image-circle {{
    transform: scale(1.08);
    border-color: #C2E3FA;
}}

.organelle-image {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 5px;
}}

.organelle-name {{
    display: block;
    width: max-content;
    max-width: 145%;
    color: #F1F5F9;
    font-size: clamp(10px, 1.8vw, 14px);
    font-weight: 600;
    text-align: center;
    white-space: nowrap;
    text-shadow: 0 1px 4px #101820;
}}

.missing-image {{
    color: #B8C5D1;
    font-size: 10px;
    text-align: center;
    padding: 4px;
}}

@media (max-width: 480px) {{
    .orbit {{
        width: 100%;
    }}

    .organelle {{
        width: 16%;
    }}

    .cell-center {{
        width: 32%;
        height: 32%;
    }}

    .organelle-name {{
        font-size: 10px;
    }}
}}
</style>
</head>

<body>
    <main class="orbit">
        <div class="orbit-ring"></div>
        {center_html}
        {''.join(orbit_items)}
    </main>
</body>
</html>
"""

components.html(
    orbit_html,
    height=760,
    scrolling=False,
)

st.caption("각 소기관 이미지를 선택해 상세 정보를 확인하세요.")
