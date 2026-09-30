import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 미토콘드리아", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_mito" not in st.session_state:
    st.session_state["selected_sub_struct_mito"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "mitochondria.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/mitochondria.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("미토콘드리아 (Mitochondria)")
    st.write("세포 호흡을 통해 에너지 통화인 ATP를 대량 합성하는 세포 발전소")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 세포 호흡 수행\n• ATP 에너지 생산\n• 세포 사멸 조절")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포질 전반\n(에너지 소비가 많은 곳에 다수)")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 이중막 (외막/내막)\n• 크리스타\n• 기질 및 자체 DNA")

    st.markdown("---")
    
    st.info("""
    **미토콘드리아는 왜 중요할까요?**  
    세포가 이동하고, 물질을 합성하며, 생명 활동을 유지하려면 지속적인 에너지가 필요합니다. 
    미토콘드리아는 영양소를 산소와 반응시켜 세포가 즉시 사용할 수 있는 형태인 ATP 에너지를 합성합니다.
    """)

st.markdown("---")

st.subheader("미토콘드리아의 주요 구성 요소")
st.write("미토콘드리아는 특유의 이중막과 내부 주름 구조로 효율적인 호흡을 수행합니다.")

sub_structures = [
    {
        "key": "outer_inner_membrane",
        "title": "외막 및 내막 (Outer & Inner membrane)",
        "img": "mito_membrane.png",
        "desc": "이중막 구조로 완벽한 내부 환경을 유지합니다.",
        "detail": "내막은 선택적 투과성이 매우 높으며 수소 이온 농도 기울기를 형성하는 장벽 역할을 합니다."
    },
    {
        "key": "cristae",
        "title": "크리스타 (Cristae)",
        "img": "mito_cristae.png",
        "desc": "내막이 안쪽으로 접혀 형성된 주름 구조입니다.",
        "detail": "표면적을 극대화하여 전자전달계 단백질 복합체와 ATP 합성효소를 다수 배치합니다."
    },
    {
        "key": "matrix",
        "title": "기질 (Matrix)",
        "img": "mito_matrix.png",
        "desc": "TCA 회로 관련 효소와 자체 DNA가 존재하는 내부 액체입니다.",
        "detail": "피루브산을 산화하여 전자를 추출하는 TCA 회로가 구동되며, 자체 70S 리보솜을 가지고 있습니다."
    }
]

cols = st.columns(3, gap="medium")

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
            if st.session_state["selected_sub_struct_mito"] == item["key"]:
                st.session_state["selected_sub_struct_mito"] = None
            else:
                st.session_state["selected_sub_struct_mito"] = item["key"]

if st.session_state["selected_sub_struct_mito"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_mito"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
