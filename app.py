
import base64
import html
import math
from pathlib import Path
from urllib.parse import quote

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

# 쿼리 매개변수로 전달된 페이지 이동 요청 처리
page_lookup = {item["page"]: item["page"] for item in ORGANELLES}
requested_page = st.query_params.get("go")

if requested_page in page_lookup:
    st.query_params.clear()
    st.switch_page(page_lookup[requested_page])


# 이미지 파일을 HTML에서 사용할 수 있도록 변환
def image_to_data_uri(image_path):
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
        ).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"
    except OSError:
        return None


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

    .intro-text {
        color: #B8C5D1;
        text-align: center;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Cell Explorer")

st.markdown(
    """
    <p class="intro-text">
        세포를 둘러싼 소기관을 선택해 구조와 기능을 탐색해 보세요.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#8FA8BA;
        font-size:13px;
        margin-top:0;
        margin-bottom:8px;
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
            <span>세포 이미지 없음</span>
            <small>images/cell.png 파일을 확인해 주세요.</small>
        </div>
    """


# 원형 궤도에 소기관 9개를 균등하게 배치
orbit_items = []

for index, item in enumerate(ORGANELLES):
    angle = -90 + index * (360 / len(ORGANELLES))
    radians = math.radians(angle)

    x = 50 + 36 * math.cos(radians)
    y = 50 + 36 * math.sin(radians)

    image_uri = image_to_data_uri(IMAGE_DIR / item["image"])
    name = html.escape(item["name"])
    page = quote(item["page"], safe="")

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

    # 부모 페이지의 주소를 기준으로 이동 URL을 생성합니다.
    # iframe 내부의 상대 주소로 이동하던 기존 방식을 수정했습니다.
    orbit_items.append(
        f"""
        <a class="organelle"
           href="?go={page}"
           data-page="{page}"
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

    <script>
    document.querySelectorAll(".organelle").forEach(function(link) {{
        link.addEventListener("click", function(event) {{
            event.preventDefault();

            const page = link.dataset.page;
            if (!page) return;

            try {{
                const destination = new URL(
                    window.parent.location.href
                );

                destination.searchParams.set(
                    "go",
                    decodeURIComponent(page)
                );

                window.parent.location.href =
                    destination.toString();
            }} catch (error) {{
                window.top.location.href = link.href;
            }}
        }});
    }});
    </script>
</body>
</html>
"""

components.html(
    orbit_html,
    height=760,
    scrolling=False,
)

st.caption("각 소기관 이미지를 선택해 상세 정보를 확인하세요.")
