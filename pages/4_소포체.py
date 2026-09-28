import streamlit as st

st.set_page_config(page_title="소포체 탐구", page_icon="📦", layout="wide")

st.title("📦 소포체 (Endoplasmic Reticulum)")
st.caption("📍 위치: 핵막과 연결되어 세포질 전반으로 확장")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("단백질과 지질을 합성하고, 합성된 물질을 세포 내 다른 부위나 골지체로 수송하는 통로 역할을 합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("핵막과 이어져 있으며, 합성한 단백질을 수송 소포에 담아 골지체로 전달합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("종류를 선택하세요", ["거친소포체 (Rough ER)", "매끈소포체 (Smooth ER)"])
    
    if struct == "거친소포체 (Rough ER)":
        st.success("표면에 리보솜이 부착되어 있어 리보솜이 만든 단백질을 가공하고 이동시킵니다.")
    elif struct == "매끈소포체 (Smooth ER)":
        st.success("리보솜이 없으며 지질(지방, 스테로이드) 합성 및 독성 물질 해독을 담당합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
