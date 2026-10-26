
import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cell Vision",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# 각 소기관 이미지와 이동할 상세 페이지
ORGANELLES = [
    {
        "name": "핵",
        "english": "Nucleus",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "key": "nucleus",
        "position": "nucleus",
    },
    {
        "name": "리보솜",
        "english": "Ribosome",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "key": "ribosome",
        "position": "ribosome",
    },
    {
        "name": "미토콘드리아",
        "english": "Mitochondria",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "key": "mitochondria",
        "position": "mitochondria",
    },
    {
        "name": "소포체",
        "english": "Endoplasmic Reticulum",
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "key": "er",
        "position": "er",
    },
    {
        "name": "골지체",
        "english": "Golgi Apparatus",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "key": "golgi",
        "position": "golgi",
    },
    {
        "name": "리소좀",
        "english": "Lysosome",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "key": "lysosome",
        "position": "lysosome",
    },
    {
        "name": "세포막",
        "english": "Cell Membrane",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "key": "membrane",
        "position": "membrane",
    },
    {
        "name": "세포질",
        "english": "Cytoplasm",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "key": "cytosol",
        "position": "cytosol",
    },
    {
        "name": "세포골격",
        "english": "Cytoskeleton",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "key": "cytoskeleton",
        "position": "cytoskeleton",
    },
]

# 이미지 파일을 HTML에서 표시할 수 있는 데이터로 변환
def image_to_base64(filename):
    image_path = IMAGE_DIR / filename

    if not image_path.exists():
        return None

    suffix = image_path.suffix.lower()
    mime_type = "image/png" if suffix == ".png" else "image/jpeg"

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# 소기관 클릭 시 앱이 해당 상세 페이지로 이동
page_map = {
    organelle["key"]: organelle["page"]
    for organelle in ORGANELLES
}

selected_organelle = st.query_params.get("organelle")

if selected_organelle in page_map:
    st.switch_page(page_map[selected_organelle])


# 전체 화면 스타일
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #05080D;
        color: #F1F5F9;
    }

    [data-testid="stHeader"] {
        background: rgba(5, 8, 13, 0.95);
    }

    [data-testid="stSidebar"] {
        background-color: #101923;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 0;
    }

    h1, p {
        color: #F1F5F9;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 상단 제목
st.markdown(
    """
    <div style="margin-bottom: 8px;">
        <div style="
            font-size: 2.8rem;
            font-weight: 300;
            letter-spacing: -1.5px;
            color: #F4F7FB;
            line-height: 1.2;
        ">
            Cell Vision
        </div>
        <div style="
            margin-top: 9px;
            color: #9AA9BA;
            font-size: 0.95rem;
            letter-spacing: 0.3px;
        ">
            세포 속 작은 세계를 탐험하다
        </div>
        <div style="
            margin-top: 4px;
            color: #718096;
            font-size: 0.82rem;
        ">
            소기관 이미지를 클릭하면 구조와 기능을 자세히 확인할 수 있습니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 중앙 세포 이미지
cell_image = image_to_base64("cell.png")

if cell_image is None:
    cell_html = """
    <div class="cell-placeholder">
        <div class="placeholder-title">CELL</div>
        <div class="placeholder-subtitle">세포 전체 이미지</div>
        <div class="placeholder-note">
            images/cell.png 파일을 추가하면<br>
            이 위치에 세포 이미지가 표시됩니다.
        </div>
    </div>
    """
else:
    cell_html = f"""
    <img class="whole-cell"
         src="{cell_image}"
         alt="세포 전체 구조">
    """


# 소기관별 원형 이미지 HTML 생성
organelles_html = ""

for organelle in ORGANELLES:
    image_data = image_to_base64(organelle["image"])

    if image_data is None:
        image_content = f"""
        <div class="missing-image">
            {organelle["name"]}
        </div>
        """
    else:
        image_content = f"""
        <img
            class="organelle-image"
            src="{image_data}"
            alt="{organelle["name"]}"
        >
        """

    # 쿼리 매개변수로 이동하므로 HTML 링크에서 직접 페이지 이동 가능
    destination = "/?organelle=" + quote(organelle["key"])

    organelles_html += f"""
    <a class="organelle {organelle["position"]}"
       href="{destination}"
       aria-label="{organelle["name"]} 상세 페이지로 이동">
        <div class="image-ring">
            {image_content}
        </div>
        <div class="organelle-name">{organelle["name"]}</div>
        <div class="organelle-english">{organelle["english"]}</div>
    </a>
    """


# 메인 화면
main_html = f"""
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
    background: #05080D;
    color: #F1F5F9;
    font-family: Arial, "Malgun Gothic", sans-serif;
}}

.explorer {{
    position: relative;
    width: 100%;
    max-width: 940px;
    aspect-ratio: 1 / 1;
    margin: 0 auto;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 50% 49%,
            rgba(27, 74, 110, 0.15),
            transparent 34%
        );
}}

.orbit {{
    position: absolute;
    width: 61%;
    height: 61%;
    left: 19.5%;
    top: 19.5%;
    border: 1px solid rgba(103, 160, 205, 0.19);
    border-radius: 50%;
    pointer-events: none;
}}

.orbit-inner {{
    position: absolute;
    width: 47%;
    height: 47%;
    left: 26.5%;
    top: 26.5%;
    border: 1px solid rgba(103, 160, 205, 0.12);
    border-radius: 50%;
    pointer-events: none;
}}

.cell-center {{
    position: absolute;
    width: 43%;
    height: 43%;
    left: 28.5%;
    top: 28.5%;
    display: flex;
    justify-content: center;
    align-items: center;
}}

.whole-cell {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 0 12px rgba(60, 160, 255, 0.22));
}}

.cell-placeholder {{
    width: 100%;
    height: 100%;
    border: 1px solid rgba(93, 190, 255, 0.8);
    border-radius: 50%;
    background:
        radial-gradient(
            circle at 50% 43%,
            rgba(91, 150, 220, 0.35),
            rgba(17, 42, 67, 0.7) 55%,
            rgba(6, 12, 21, 0.95) 72%
        );
    box-shadow:
        0 0 20px rgba(55, 166, 255, 0.25),
        inset 0 0 28px rgba(70, 170, 255, 0.18);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 12px;
}}

.placeholder-title {{
    font-size: clamp(20px, 3vw, 34px);
    letter-spacing: 5px;
    font-weight: 300;
    color: #BFE7FF;
}}

.placeholder-subtitle {{
    margin-top: 6px;
    font-size: clamp(11px, 1.5vw, 15px);
    color: #FFFFFF;
}}

.placeholder-note {{
    margin-top: 12px;
    font-size: clamp(8px, 1vw, 11px);
    line-height: 1.6;
    color: #9FB5C9;
}}

.organelle {{
    position: absolute;
    width: 19%;
    min-width: 0;
    text-align: center;
    text-decoration: none !important;
    color: #F1F5F9 !important;
    z-index: 2;
    transform: translate(-50%, -50%);
    cursor: pointer;
}}

.image-ring {{
    width: clamp(66px, 10.5vw, 112px);
    height: clamp(66px, 10.5vw, 112px);
    max-width: 100%;
    aspect-ratio: 1 / 1;
    margin: 0 auto 8px;
    padding: 5px;
    border: 1.5px solid var(--ring-color);
    border-radius: 50%;
    background: rgba(7, 15, 26, 0.9);
    box-shadow:
        0 0 9px color-mix(in srgb, var(--ring-color) 45%, transparent),
        inset 0 0 12px rgba(110, 180, 255, 0.07);
    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        background 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.organelle:hover .image-ring {{
    transform: scale(1.08);
    background: rgba(20, 36, 55, 0.98);
    box-shadow:
        0 0 22px color-mix(in srgb, var(--ring-color) 75%, transparent),
        inset 0 0 15px rgba(110, 180, 255, 0.12);
}}

.organelle-image {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    border-radius: 50%;
    display: block;
}}

.missing-image {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    color: #A9C8E3;
    background: rgba(24, 47, 70, 0.8);
}}

.organelle-name {{
    font-size: clamp(11px, 1.35vw, 15px);
    font-weight: 650;
    line-height: 1.4;
    color: #F5F8FC;
    word-break: keep-all;
}}

.organelle-english {{
    margin-top: 2px;
    font-size: clamp(8px, 1vw, 11px);
    line-height: 1.35;
    color: #A9B8C9;
    overflow-wrap: anywhere;
}}

.nucleus {{
    left: 50%;
    top: 9%;
    --ring-color: #B58CFF;
}}

.ribosome {{
    left: 79%;
    top: 20%;
    --ring-color: #52C8FF;
}}

.mitochondria {{
    left: 91%;
    top: 43%;
    --ring-color: #FF986B;
}}

.er {{
    left: 88%;
    top: 68%;
    --ring-color: #49BFFF;
}}

.golgi {{
    left: 72%;
    top: 87%;
    --ring-color: #9FE7A6;
}}

.lysosome {{
    left: 50%;
    top: 91%;
    --ring-color: #C99AFF;
}}

.membrane {{
    left: 23%;
    top: 83%;
    --ring-color: #55E0FF;
}}

.cytosol {{
    left: 9%;
    top: 55%;
    --ring-color: #9EDBFF;
}}

.cytoskeleton {{
    left: 21%;
    top: 20%;
    --ring-color: #62C9FF;
}}

@media (min-width: 900px) {{
    .explorer {{
        width: 100%;
    }}
}}

@media (max-width: 600px) {{
    .explorer {{
        min-height: 420px;
    }}

    .organelle {{
        width: 21%;
    }}

    .image-ring {{
        width: clamp(48px, 12vw, 70px);
        height: clamp(48px, 12vw, 70px);
        padding: 3px;
    }}

    .organelle-english {{
        font-size: 8px;
    }}

    .placeholder-note {{
        display: none;
    }}
}}
</style>
</head>
<body>
<div class="explorer">
    <div class="orbit"></div>
    <div class="orbit-inner"></div>

    <div class="cell-center">
        {cell_html}
    </div>

    {organelles_html}
</div>
</body>
</html>
"""

components.html(
    main_html,
    height=900,
    scrolling=False,
)
