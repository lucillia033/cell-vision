import streamlit as st

st.set_page_config(page_title="핵 탐구", layout="wide")

st.title("핵 (Nucleus)")
st.caption("세포의 유전 정보 저장 및 생명 활동 총괄 제어 센터")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["핵심 기능 & 메커니즘", "세부 구조 심화", "관련 지식 & 질환"])

with tab1:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.subheader("유전 정보 전사 및 세포 활동 제어")
        st.markdown("""
        - **DNA 보관 및 보호:** 세포의 모든 설계도인 유전 정보(DNA)를 안전하게 보관합니다.
        - **전사(Transcription) 진행:** DNA 유전 정보를 mRNA로 복제하여 핵공을 통해 세포질로 보냅니다.
        - **세포 주기 및 분열 조절:** 세포 분열 시 염색질을 염색체 형태로 응축시켜 유전 물질을 분배합니다.
        """)
    with col2:
        st.info("""
        **중요 작용 경로**  
        DNA ➔ mRNA 전사 ➔ 핵공 배출 ➔ 리보솜 번역 ➔ 단백질 형성
        """)

with tab2:
    st.subheader("핵의 세부 구조")
    with st.expander("1. 핵막 (Nuclear Envelope) 및 핵공 (Nuclear Pore)", expanded=True):
        st.write("2중막(외막/내막) 구조이며, 외막은 소포체와 이어져 있습니다. 핵공 복합체는 RNA와 단백질 수송을 선택적으로 통제합니다.")
    with st.expander("2. 인 (Nucleolus)"):
        st.write("막이 없는 고농도 영역으로, rRNA 합성 및 리보솜 소단위체 조립이 집약적으로 일어납니다.")
    with st.expander("3. 염색질 (Chromatin)"):
        st.write("DNA가 히스톤 단백질을 감싸고 있는 뉴클레오솜 구조입니다. 유전자 발현이 활발한 진정염색질과 응축되어 억제된 이질염색질로 나뉩니다.")

with tab3:
    st.subheader("생물학적 지식")
    st.warning("""
    - **조경증(Progeria):** 핵막을 지지하는 라민(Lamin A) 단백질의 변형으로 핵막 형태가 무너져 조기 노화가 발생하는 질환입니다.
    - **포유류 적혈구:** 성숙한 포유류 적혈구는 산소 운반 공간을 극대화하기 위해 발달 과정에서 핵을 퇴화시킵니다.
    """)

st.markdown("---")
if st.button("메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
