
import streamlit as st
from pathlib import Path
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(
    page_title="Cell Vision",
    page_icon="🔬",
    layout="wide"
)

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"

# ---------- 전체 다크 테마 ----------
st.markdown("""
<style>
/* 전체 화면 배경 */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background: radial-gradient(
        ellipse at 50% 40%,
        #10213a 0%,
        #070d18 55%,
        #03060c 100%
    ) !important;
    color: #F4F7FF !important;
}

/* 상단 메뉴 */
[data-testid="stHeader"] {
    background: #050A13 !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

/* 왼쪽 사이드바 */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"] {
    background: #080F1C !important;
    color: #EAF3FF !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] a,
[data-testid="stSidebar"] div {
    color: #EAF3FF !important;
}

/* 페이지 탐색 메뉴 */
[data-testid="stSidebarNav"] {
    background: #080F1C !important;
}

[data-testid="stSidebarNav"] a {
    background: #0D192B !important;
    color: #EAF3FF !important;
    border-radius: 8px !important;
    margin: 4px 0 !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: #1B3150 !important;
    color: #FFFFFF !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #183454 !important;
    border-left: 3px solid #55BFFF !important;
    color: #FFFFFF !important;
}

/* 제목과 본문 */
h1, h2, h3, h4, h5, h6,
p, label, li, small {
    color: #F4F7FF;
}

/* 상단 제목 */
.cv-title {
    text-align: center;
    font-size: clamp(34px, 4vw, 54px);
    font-weight: 300;
    letter-spacing: 5px;
    color: #F4F8FF;
    margin: 0 0 22px 0;
    text-shadow: 0 0 24px #3B82F655;
}

/* 소기관 이름과 영문명 */
.orbit-card {
    text-align: center;
    margin: 7px auto 12px auto;
}

.orbit-label {
    color: #F4F8FF !important;
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    margin-top: 7px;
}

.orbit-en {
    color: #A9BCD5 !important;
    font-size: 11px;
    text-align: center;
}

/* 중앙 세포 이미지 테두리 */
.center-cell {
    border: 1px solid #244D7A;
    border-radius: 50%;
    padding: 8px;
    background: radial-gradient(
        circle,
        #11284688,
        #050B1500 72%
    );
    box-shadow: 0 0 35px #168BFF22;
}

.center-caption {
    text-align: center;
    color: #A9BCD5 !important;
    font-size: 12px;
    letter-spacing: 2px;
    margin-top: 8px;
}

/* 소기관 버튼을 원형으로 만들고 어두운 배경 적용 */
div[data-testid="stButton"] {
    display: flex;
    justify-content: center;
}

div[data-testid="stButton"] > button {
    width: 100px !important;
    min-width: 100px !important;
    max-width: 100px !important;
    height: 100px !important;
    min-height: 100px !important;
    max-height: 100px !important;
    padding: 8px !important;
    margin: 0 auto !important;

    border-radius: 50% !important;
    border: 2px solid #4FBFFF !important;

    background: #0B192B !important;
    color: #F4F8FF !important;

    white-space: normal !important;
    overflow-wrap: anywhere !important;
    line-height: 1.25 !important;
    font-size: 13px !important;
    font-weight: 600 !important;

    box-sizing: border-box !important;
    flex: 0 0 100px !important;

    box-shadow: 0 0 15px #259DFF44 !important;
    transition: all 0.2s ease !important;
}

/* 버튼 내부 텍스트도 흰색 유지 */
div[data-testid="stButton"] > button p,
div[data-testid="stButton"] > button span {
    color: #F4F8FF !important;
}

/* 마우스를 올렸을 때 */
div[data-testid="stButton"] > button:hover {
    background: #193453 !important;
    border-color: #B3E7FF !important;
    color: #FFFFFF !important;
    box-shadow: 0 0 25px #259DFF99 !important;
    transform: scale(1.04);
}

/* 입력창 */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
[data-baseweb="input"] > div {
    background: #101C2D !important;
    color: #F4F8FF !important;
    border-color: #405875 !important;
}

/* 선택 상자 */
[data-baseweb="select"] > div {
    background: #101C2D !important;
    color: #F4F8FF !important;
    border-color: #405875 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"],
[role="option"] {
    background: #101C2D !important;
    color: #F4F8FF !important;
}

[role="option"]:hover {
    background: #254261 !important;
}

/* 안내 상자와 펼침 영역 */
[data-testid="stAlert"],
[data-testid="stExpander"] {
    background: #0D192B !important;
    color: #F4F8FF !important;
    border-color: #304865 !important;
}

/* 구분선과 하단 */
hr {
    border-color: #263B56 !important;
}

footer {
    background: #050A13 !important;
    color: #9EB2CD !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- 제목 ----------
st.markdown(
    '<div class="cv-title">Cell Vision</div>',
    unsafe_allow_html=True
)


# ---------- 소기관 정보 ----------
organelles = {
    "핵": {
        "page": "pages/1_핵.py",
        "image": "nucleus.png",
        "english": "Nucleus"
    },
    "세포골격": {
        "page": "pages/9_세포골격.py",
        "image": "cytoskeleton.png",
        "english": "Cytoskeleton"
    },
    "리보솜": {
        "page": "pages/2_리보솜.py",
        "image": "ribosome.png",
        "english": "Ribosome"
    },
    "미토콘드리아": {
        "page": "pages/3_미토콘드리아.py",
        "image": "mitochondria.png",
        "english": "Mitochondria"
    },
    "소포체": {
        "page": "pages/4_소포체.py",
        "image": "er.png",
        "english": "Endoplasmic Reticulum"
    },
    "골지체": {
        "page": "pages/5_골지체.py",
        "image": "golgi.png",
        "english": "Golgi Apparatus"
    },
    "리소좀": {
        "page": "pages/6_리소좀.py",
        "image": "lysosome.png",
        "english": "Lysosome"
    },
    "세포막": {
        "page": "pages/7_세포막.py",
        "image": "membrane.png",
        "english": "Cell Membrane"
    },
    "세포질": {
        "page": "pages/8_세포질.py",
        "image": "cytosol.png",
        "english": "Cytoplasm"
    }
}


# ---------- 소기관 표시 함수 ----------
def show_organelle(name):
    item = organelles[name]
    image_path = IMG / item["image"]

    st.markdown(
        '<div class="orbit-card">',
        unsafe_allow_html=True
    )

    # 소기관 이미지
    if image_path.is_file():
        try:
            with Image.open(image_path) as original:
                original.load()
                icon_image = original.convert("RGBA")
                icon_image.thumbnail(
                    (150, 150),
                    Image.Resampling.LANCZOS
                )

            buffer = BytesIO()
            icon_image.save(buffer, format="PNG")

            encoded = base64.b64encode(
                buffer.getvalue()
            ).decode("utf-8")

            st.markdown(
                f"""
                <img
                    src="data:image/png;base64,{encoded}"
                    alt="{name}"
                    style="
                        width:78px;
                        height:78px;
                        object-fit:contain;
                        border-radius:50%;
                        padding:7px;
                        background:#10213A;
                        border:2px solid #55BFFF;
                        box-shadow:0 0 14px #36AAFF88;
                    "
                >
                """,
                unsafe_allow_html=True
            )
        except Exception:
            st.markdown(
                '<div style="height:78px;"></div>',
                unsafe_allow_html=True
            )
    else:
        st.markdown(
            '<div style="height:78px;"></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="orbit-label">{name}</div>'
        f'<div class="orbit-en">{item["english"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # 어두운 원형 버튼을 눌러 상세 페이지로 이동
    if st.button(
        f"{name} 탐구",
        key=f"open_{name}",
        help=f"{name} 상세 페이지로 이동"
    ):
        st.switch_page(item["page"])


# ---------- 위쪽 소기관 ----------
top1, top2, top3, top4, top5 = st.columns(5)

with top1:
    show_organelle("세포골격")

with top3:
    show_organelle("핵")

with top5:
    show_organelle("리보솜")


# ---------- 중앙 세포와 양옆 소기관 ----------
left, center, right = st.columns(
    [1.15, 2.7, 1.15],
    gap="medium",
    vertical_alignment="center"
)

with left:
    show_organelle("세포질")
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    show_organelle("세포막")

with center:
    cell_path = IMG / "cell.png"

    if cell_path.is_file():
        try:
            with Image.open(cell_path) as original:
                original.load()
                cell_image = original.convert("RGBA")

            # 원본 비율을 유지하고 전체 이미지가 들어가도록 축소
            cell_image.thumbnail(
                (650, 650),
                Image.Resampling.LANCZOS
            )

            st.markdown(
                '<div class="center-cell">',
                unsafe_allow_html=True
            )

            st.image(
                cell_image,
                use_container_width=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown(
                '<div class="center-caption">'
                'EXPLORE THE CELL'
                '</div>',
                unsafe_allow_html=True
            )

        except Exception as error:
            st.error(
                f"세포 이미지를 불러오지 못했습니다: {error}"
            )
    else:
        st.warning(
            "전체 세포 그림이 없습니다. "
            "images/cell.png 파일을 추가해 주세요."
        )

with right:
    show_organelle("미토콘드리아")
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    show_organelle("소포체")


# ---------- 아래쪽 소기관 ----------
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

bottom1, bottom2, bottom3, bottom4, bottom5 = st.columns(5)

with bottom2:
    show_organelle("리소좀")

with bottom4:
    show_organelle("골지체")


# ---------- 하단 문구 ----------
st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#9EB2CD;
        font-size:11px;
        letter-spacing:2px;
    ">
        CELL STRUCTURE · INTERACTIVE BIOLOGY
    </div>
    """,
    unsafe_allow_html=True
)
