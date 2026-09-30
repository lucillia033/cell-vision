import streamlit as st
import os

st.set_page_config(page_title="핵 탐구", layout="wide")

st.title("핵 (Nucleus)")
st.caption("진핵세포의 유전 정보 저장, 전사 및 세포 생명 활동 총괄 제어 센터")

st.markdown("---")

# 이미지 로딩 (절대 경로 기반 탐색)
col_img, col_info = st.columns([1, 1.2])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = os.path.join(BASE_DIR, "images", "nucleus.png")

with col_img:
    if os.path.exists(img_path):
        st.image(img_path, caption="핵의 이중막 구조, 핵공 복합체 및 인", use_container_width=True)
    else:
        st.warning(f"이미지 파일(`images/nucleus.png`)을 찾을 수 없습니다.")

with col_info:
    st.subheader("개요 및 생물학적 중요성")
    st.write("""
    핵은 진핵세포를 원핵세포와 구별 짓는 가장 핵심적인 소기관입니다. 
    세포의 모든 유전 설계도인 DNA를 보관하며, 전사(Transcription) 과정을 통해 유전 정보를 mRNA로 복제하여 세포 전체의 단백질 합성 및 대사 과정을 총괄 제어합니다.
    """)

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["핵심 기능 & 메커니즘", "세부 구조 심화", "관련 지식 & 질환"])

with tab1:
    st.subheader("유전 정보의 발현 및 제어 메커니즘")
    st.markdown("""
    - **유전 정보의 보관 및 복제:** DNA 이중 가닥 형태로 유전 정보를 안전하게 유지하며, 세포 분열 전 정확히 복제합니다.
    - **전사(Transcription) 조절:** RNA 포식효소가 DNA 가닥을 읽어 mRNA를 합성하며, 다양한 전사 인자가 유전자 발현 시기와 양을 조절합니다.
    - **핵-세포질 물질 수송:** 핵공 복합체(NPC)를 통해 합성된 RNA는 세포질로 내보내고, 단백질(전사 인자, 히스톤 등)은 핵 내부로 선택적 수용합니다.
    """)

with tab2:
    st.subheader("핵의 세부 정밀 구조")
    with st.expander("1. 핵막(Nuclear Envelope) 및 핵공 복합체(NPC)", expanded=True):
        st.write("내막과 외막의 이중막 구조로 이루어져 있으며, 외막은 소포체 막과 직접 연결되어 있습니다. 핵공 복합체는 수백 개의 단백질로 구성되어 수용성 분자와 고분자 물질의 출입을 가이딩합니다.")
    with st.expander("2. 인(Nucleolus)"):
        st.write("막이 없는 고밀도 영역으로, 리보솜 RNA(rRNA)의 전사 및 가공, 그리고 리보솜 대/소단위체의 조립이 집중적으로 일어나는 장소입니다.")
    with st.expander("3. 염색질(Chromatin)"):
        st.write("DNA가 히스톤 단백질을 감싼 뉴클레오솜 구조입니다. 유전자 발현이 활발한 진정염색질(Euchromatin)과 고도로 응축되어 억제된 이질염색질(Heterochromatin)로 구분됩니다.")

with tab3:
    st.subheader("생물학적 중요 지식 및 질환")
    st.warning("""
    - **조경증(Progeria):** 핵막 내측의 구조를 지지하는 라민(Lamin A) 단백질 변형으로 인해 핵막 형태가 무너지고 조기 노화가 유발되는 유전 질환입니다.
    - **무핵 세포:** 포유류의 성숙한 적혈구는 산소 운반 효율을 극대화하기 위해 발달 과정에서 핵을 퇴화시킵니다.
    """)

st.markdown("---")
if st.button("메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
