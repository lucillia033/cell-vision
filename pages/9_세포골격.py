import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 세포골격", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_skel" not in st.session_state:
    st.session_state["selected_sub_struct_skel"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "cytoskeleton.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/cytoskeleton.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("세포골격 (Cytoskeleton)")
    st.write("세포의 입체 형태를 유지하고 물질 수송 도로 역할을 하는 단백질 섬유망")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 입체 형태 지지\n• 모터 단백질 이동 레일\n• 세포 분열 및 운동 구동")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포질 전반에 그물망 분포")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 미세관 (가장 굵음)\n• 중간섬유 (중간)\n• 미세섬유 (가장 가늚)")

    st.markdown("---")
    
    st.info("""
    **세포골격은 왜 중요할까요?**  
    세포가 오그라들지 않고 형태를 유지할 수 있게 지지해 주는 내부 뼈대입니다. 
    동시에 소포나 소기관이 도로 위를 달리는 것처럼 이동할 수 있도록 레일을 제공합니다.
    """)

st.markdown("---")

st.subheader("세포골격의 3대 단백질 섬유")
st.write("굵기와 단백질 종류에 따라 미세관, 중간섬유, 미세섬유로 나뉩니다.")

sub_structures = [
    {
        "key": "microtubule",
        "title": "미세관 (Microtubule)",
        "img": "skel_microtubule.png",
        "desc": "튜불린 단백질로 구성된 수송 도로 및 방추사입니다.",
        "detail": "가장 굵은 섬유(25nm)로, 키네신 모터 단백질의 이동 레일 및 방추사 역할을 수행합니다."
    },
    {
        "key": "intermediate_filament",
        "title": "중간섬유 (Intermediate filament)",
        "img": "skel_intermediate.png",
        "desc": "케라틴 등으로 이루어져 소기관 위치를 단단히 고정합니다.",
        "detail": "기계적 강도가 가장 뛰어나 핵막을 지지하고 외력으로부터 형태를 고정합니다."
    },
    {
        "key": "microfilament",
        "title": "미세섬유 (Microfilament)",
        "img": "skel_microfilament.png",
        "desc": "액틴 단백질로 이루어진 세포 수축 및 운동 섬유입니다.",
        "detail": "세포막 바로 밑에 존재하며 수축환 형성 및 아메바 운동을 구동합니다."
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
            if st.session_state["selected_sub_struct_skel"] == item["key"]:
                st.session_state["selected_sub_struct_skel"] = None
            else:
                st.session_state["selected_sub_struct_skel"] = item["key"]

if st.session_state["selected_sub_struct_skel"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_skel"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
