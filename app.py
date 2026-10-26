
import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

st.set_page_config(
    page_title="Cell Vision",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

ORGANELLES = [
    {
        "key": "nucleus",
        "name": "핵",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
    },
    {
        "key": "ribosome",
        "name": "리보솜",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
    },
    {
        "key": "mitochondria",
        "name": "미토콘드리아",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
    },
    {
        "key": "er",
        "name": "소포체",
        "image": "er.png",
        "page": "pages/4_소포체.py",
    },
    {
        "key": "golgi",
        "name": "골지체",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
    },
    {
        "key": "lysosome",
        "name": "리소좀",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
    },
    {
        "key": "membrane",
        "name": "세포막",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
    },
    {
        "key": "cytosol",
        "name": "세포질",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
    },
    {
        "key": "cytoskeleton",
        "name": "세포골격",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
    },
]

# 이미지 파일을 HTML에서 표시할 수 있는 형태로 변환
def get_image_data(filename):
    path = IMAGE_DIR / filename

    if not path.exists():
        return None

    extension = path.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(extension, "image/png")

    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")

    return f"data:{mime};base64,{encoded}"


# 클릭한 소기관의 상세 페이지로 이동
page_map = {
    item["key"]: item["page"]
    for item in ORGANELLES
}

selected = st.query_params.get("organelle")

if selected in page_map:
    st.switch_page(page_map[selected])


# 화면 디자인
st.markdown(
    """
    <style>
    .stApp {
        background: #05080D;
        color: #F1F5F9;
    }

    [data-testid="stHeader"] {
        background: #05080D;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

    [data-testid="stSidebar"] {
        background: #101923;
    }

    .cv-title {
        color: #F5F8FC;
        font-size: clamp(2.1rem, 4vw, 3rem);
        font-weight: 300;
        letter-spacing: -1.5px;
        line-height: 1.2;
        margin-bottom: 8px;
    }

    .cv-subtitle {
        color: #9BAFC2;
        font-size: 0.9rem;
        margin-bottom: 0;
    }

    .cv-instruction {
        color: #70869B;
        font-size: 0.8rem;
        margin-top: 5px;
        margin-bottom: 12px;
    }

    .cv-explorer {
        position: relative;
        width: 100%;
        max-width: 850px;
        aspect-ratio: 1 / 1;
        margin: 0 auto;
        overflow: hidden;
        isolation: isolate;
        background:
            radial-gradient(
                circle at 50% 50%,
                rgba(23, 66, 100, 0.18) 0%,
                rgba(5, 8, 13, 0) 53%
            );
    }

    .cv-orbit {
        position: absolute;
        width: 69%;
        height: 69%;
        left: 15.5%;
        top: 15.5%;
        border: 1px solid rgba(100, 169, 220, 0.17);
        border-radius: 50%;
        pointer-events: none;
    }

    .cv-orbit-inner {
        position: absolute;
        width: 49%;
        height: 49%;
        left: 25.5%;
        top: 25.5%;
        border: 1px solid rgba(100, 169, 220, 0.10);
        border-radius: 50%;
        pointer-events: none;
    }

    .cv-center {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 43%;
        height: 43%;
        transform: translate(-50%, -50%);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1;
    }

    .cv-cell-image {
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
        filter: drop-shadow(0 0 13px rgba(64, 163, 255, 0.22));
    }

    .cv-cell-placeholder {
        width: 100%;
        aspect-ratio: 1 / 1;
        border: 1px solid rgba(85, 190, 255, 0.7);
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: radial-gradient(
            circle,
            #193754 0%,
            #0D1C2B 58%,
            #070B12 100%
        );
        color: #D6ECFF;
        box-shadow: 0 0 24px rgba(53, 158, 255, 0.14);
    }

    .cv-cell-placeholder strong {
        font-size: clamp(18px, 2.6vw, 30px);
        font-weight: 400;
        letter-spacing: 4px;
    }

    .cv-cell-placeholder span {
        color: #A4BED5;
        font-size: clamp(8px, 1vw, 11px);
        margin-top: 8px;
    }

    .cv-organelle {
        position: absolute;
        width: 18%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        text-decoration: none !important;
        color: #F1F5F9 !important;
        transform: translate(-50%, -50%);
        z-index: 2;
        cursor: pointer;
        -webkit-tap-highlight-color: transparent;
    }

    .cv-image-ring {
        width: clamp(64px, 10vw, 100px);
        aspect-ratio: 1 / 1;
        padding: 5px;
        border: 1.5px solid var(--ring);
        border-radius: 50%;
        background: rgba(7, 14, 24, 0.95);
        box-shadow:
            0 0 9px color-mix(in srgb, var(--ring) 45%, transparent),
            inset 0 0 10px rgba(111, 180, 255, 0.08);
        display: flex;
        align-items: center;
        justify-content: center;
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .cv-organelle:hover .cv-image-ring,
    .cv-organelle:focus-visible .cv-image-ring {
        transform: scale(1.09);
        box-shadow:
            0 0 20px color-mix(in srgb, var(--ring) 75%, transparent),
            inset 0 0 12px rgba(111, 180, 255, 0.13);
    }

    .cv-organelle:focus-visible {
        outline: none;
    }

    .cv-organelle-image {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 50%;
    }

    .cv-missing {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px;
        color: #BCD5E9;
        background: #122437;
    }

    .cv-organelle-name {
        margin-top: 7px;
        color: #F3F6FA;
        font-size: clamp(11px, 1.35vw, 15px);
        font-weight: 600;
        line-height: 1.35;
        text-align: center;
        white-space: nowrap;
    }

    /* 원형 궤도에 따라 9개 소기관을 균등 배치 */
    .cv-nucleus {
        left: 50%;
        top: 8%;
        --ring: #B68AFF;
    }

    .cv-ribosome {
        left: 77%;
        top: 16%;
        --ring: #55C8FF;
    }

    .cv-mitochondria {
        left: 91%;
        top: 39%;
        --ring: #FF9A70;
    }

    .cv-er {
        left: 88%;
        top: 67%;
        --ring: #53BFFF;
    }

    .cv-golgi {
        left: 72%;
        top: 86%;
        --ring: #9EE8A7;
    }

    .cv-lysosome {
        left: 50%;
        top: 92%;
        --ring: #C99AFF;
    }

    .cv-membrane {
        left: 28%;
        top: 86%;
        --ring: #5BDFF5;
    }

    .cv-cytosol {
        left: 9%;
        top: 67%;
        --ring: #9EDBFF;
    }

    .cv-cytoskeleton {
        left: 23%;
        top: 16%;
        --ring: #68CFFF;
    }

    @media (min-width: 900px) {
        .cv-explorer {
            width: 100%;
        }
    }

    @media (max-width: 600px) {
        .cv-explorer {
            min-width: 0;
        }

        .cv-organelle {
            width: 20%;
        }

        .cv-image-ring {
            width: clamp(43px, 11vw, 65px);
            padding: 3px;
        }

        .cv-organelle-name {
            font-size: clamp(9px, 2.5vw, 12px);
        }
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
    <div class="cv-instruction">
        소기관 이미지를 클릭해 구조와 기능을 알아보세요.
    </div>
    """,
    unsafe_allow_html=True,
)


# 중앙 세포 이미지
cell_data = get_image_data("cell.png")

if cell_data:
    center_html = f"""
    <img
        class="cv-cell-image"
        src="{cell_data}"
        alt="세포 전체 구조"
    >
    """
else:
    center_html = """
    <div class="cv-cell-placeholder">
        <strong>CELL</strong>
        <span>images/cell.png 파일을 추가해 주세요.</span>
    </div>
    """


# 소기관 이미지와 클릭 링크 생성
organelle_html = ""

for item in ORGANELLES:
    image_data = get_image_data(item["image"])

    if image_data:
        image_html = f"""
        <img
            class="cv-organelle-image"
            src="{image_data}"
            alt="{item["name"]}"
        >
        """
    else:
        image_html = f"""
        <div class="cv-missing">{item["name"]}</div>
        """

    # 링크를 누르면 쿼리 매개변수가 바뀌고
    # 위쪽의 page_map 코드가 상세 페이지로 전환합니다.
    href = "/?organelle=" + quote(item["key"])

    organelle_html += f"""
    <a
        class="cv-organelle cv-{item["key"]}"
        href="{href}"
        aria-label="{item["name"]} 상세 페이지로 이동"
        title="{item["name"]}"
    >
        <div class="cv-image-ring">
            {image_html}
        </div>
        <div class="cv-organelle-name">{item["name"]}</div>
    </a>
    """


# 하나의 메인 탐색 화면
explorer_html = f"""
<div class="cv-explorer">
    <div class="cv-orbit"></div>
    <div class="cv-orbit-inner"></div>

    <div class="cv-center">
        {center_html}
    </div>

    {organelle_html}
</div>
"""

st.markdown(explorer_html, unsafe_allow_html=True)
