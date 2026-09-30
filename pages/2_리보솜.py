import streamlit as st
import os

st.set_page_config(page_title="Cell Explorer - 리보솜", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "selected_sub_struct_ribo" not in st.session_state:
    st.session_state["selected_sub_struct_ribo"] = None

if st.button("← 세포소기관 목록으로"):
    st.switch_page("pages/0_메인.py")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    main_img_path = os.path.join(BASE_DIR, "images", "ribosome.png")
    if os.path.exists(main_img_path):
        st.image(main_img_path, use_container_width=True)
    else:
        st.info("images/ribosome.png 대표 이미지를 등록해 주세요.")
    st.caption("각 세부 구조를 클릭하면 자세한 설명을 볼 수 있습니다.")

with col_right:
    st.title("리보솜 (Ribosome)")
    st.write("mRNA 유전 정보를 해독하여 아미노산을 연결하는 단백질 제조 공장")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 주요 기능")
        st.caption("• 유전 코드 해독\n• 펩타이드 결합 형성\n• 단백질 폴리펩타이드 합성")
    with c2:
        st.markdown("#### 위치")
        st.caption("• 세포질 유리 상태\n• 거친소포체 표면 부착")
    with c3:
        st.markdown("#### 주요 구성 요소")
        st.caption("• 대단위체\n• 소단위체\n• rRNA 및 단백질")

    st.markdown("---")
    
    st.info("""
    **리보솜은 왜 중요할까요?**  
    세포가 살아가는 데 필요한 대부분의 구조물과 효소는 단백질로 이루어져 있습니다. 
    리보솜은 핵에서 전달된 설계도(mRNA)를 실제로 읽어 아미노산을 조합하여 생명체에 필요한 단백질을 직접 생산합니다.
    """)

st.markdown("---")

st.subheader("리보솜의 주요 구성 요소")
st.write("리보솜은 대단위체와 소단위체가 결합하여 번역 작용을 수행합니다.")

sub_structures = [
    {
        "key": "large_subunit",
        "title": "대단위체 (Large subunit)",
        "img": "ribosome_large.png",
        "desc": "아미노산 사이의 펩타이드 결합을 직접 연결하는 촉매 작용을 합니다.",
        "detail": "A자리, P자리, E자리를 포함하며, 펩타이드 전달효소 활성을 가진 rRNA가 존재합니다."
    },
    {
        "key": "small_subunit",
        "title": "소단위체 (Small subunit)",
        "img": "ribosome_small.png",
        "desc": "mRNA 유전 정보 서열을 직접 결합하여 유전 코드를 읽어냅니다.",
        "detail": "mRNA의 개시 코돈을 인지하고 tRNA의 안티코돈과 상보성을 검증하는 부위입니다."
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
            if st.session_state["selected_sub_struct_ribo"] == item["key"]:
                st.session_state["selected_sub_struct_ribo"] = None
            else:
                st.session_state["selected_sub_struct_ribo"] = item["key"]

if st.session_state["selected_sub_struct_ribo"]:
    selected_item = next(i for i in sub_structures if i["key"] == st.session_state["selected_sub_struct_ribo"])
    st.success(f"**{selected_item['title']} 상세 정보:** {selected_item['detail']}")
