import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 골지체", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_golgi" not in st.session_state:
    st.session_state["selected_sub_struct_golgi"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "golgi.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/golgi.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("골지체 (Golgi Apparatus)")
    st.write("단백질과 지질을 최종 가공·분류하여 목적지로 분비하는 우체국")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 당화 수정 및 가공\n• 목적지 주지 표지 부착\n• 분비 소포 포장")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 소포체 주변 및\n세포막 근처")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 시스테르나 층\n• Cis 면 (입구)\n• Trans 면 (출구)")

    st.markdown("---")
    
    st.info("""
    **골지체는 왜 중요할까요?**  
    소포체에서 만들어진 단백질이 필요한 장소(세포 밖, 리소좀, 세포막 등)로 이동하려면 포장과 주소표가 필요합니다. 
    골지체는 최종 물질 가공과 배송지 라벨링을 담당하는 세포 내 물류 포장 센터입니다.
    """)

st.markdown("---")

st.subheader("골지체의 주요 구성 요소")
st.write("골지체는 방향성을 지닌 층층의 시스테르나 구조로 이루어져 있습니다.")

sub_structures = [
    {
        "key": "cis_face",
        "title": "Cis 면 (Cis face)",
        "img": "golgi_cis.png",
        "desc": "소포체에서 유래한 수송 소포를 받아들이는 입구 부위입니다.",
        "detail": "소포체 단백질을 수용하여 초기 수정 가공 층으로 이동시킵니다."
    },
    {
        "key": "cisternae_stack",
        "title": "시스테르나 층 (Cisternae stack)",
        "img": "golgi_cisternae.png",
        "desc": "납작한 막 주머니가 쌓여 있는 중공 가공 공간입니다.",
        "detail": "층마다 존재하는 특이 효소들이 당 사슬을 다듬고 최종 수선을 진행합니다."
    },
    {
        "key": "trans_face",
        "title": "Trans 면 (Trans face)",
        "img": "golgi_trans.png",
        "desc": "가공 완료된 물질을 소포에 담아 방출하는 출구 부위입니다.",
        "detail": "목적지 표지에 따라 분비 소포나 리소좀으로 이동할 소포를 떨구어 냅니다."
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
            if st.session_state["selected_sub_struct_golgi"] == item["key"]:
                st.session_state["selected_sub_struct_golgi"] = None
            else:
                st.session_state["selected_sub_struct_golgi"] = item["key"]

if st.session_state["selected_sub_struct_golgi"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_golgi"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
