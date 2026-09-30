import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 세포질", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_cyto" not in st.session_state:
    st.session_state["selected_sub_struct_cyto"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "cytosol.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/cytosol.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("세포질 (Cytoplasm / Cytosol)")
    st.write("소기관이 배치되고 초기 대사 반응이 진행되는 점성 매질")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 해당작용 수행\n• 소기관 지지 및 보호\n• 세포질 유동 영양 수송")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 핵 제외 세포막 내부 전체")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 세포액 (Cytosol)\n• 가용성 효소\n• 이온 및 수분")

    st.markdown("---")
    
    st.info("""
    **세포질은 왜 중요할까요?**  
    세포 내 모든 소기관들이 작동할 수 있는 바탕 환경입니다. 
    포도당을 초기에 분해하는 해당작용이 일어나며 영양분과 이온이 이동하는 수송로입니다.
    """)

st.markdown("---")

st.subheader("세포질의 주요 구성 요소")
st.write("세포액과 분해 효소가 균일하게 섞여 있는 유동성 상태입니다.")

sub_structures = [
    {
        "key": "cytosol_liquid",
        "title": "세포액 (Cytosol)",
        "img": "cyto_liquid.png",
        "desc": "물과 이온, 효소가 고농도로 용해된 점성 액체입니다.",
        "detail": "약 70~80%의 수분과 칼륨 이온, 아미노산이 포함되어 있습니다."
    },
    {
        "key": "cytoplasmic_streaming",
        "title": "세포질 유동 현상",
        "img": "cyto_stream.png",
        "desc": "세포질이 한 방향으로 흐르며 물질을 수송합니다.",
        "detail": "미세섬유 수축에 의해 액체가 움직여 물질 순환을 촉진시킵니다."
    }
]

cols = st.columns(2, gap="medium")

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
            if st.session_state["selected_sub_struct_cyto"] == item["key"]:
                st.session_state["selected_sub_struct_cyto"] = None
            else:
                st.session_state["selected_sub_struct_cyto"] = item["key"]

if st.session_state["selected_sub_struct_cyto"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_cyto"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
