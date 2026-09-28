import streamlit as st

st.set_page_config(page_title="골지체 탐구", page_icon="📮", layout="wide")

st.title("📮 골지체 (Golgi Apparatus)")
st.caption("📍 위치: 소포체 주변 및 세포막 근처")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("소포체에서 전달받은 단백질과 지질을 수선·가공·분류하여 세포 안팎으로 분비하는 우체국 역할을 합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("소포체로부터 수송 소포를 받고, 가공 완료 후 분비 소포를 만들어 세포막이나 리소좀으로 보냅니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["시스테르나 (Cisterna)", "수송/분비 소포"])
    
    if struct == "시스테르나 (Cisterna)":
        st.success("납작한 주머니가 여러 층으로 쌓여 있는 구조입니다.")
    elif struct == "수송/분비 소포":
        st.success("골지체 가장자리에서 떨어져 나와 물질을 목적지까지 운반하는 막 주머니입니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
