
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Explorer - 리보솜",
    page_icon="🔬",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent.parent

if "selected_sub_struct_ribo" not in st.session_state:
    st.session_state["selected_sub_struct_ribo"] = None

# 어두운 테마: 핵 페이지와 통일
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

    h1, h2, h3, h4, p, label,
    [data-testid="stMarkdownContainer"] {
        color: #F1F5F9;
    }

    [data-testid="stCaptionContainer"] {
        color: #B8C5D1;
    }

    [data-testid="stAlert"] {
        background-color: #1C2B38;
        color: #F1F5F9;
        border: 1px solid #34495A;
        border-radius: 12px;
    }

    div.stButton > button {
        background-color: #243746;
        color: #F1F5F9;
        border: 1px solid #405568;
        border-radius: 10px;
    }

    div.stButton > button:hover {
        background-color: #344D60;
        color: #FFFFFF;
        border-color: #7C9BB5;
    }

    hr {
        border-color: #34495A;
    }

    .info-card {
        background-color: #1A2834;
        border: 1px solid #34495A;
        border-radius: 12px;
        padding: 16px;
        height: 100%;
        margin-bottom: 10px;
    }

    .info-card h4 {
        color: #A9D6F5;
        margin-top: 0;
    }

    .info-card p {
        color: #E2E8F0;
        margin-bottom: 0;
        line-height: 1.7;
    }

    .detail-card {
        background-color: #1A2834;
        border-left: 4px solid #78A9CC;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 10px 0;
    }

    .detail-card h4 {
        color: #A9D6F5;
        margin-top: 0;
    }

    .detail-card p {
        color: #E2E8F0;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 메인 화면으로 돌아가기
if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

st.markdown("# 리보솜 (Ribosome)")
st.caption("mRNA의 유전 정보를 해독하여 단백질을 합성하는 세포 내 구조")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = ROOT_DIR / "images" / "ribosome.png"

    if main_img_path.exists():
        st.image(str(main_img_path), use_container_width=True)
        st.caption("리보솜 대표 이미지")
    else:
        st.info(
            "대표 이미지를 준비 중입니다. "
            "`images/ribosome.png` 파일을 확인해 주세요."
        )

with col_right:
    st.markdown("### 핵심 정보")

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown(
            """
            <div class="info-card">
                <h4>주요 기능</h4>
                <p>
                mRNA 해독<br>
                펩타이드 결합 형성<br>
                단백질 합성
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="info-card">
                <h4>존재 위치</h4>
                <p>
                세포질에 자유롭게 존재<br>
                거친면소포체 표면에 부착
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="info-card">
            <h4>주요 구성 요소</h4>
            <p>
            대단위체 · 소단위체 · rRNA · 리보솜 단백질
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">
            <h4>리보솜은 왜 중요할까요?</h4>
            <p>
            단백질은 효소, 세포 구조물, 신호 전달 물질 등 다양한 역할을 합니다.
            리보솜은 mRNA의 정보를 읽고 tRNA가 운반한 아미노산을 연결하여
            단백질 합성에 필요한 폴리펩타이드 사슬을 만듭니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("## 리보솜의 주요 구성 요소")
st.write(
    "리보솜은 대단위체와 소단위체가 협력하여 번역을 수행합니다. "
    "각 항목을 선택하면 구조와 작동 원리를 확인할 수 있습니다."
)

sub_structures = [
    {
        "key": "large_subunit",
        "title": "대단위체 (Large subunit)",
        "desc": "아미노산 사이의 펩타이드 결합 형성에 관여합니다.",
        "function": (
            "대단위체는 성장 중인 폴리펩타이드 사슬에 새로운 아미노산이 "
            "연결되도록 합니다. 펩타이드 결합 형성의 촉매 중심은 "
            "리보솜 RNA(rRNA)에 있습니다."
        ),
        "detail": (
            "리보솜의 A자리에는 새로운 아미노산을 운반한 tRNA가 들어오고, "
            "P자리에는 성장 중인 폴리펩타이드 사슬을 가진 tRNA가 위치합니다. "
            "E자리는 아미노산을 전달한 tRNA가 리보솜을 떠나는 통로 역할을 합니다. "
            "이 세 자리는 번역 과정에서 서로 협력합니다."
        ),
        "importance": (
            "아미노산을 올바른 순서로 연결하여 단백질의 기본 골격인 "
            "폴리펩타이드 사슬을 형성하는 데 중요합니다."
        )
    },
    {
        "key": "small_subunit",
        "title": "소단위체 (Small subunit)",
        "desc": "mRNA를 읽고 유전 정보와 tRNA 사이의 대응을 확인합니다.",
        "function": (
            "소단위체는 mRNA와 결합하고 코돈을 읽는 과정에 관여합니다. "
            "tRNA의 안티코돈이 mRNA의 코돈과 상보적으로 결합하는지 "
            "확인하는 데 중요한 역할을 합니다."
        ),
        "detail": (
            "mRNA의 코돈은 일반적으로 세 개의 염기로 이루어집니다. "
            "각 코돈은 특정 아미노산이나 번역 종료 신호를 지정합니다. "
            "번역은 개시 과정에서 시작 코돈을 인식하면서 시작되고, "
            "리보솜은 mRNA를 따라 이동하며 유전 정보를 해독합니다."
        ),
        "importance": (
            "mRNA의 염기서열이 단백질의 아미노산 서열로 정확하게 "
            "전달되도록 하는 데 중요합니다."
        )
    }
]

for item in sub_structures:
    with st.container(border=True):
        st.markdown(f"### {item['title']}")
        st.write(item["desc"])

        button_label = (
            "상세 정보 접기"
            if st.session_state["selected_sub_struct_ribo"] == item["key"]
            else "상세 정보 보기"
        )

        if st.button(
            button_label,
            key=f"toggle_{item['key']}",
            use_container_width=True
        ):
            if st.session_state["selected_sub_struct_ribo"] == item["key"]:
                st.session_state["selected_sub_struct_ribo"] = None
            else:
                st.session_state["selected_sub_struct_ribo"] = item["key"]

        if st.session_state["selected_sub_struct_ribo"] == item["key"]:
            st.markdown(
                f"""
                <div class="detail-card">
                    <h4>주요 기능</h4>
                    <p>{item['function']}</p>
                    <h4>구조와 작동 원리</h4>
                    <p>{item['detail']}</p>
                    <h4>생물학적 중요성</h4>
                    <p>{item['importance']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

st.markdown("## 단백질 합성 과정")

steps = [
    (
        "1. 개시",
        "리보솜이 mRNA와 결합하고 시작 코돈을 인식하여 번역을 시작합니다."
    ),
    (
        "2. 신장",
        "tRNA가 코돈에 대응하는 아미노산을 운반하고, 리보솜이 아미노산을 연결합니다."
    ),
    (
        "3. 종결",
        "종결 코돈에 도달하면 번역이 끝나고 폴리펩타이드 사슬이 방출됩니다."
    )
]

for title, description in steps:
    st.markdown(
        f"""
        <div class="detail-card">
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("## 핵심 개념 정리")

st.markdown(
    """
    - **번역:** mRNA의 유전 정보를 바탕으로 아미노산 서열을 합성하는 과정입니다.
    - **코돈:** mRNA에서 일반적으로 세 개의 염기로 이루어진 단위로, 아미노산이나 종결 신호를 지정합니다.
    - **안티코돈:** tRNA에 있는 염기서열로, mRNA의 코돈과 상보적으로 결합합니다.
    - **rRNA:** 리보솜의 구조를 이루며 단백질 합성 과정의 촉매 작용에도 관여합니다.
    - **자유 리보솜과 부착 리보솜:** 두 리보솜은 기본적인 단백질 합성 기능을 공유하지만, 만들어지는 단백질의 목적지와 경로에 차이가 있을 수 있습니다.
    """
)
