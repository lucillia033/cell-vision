
import streamlit as st
from pathlib import Path
import math

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

    div.stButton > button {
        background-color: #243746;
        color: #F1F5F9;
        border: 1px solid #405568;
        border-radius: 12px;
        min-height: 34px;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #344D60;
        border-color: #7C9BB5;
        color: #FFFFFF;
    }

    .stImage img {
        border-radius: 50%;
    }

    hr {
        border-color: #34495A;
    }

    .organelle-name {
        text-align: center;
        font-weight: 600;
        color: #F1F5F9;
        margin: 5px 0;
    }

    .cell-label {
        text-align: center;
        font-size: 20px;
        font-weight: 700;
        color: #F1F5F9;
        margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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


def show_organelle(item, image_width=90):
    image_path = IMAGE_DIR / item["image"]

    if image_path.exists():
        st.image(str(image_path), width=image_width)
    else:
        st.caption(f"이미지 없음: {item['image']}")

    st.markdown(
        f"<div class='organelle-name'>{item['name']}</div>",
        unsafe_allow_html=True
    )

    if st.button(
        item["name"] + " 열기",
        key=f"open_{item['name']}",
        use_container_width=True
    ):
        st.switch_page(item["page"])


st.title("Cell Explorer")
st.write("세포를 구성하는 소기관을 탐색하고 각 구조와 기능을 알아보세요.")
st.divider()

# 원형 배치 영역
# 중앙에 세포 전체 이미지, 주변에 9개 소기관을 배치합니다.
orbit_radius = 2
center_col = 4
center_row = 2

grid = []
for row in range(5):
    grid.append(st.columns(9, gap="small"))

# 중앙 세포 이미지
with grid[center_row][center_col]:
    cell_image_path = IMAGE_DIR / "cell.png"

    if cell_image_path.exists():
        st.image(str(cell_image_path), use_container_width=True)
        st.markdown(
            "<div class='cell-label'>세포 전체 구조</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("images/cell.png 파일을 확인해 주세요.")

# 각 소기관의 원형 위치 계산
positions = []
for index, item in enumerate(ORGANELLES):
    angle = -90 + index * (360 / len(ORGANELLES))
    radians = math.radians(angle)

    x = center_col + round(orbit_radius * math.cos(radians))
    y = center_row + round(orbit_radius * math.sin(radians))

    x = max(0, min(8, x))
    y = max(0, min(4, y))

    positions.append((x, y, item))

# 소기관 표시
for x, y, item in positions:
    with grid[y][x]:
        show_organelle(item)

st.divider()
st.caption("소기관을 선택하면 해당 상세 페이지로 이동합니다.")
