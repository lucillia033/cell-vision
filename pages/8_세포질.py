import streamlit as st

st.set_page_config(page_title="세포질 탐구", page_icon="🌊", layout="wide")

st.title("🌊 세포질 (Cytoplasm / Cytosol)")
st.caption("📍 위치: 핵을 제외한 세포막 내부 전반")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 내부를 채우는 액체 환경으로, 소기관들이 배치되어 있고 여러 화학 반응(해당작용 등)이 일어납니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("모든 소기관이 위치하는 공간이며, 영양소와 효소가 이동하는 통로 역할을 합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구성 요소를 선택하세요", ["세포액 (Cytosol)", "세포질 유동"])
    
    if struct == "세포액 (Cytosol)":
        st.success("물, 이온, 가용성 단백질 및 효소가 용해되어 있는 젤 상태의 액체 성분입니다.")
    elif struct == "세포질 유동":
        st.success("세포질이 일정한 방향으로 흐르면서 내부 물질과 소기관을 효율적으로 이동시킵니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
