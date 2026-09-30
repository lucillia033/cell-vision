import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 소포체", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_er" not in st.session_state:
    st.session_state["selected_sub_struct_er"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "er.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/er.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("소포체 (Endoplasmic Reticulum)")
    st.write("단백질과 지질의 합성, 당화 가공 및 세포 내 이동 경로")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 단백질 변형 및 접힘\n• 지질 및 스테로이드 합성\n• 칼슘 이온 저장")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 핵막 외막과 연결되어\n세포질 전반으로 확장")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 거친소포체\n• 매끈소포체\n• 소포체 내강")

    st.markdown("---")
    
    st.info("""
    **소포체는 왜 중요할까요?**  
    리보솜이 만든 단백질은 그대로 사용할 수 없고 입체 구조로 접히는 가공 과정이 필요합니다. 
    소포체는 단백질을 올바르게 접어주고, 세포막을 구성하는 지질을 만드는 가공소이자 도로망입니다.
    """)

st.markdown("---")

st.subheader("소포체의 주요 구성 요소")
st.write("소포체는 표면 리보솜 부착 여부에 따라 거친소포체와 매끈소포체로 구분됩니다.")

sub_structures = [
    {
        "key": "rough_er",
        "title": "거친소포체 (Rough ER)",
        "img": "er_rough.png",
        "desc": "표면에 리보솜이 부착되어 있어 단백질 가공을 담당합니다.",
        "detail": "합성된 단백질을 내강으로 받아들여 입체 구조 접힘과 초기 N-당화 가공을 진행합니다."
    },
    {
        "key": "smooth_er",
        "title": "매끈소포체 (Smooth ER)",
        "img": "er_smooth.png",
        "desc": "리보솜이 없는 관 모양으로 지질 합성 및 해독을 담당합니다.",
        "detail": "인지질 및 스테로이드 호르몬을 제작하고, 독성 물질 해독과 칼슘 이온을 저장합니다."
    }
]

cols = st.columns(2, gap="medium")

for idx, item in enumerate(sub_structures):
    with cols[idx]:
        sub_img_path = os.path.join(BASE_DIR, "images", item["img"])
        if os.path.exists(sub_img_path):
            st.image(sub_img_path, use_container_width=True)
        else:
            st.info(f"images/{item['item'] if 'item' in item else item['img']}")
            
        st.markdown(f"**{item['title']}**")
        st.caption(item["desc"])
        
        if st.button("자세히 보기 →", key=item["key"], use_container_width=True):
            if st.session_state["selected_sub_struct_er"] == item["key"]:
                st.session_state["selected_sub_struct_er"] = None
            else:
                st.session_state["selected_sub_struct_er"] = item["key"]

if st.session_state["selected_sub_struct_er"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_er"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
