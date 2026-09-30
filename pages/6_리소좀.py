import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 리소좀", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_lyso" not in st.session_state:
    st.session_state["selected_sub_struct_lyso"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "lysosome.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/lysosome.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("리소좀 (Lysosome)")
    st.write("가수분해 효소로 손상된 부품과 외부 물질을 소화하는 재활용 센터")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 이물질 분해 소화\n• 손상 소기관 자가포식\n• 세포 자살 유도")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포질 전반에 분포")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 단일막 주머니\n• 가수분해 효소\n• 수소 이온 펌프")

    st.markdown("---")
    
    st.info("""
    **리소좀은 왜 중요할까요?**  
    세포 내 노폐물이나 외부 세균이 처리되지 못하면 세포 기능이 마비됩니다. 
    리소좀은 세균을 파괴하고 수명이 다한 소기관을 분해하여 다시 유용한 영양소 원료로 재활용합니다.
    """)

st.markdown("---")

st.subheader("리소좀의 주요 구성 요소")
st.write("강력한 내부 효소가 세포 자체를 파괴하지 못하도록 막으로 안전하게 차단되어 있습니다.")

sub_structures = [
    {
        "key": "single_membrane",
        "title": "단일막 및 수소 펌프",
        "img": "lyso_membrane.png",
        "desc": "효소의 외부 유출을 차단하며 내부를 산성으로 유지합니다.",
        "detail": "V-ATPase 펌프를 가동하여 H+ 이온을 집어넣어 내부 pH 4.5~5.0 환경을 형성합니다."
    },
    {
        "key": "acid_hydrolases",
        "title": "가수분해 효소군",
        "img": "lyso_enzymes.png",
        "desc": "단백질, 지질, 핵산, 다당류를 분해하는 50여 가지 효소입니다.",
        "detail": "산성 상태에서만 활성화되므로 혹시 막이 찢어져 유출되어도 중성 세포질에서는 활성을 잃습니다."
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
            if st.session_state["selected_sub_struct_lyso"] == item["key"]:
                st.session_state["selected_sub_struct_lyso"] = None
            else:
                st.session_state["selected_sub_struct_lyso"] = item["key"]

if st.session_state["selected_sub_struct_lyso"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_lyso"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
