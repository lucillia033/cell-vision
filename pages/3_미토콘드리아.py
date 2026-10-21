
import streamlit as st
import os

st.set_page_config(
    page_title="Cell Explorer - 미토콘드리아",
    page_icon="🔬",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

if "selected_sub_struct_mito" not in st.session_state:
    st.session_state["selected_sub_struct_mito"] = None

# 메인 화면으로 돌아가기
if st.button("← 세포소기관 목록으로", key="back_to_main_mito"):
    st.switch_page("pages/0_메인.py")

st.title("미토콘드리아")
st.caption("Mitochondria · 세포의 에너지 전환 기관")

st.markdown("---")

# 대표 이미지와 핵심 정보
col_left, col_right = st.columns([1, 1.15], gap="large")

with col_left:
    main_img_path = os.path.join(IMAGE_DIR, "mitochondria.png")

    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.warning("대표 이미지 파일을 찾을 수 없습니다: images/mitochondria.png")

    st.caption("미토콘드리아의 전체 구조")

with col_right:
    st.subheader("미토콘드리아란?")
    st.write(
        "미토콘드리아는 세포 호흡에 관여하며, "
        "영양소에서 얻은 에너지를 ATP 형태로 전환하는 세포소기관입니다."
    )

    st.markdown("### 주요 기능")
    st.markdown(
        """
        - 세포 호흡과 ATP 합성
        - 지방산 등 여러 영양소의 대사
        - 세포 내 칼슘 이온 조절
        - 세포 사멸 신호 조절에 관여
        """
    )

    st.markdown("### 위치")
    st.write(
        "대부분의 진핵세포에서 세포질에 분포합니다. "
        "에너지 수요와 세포 종류에 따라 수와 분포가 달라집니다."
    )

    st.markdown("### 주요 구성")
    st.write("외막, 내막, 막 사이 공간, 크리스타, 기질, 미토콘드리아 DNA")

st.markdown("---")

with st.expander("미토콘드리아는 어떻게 ATP를 합성할까요?", expanded=True):
    st.markdown(
        """
        **1. 기질에서 일어나는 반응**

        피루브산 산화와 TCA 회로를 통해 전자를 운반하는 NADH와 FADH₂가 생성됩니다.

        **2. 내막의 전자전달계**

        전자가 전달되는 과정에서 방출되는 에너지를 이용해 수소 이온이 막 사이 공간으로 이동합니다.

        **3. ATP 합성효소의 작용**

        수소 이온이 기질 쪽으로 돌아오면서 ATP 합성효소가 작동하고, ADP와 인산으로부터 ATP가 생성됩니다.
        """
    )

st.markdown("---")

st.subheader("미토콘드리아의 주요 구성 요소")
st.write(
    "아래 구조를 선택하면 해당 부분의 기능과 에너지 생산 과정에서의 역할을 자세히 확인할 수 있습니다."
)

sub_structures = [
    {
        "key": "outer_inner_membrane",
        "title": "외막 및 내막",
        "english": "Outer and Inner Membrane",
        "img": "mito_membrane.png",
        "desc": "미토콘드리아의 내부 환경과 물질 이동을 조절합니다.",
        "detail": """
**외막**
- 미토콘드리아의 바깥 경계를 형성합니다.
- 여러 물질의 이동을 조절하는 단백질을 포함합니다.

**내막**
- 전자전달계와 ATP 합성효소가 위치합니다.
- 수소 이온 농도 기울기를 유지하는 데 중요한 역할을 합니다.
- 이온과 여러 분자의 이동을 선택적으로 조절합니다.
""",
        "connection": "내막의 수소 이온 농도 기울기는 산화적 인산화와 ATP 합성에 필수적입니다."
    },
    {
        "key": "cristae",
        "title": "크리스타",
        "english": "Cristae",
        "img": "mito_cristae.png",
        "desc": "내막이 안쪽으로 접혀 만들어진 주름입니다.",
        "detail": """
- 내막의 표면적을 넓혀 줍니다.
- 전자전달계 단백질과 ATP 합성효소가 작용할 수 있는 공간을 제공합니다.
- 세포의 에너지 수요에 따라 구조와 배열이 달라질 수 있습니다.
""",
        "connection": "크리스타는 내막의 구조적 특징으로, 효율적인 에너지 전환에 기여합니다."
    },
    {
        "key": "matrix",
        "title": "기질",
        "english": "Matrix",
        "img": "mito_matrix.png",
        "desc": "내막 안쪽을 채우며 여러 대사 반응이 일어나는 공간입니다.",
        "detail": """
- 피루브산 산화와 TCA 회로에 필요한 효소가 존재합니다.
- 미토콘드리아 DNA와 RNA가 존재합니다.
- 미토콘드리아 리보솜을 이용한 일부 단백질 합성이 일어납니다.
- 여러 대사 반응을 통해 에너지 전환에 필요한 물질을 공급합니다.
""",
        "connection": "기질에서 생성된 NADH와 FADH₂는 내막의 전자전달계에 전자를 전달합니다."
    }
]

cols = st.columns(3, gap="medium")

for idx, item in enumerate(sub_structures):
    with cols[idx]:
        sub_img_path = os.path.join(IMAGE_DIR, item["img"])

        if os.path.exists(sub_img_path):
            st.image(sub_img_path, use_container_width=True)
        else:
            st.info(f"세부 구조 이미지 준비 중: {item['img']}")

        st.markdown(f"### {item['title']}")
        st.caption(item["english"])
        st.write(item["desc"])

        button_label = (
            "설명 접기 ↑"
            if st.session_state["selected_sub_struct_mito"] == item["key"]
            else "자세히 보기 →"
        )

        if st.button(
            button_label,
            key=f"toggle_{item['key']}",
            use_container_width=True
        ):
            if st.session_state["selected_sub_struct_mito"] == item["key"]:
                st.session_state["selected_sub_struct_mito"] = None
            else:
                st.session_state["selected_sub_struct_mito"] = item["key"]

if st.session_state["selected_sub_struct_mito"]:
    selected_item = next(
        item
        for item in sub_structures
        if item["key"] == st.session_state["selected_sub_struct_mito"]
    )

    st.markdown("---")

    st.subheader(f"{selected_item['title']} 상세 탐구")
    st.caption(selected_item["english"])

    st.markdown(selected_item["detail"])

    st.info(selected_item["connection"])

    if st.button("상세 설명 닫기", key="close_mito_detail"):
        st.session_state["selected_sub_struct_mito"] = None
        st.rerun()

st.markdown("---")

st.subheader("핵심 정리")

st.markdown(
    """
    | 구성 요소 | 핵심 역할 |
    |---|---|
    | 외막 | 미토콘드리아의 바깥 경계를 형성 |
    | 내막 | 전자전달계와 ATP 합성효소가 위치 |
    | 크리스타 | 내막의 표면적을 넓혀 에너지 전환에 기여 |
    | 기질 | 피루브산 산화, TCA 회로 등 여러 대사 반응 수행 |
    """
)

st.caption(
    "참고: 미토콘드리아의 ATP 합성은 기질에서의 대사 반응과 "
    "내막에서의 산화적 인산화가 연결되어 이루어집니다."
)
