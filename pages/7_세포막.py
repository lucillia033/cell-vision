import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 세포막", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_mem" not in st.session_state:
    st.session_state["selected_sub_struct_mem"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "membrane.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/membrane.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("세포막 (Cell Membrane)")
    st.write("세포 내부를 보호하고 물질 출입을 선택적으로 조절하는 유동성 장벽")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 선택적 물질 투과\n• 신호 전달 수용\n• 세포 내부 보호")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포 최외곽 경계")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 인지질 이중층\n• 막단백질\n• 콜레스테롤")

    st.markdown("---")
    
    st.info("""
    **세포막은 왜 중요할까요?**  
    외부 환경으로부터 세포 내부를 독립적으로 보호하는 첫 번째 울타리입니다. 
    필요한 영양분만 선택적으로 받아들이고 노폐물을 배출하여 세포 내부 조건을 일정하게 유지합니다.
    """)

st.markdown("---")

st.subheader("세포막의 주요 구성 요소")
st.write("유동 모자이크 모델에 의해 인지질과 단백질이 자유롭게 이동합니다.")

sub_structures = [
    {
        "key": "phospholipid_bilayer",
        "title": "인지질 이중층",
        "img": "mem_phospholipid.png",
        "desc": "친수성 머리와 소수성 꼬리로 이루어진 2중 장벽입니다.",
        "detail": "수용성 물질의 자유로운 통과를 차단하는 기본 골격 역할을 수행합니다."
    },
    {
        "key": "membrane_protein",
        "title": "막단백질",
        "img": "mem_protein.png",
        "desc": "인지질 사이에 배치되어 통로, 펌프, 수용체 역할을 합니다.",
        "detail": "이온 능동 수송 펌프나 외부 호르몬 인지 수용체 작용을 담당합니다."
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
            if st.session_state["selected_sub_struct_mem"] == item["key"]:
                st.session_state["selected_sub_struct_mem"] = None
            else:
                st.session_state["selected_sub_struct_mem"] = item["key"]

if st.session_state["selected_sub_struct_mem"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_mem"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
