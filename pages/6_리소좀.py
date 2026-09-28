import streamlit as st

st.set_page_config(page_title="리소좀 탐구", page_icon="♻️", layout="wide")

st.title("♻️ 리소좀 (Lysosome)")
st.caption("📍 위치: 세포질 전반에 분포")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("다양한 가수분해 효소를 포함하고 있어 손상된 세포 소기관, 노폐물, 외부 침입물(세균)을 분해하는 재활용 센터입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("골지체에서 형성된 막 주머니에 가수분해 효소가 담겨 완성됩니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("특징을 선택하세요", ["단일막 주머니", "산성 환경 (pH 4.5~5.0)"])
    
    if struct == "단일막 주머니":
        st.success("내부의 강력한 효소가 세포 자체를 파괴하지 못하도록 막으로 안전하게 둘러싸여 있습니다.")
    elif struct == "산성 환경 (pH 4.5~5.0)":
        st.success("수소 이온 펌프를 작동시켜 내부를 산성으로 유지하며, 효소가 가장 활발히 작동하게 합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
