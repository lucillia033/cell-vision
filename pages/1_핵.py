import streamlit as st
import os

st.set_page_config(page_title="핵 탐구", layout="wide")

st.title("핵 (Nucleus)")
st.caption("세포의 유전 정보 저장 및 생명 활동 총괄 제어 센터")

st.markdown("---")

# -----------------------------------------------------------------------------
# 1. 절대 경로 기반 파일 탐색 방식 적용
# -----------------------------------------------------------------------------
col_img, col_info = st.columns([1, 1.2])

# 현재 파일(1_핵.py)의 상위 폴더(프로젝트 루트)를 기준으로 images 폴더 지정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = os.path.join(BASE_DIR, "images", "nucleus.png")

with col_img:
    if os.path.exists(img_path):
        st.image(img_path, caption="핵의 구조 및 핵공 다이어그램", use_container_width=True)
    else:
        st.warning(f"⚠️ 이미지를 찾을 수 없습니다.\n\n탐색 경로: `{img_path}`\n\nGitHub의 `images/` 폴더에 `nucleus.png` 파일이 존재하는지 확인해 주세요.")

with col_info:
    st.subheader("개요 및 중요성")
    st.write("""
    핵은 이중막 구조인 핵막으로 둘러싸여 있으며, 세포의 설계도인 유전 정보(DNA)를 안전하게 보관합니다. 
    핵공을 통해 유전 정보를 담은 mRNA를 세포질로 내보내어 단백질 합성과 모든 생명 활동을 총괄 조절합니다.
    """)

st.markdown("---")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["핵심 기능 & 메커니즘", "세부 구조 심화", "관련 지식 & 질환"])

with tab1:
    st.subheader("유전 정보 전사 및 세포 활동 제어")
    st.markdown("""
    - **DNA 보관 및 보호:** 세포의 모든 유전 정보를 보관합니다.
    - **전사(Transcription) 진행:** DNA 유전 정보를 mRNA로 복제하여 핵공을 통해 세포질로 보냅니다.
    """)

with tab2:
    st.subheader("핵의 세부 구조")
    with st.expander("1. 핵막 및 핵공", expanded=True):
        st.write("2중막 구조이며 핵공 복합체가 물질 출입을 선택적으로 통제합니다.")
    with st.expander("2. 인 (Nucleolus)"):
        st.write("rRNA 합성 및 리보솜 소단위체 조립이 일어납니다.")

with tab3:
    st.subheader("생물학적 지식")
    st.warning("조경증: 라민 단백질 변형으로 핵막 형태가 무너져 조기 노화가 발생하는 질환입니다.")

st.markdown("---")
if st.button("메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
