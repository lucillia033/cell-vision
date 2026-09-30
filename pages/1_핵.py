import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 핵", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct" not in st.session_state:
    st.session_state["selected_sub_struct"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "nucleus.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/nucleus.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("핵 (Nucleus)")
    st.write("세포의 유전 정보를 저장하고 세포의 활동을 조절하는 핵심 제어 센터")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 유전 정보 저장 및 보호\n• 세포 활동 조절\n• 단백질 합성 조절")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포질 내\n(진핵세포에서만 존재)")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 핵막\n• 핵공\n• 염색질\n• 인")

    st.markdown("---")
    
    st.info("""
    **핵은 왜 중요할까요?**  
    핵은 세포의 설계도인 DNA를 보관하고, 세포가 언제 어떤 일을 할지 지시하는 역할을 합니다. 
    단순히 정보를 저장하는 것뿐만 아니라 세포의 성장, 분열, 대사 등 모든 활동을 조절하는 컨트롤 센터와 같습니다.
    """)

st.markdown("---")

st.subheader("핵의 주요 구성 요소")
st.write("핵은 여러 구조가 유기적으로 작용하여 세포의 유전 정보를 관리합니다.")

sub_structures = [
    {
        "key": "nuclear_envelope",
        "title": "핵막 (Nuclear envelope)",
        "img": "nuclear_envelope.png",
        "desc": "핵을 둘러싸고 있는 이중막 구조로, 세포질과 핵을 구분합니다.",
        "detail": "내막과 외막의 2중막 구조이며, 외막은 소포체막과 연속적으로 이어져 있습니다."
    },
    {
        "key": "nuclear_pore",
        "title": "핵공 (Nuclear pore)",
        "img": "nuclear_pore.png",
        "desc": "핵막에 있는 구멍으로, 단백질, RNA 등 필요한 물질이 이동하는 통로입니다.",
        "detail": "핵공 복합체(NPC)가 수백 개의 단백질로 구성되어 물질의 선택적 수송을 엄격히 통제합니다."
    },
    {
        "key": "chromatin",
        "title": "염색질 (Chromatin)",
        "img": "chromatin.png",
        "desc": "DNA와 단백질이 결합한 구조로, 유전 정보를 저장합니다.",
        "detail": "세포 분열 시 고도로 응축되어 염색체가 되며, 유전자 발현 양상을 조절합니다."
    },
    {
        "key": "nucleolus",
        "title": "인 (Nucleolus)",
        "img": "nucleolus.png",
        "desc": "리보솜의 조립이 이루어지는 곳으로, 리보솜 RNA를 생성합니다.",
        "detail": "막이 없는 고농도 영역으로, rRNA의 전사 및 리보솜 소단위체 조립이 집중적으로 수행됩니다."
    }
]

cols = st.columns(4, gap="medium")

for idx, item in enumerate(sub_structures):
    with cols[idx]:
        sub_img_path = os.path.join(BASE_DIR, "images", item["img"])
        if os.path.exists(sub_img_path):
            st.image(sub_img_path, use_container_width=True)
        else:
            st.info(f"images/{item['img']}")
            
        st.markdown(f"**{item['title']}**")
        st.caption(item["desc"])
        
        if st.button("자세히 보기 →", key=item["key"], use_container_width=True):
            if st.session_state["selected_sub_struct"] == item["key"]:
                st.session_state["selected_sub_struct"] = None
            else:
                st.session_state["selected_sub_struct"] = item["key"]

if st.session_state["selected_sub_struct"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
