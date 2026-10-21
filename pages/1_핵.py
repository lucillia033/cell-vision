
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Explorer - 핵",
    page_icon="🔬",
    layout="wide"
)

ROOT_DIR = Path(__file__).resolve().parent.parent

# 세부 구조 선택 상태
if "selected_sub_struct" not in st.session_state:
    st.session_state["selected_sub_struct"] = None

# 어두운 테마
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

# 상단 이동 버튼
if st.button("← 세포소기관 목록으로"):
    st.switch_page("app.py")

st.markdown("# 핵 (Nucleus)")
st.caption("유전 정보를 보관하고 유전자 발현을 조절하는 세포의 핵심 구조")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = ROOT_DIR / "images" / "nucleus.png"

    if main_img_path.exists():
        st.image(str(main_img_path), use_container_width=True)
        st.caption("핵의 대표 이미지")
    else:
        st.info(
            "대표 이미지를 준비 중입니다. "
            "`images/nucleus.png` 파일을 확인해 주세요."
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
                DNA 보관<br>
                유전자 발현 조절<br>
                세포 활동 조절에 관여
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
                진핵세포 내부<br>
                일반적으로 세포질 안에 위치
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
            핵막 · 핵공 · 염색질 · 인
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">
            <h4>핵은 왜 중요할까요?</h4>
            <p>
            핵은 DNA에 저장된 유전 정보를 바탕으로 RNA가 만들어지는
            과정인 전사 등을 조절합니다. 이를 통해 세포에서 필요한
            단백질이 만들어지는 과정과 세포의 성장 및 분화에 영향을 줍니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("## 핵의 주요 구성 요소")
st.write(
    "아래 항목을 선택하면 각 구조의 특징과 기능을 확인할 수 있습니다. "
    "세부 구조는 개별 이미지 없이 텍스트로 설명합니다."
)

sub_structures = [
    {
        "key": "nuclear_envelope",
        "title": "핵막 (Nuclear envelope)",
        "desc": "핵 내부와 세포질을 구분하는 이중막 구조",
        "function": (
            "핵의 내부 환경을 세포질과 구분하고 유전 물질을 보호합니다. "
            "핵막은 내막과 외막으로 이루어져 있으며, 외막은 "
            "소포체막과 연속적으로 이어져 있습니다."
        ),
        "detail": (
            "핵막 사이에는 막간 공간이 존재합니다. 핵막은 핵 내부와 "
            "세포질 사이의 물질 이동을 조절하는 핵공 복합체를 포함합니다. "
            "핵막은 세포 분열 과정에서 분해되었다가 다시 형성될 수 있습니다."
        ),
        "importance": (
            "DNA가 위치한 핵 내부 환경을 유지하고, 핵과 세포질 사이의 "
            "물질 교환이 적절하게 이루어지도록 돕습니다."
        )
    },
    {
        "key": "nuclear_pore",
        "title": "핵공 (Nuclear pore)",
        "desc": "핵막을 통과하는 물질의 이동을 조절하는 통로",
        "function": (
            "핵공 복합체는 RNA와 단백질 등 다양한 물질이 핵과 세포질 "
            "사이를 오갈 수 있도록 합니다. 작은 분자는 비교적 쉽게 "
            "통과할 수 있지만, 큰 분자의 이동은 선택적으로 조절됩니다."
        ),
        "detail": (
            "핵공은 단순히 뚫려 있는 구멍이 아니라 여러 단백질로 "
            "구성된 복합체입니다. 예를 들어, 핵에서 만들어진 mRNA는 "
            "세포질로 이동하고, 핵에서 작용하는 일부 단백질은 핵 안으로 "
            "수송됩니다."
        ),
        "importance": (
            "유전 정보의 전달과 핵 내부에서 일어나는 반응이 원활하게 "
            "이루어지도록 물질의 이동을 조절합니다."
        )
    },
    {
        "key": "chromatin",
        "title": "염색질 (Chromatin)",
        "desc": "DNA와 단백질이 결합하여 이루어진 유전 물질",
        "function": (
            "유전 정보를 저장하고 DNA가 핵 안에 효율적으로 정리되도록 "
            "합니다. 염색질의 포장 상태는 유전자 발현에도 영향을 줍니다."
        ),
        "detail": (
            "염색질은 DNA가 히스톤 등의 단백질과 결합한 구조입니다. "
            "일반적으로 비교적 느슨한 염색질 영역에서는 유전자 발현이 "
            "활발할 가능성이 높고, 응축된 영역에서는 발현이 제한될 "
            "가능성이 높습니다. 세포 분열 시에는 염색질이 더욱 응축되어 "
            "염색체를 형성합니다."
        ),
        "importance": (
            "DNA를 보호하고 필요한 유전 정보를 적절한 시점에 사용할 수 "
            "있도록 조절하는 데 중요합니다."
        )
    },
    {
        "key": "nucleolus",
        "title": "인 (Nucleolus)",
        "desc": "리보솜 구성 요소의 생산과 조립이 이루어지는 영역",
        "function": (
            "리보솜 RNA(rRNA)의 합성과 가공, 리보솜 소단위체 조립에 "
            "중요한 역할을 합니다."
        ),
        "detail": (
            "인은 핵 내부에 존재하지만 별도의 막으로 둘러싸여 있지는 "
            "않습니다. 인에서 만들어지고 조립된 리보솜 소단위체는 "
            "핵공을 거쳐 세포질로 이동한 뒤 단백질 합성에 참여합니다."
        ),
        "importance": (
            "단백질 합성에 필요한 리보솜이 만들어지는 과정에 관여하므로, "
            "세포의 단백질 생산 능력과 밀접한 관련이 있습니다."
        )
    }
]

for item in sub_structures:
    with st.container(border=True):
        st.markdown(f"### {item['title']}")
        st.write(item["desc"])

        if st.button(
            "상세 정보 보기" if st.session_state["selected_sub_struct"] != item["key"]
            else "상세 정보 접기",
            key=f"toggle_{item['key']}",
            use_container_width=True
        ):
            if st.session_state["selected_sub_struct"] == item["key"]:
                st.session_state["selected_sub_struct"] = None
            else:
                st.session_state["selected_sub_struct"] = item["key"]

        if st.session_state["selected_sub_struct"] == item["key"]:
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

st.markdown("## 핵심 개념 정리")

st.markdown(
    """
    - **DNA와 RNA:** DNA는 유전 정보를 저장하고, RNA는 유전 정보의 발현과 전달에 관여합니다.
    - **전사:** DNA의 유전 정보를 바탕으로 RNA를 합성하는 과정입니다.
    - **유전자 발현:** 유전 정보가 RNA나 단백질 등의 기능적 산물로 이어지는 과정입니다.
    - **핵과 리보솜의 연결:** 핵에서 만들어진 mRNA는 핵공을 통해 세포질로 이동하여 단백질 합성에 이용됩니다.
    """
)
