import streamlit as st

st.set_page_config(page_title="세포골격 탐구", page_icon="🏗️", layout="wide")

st.title("🏗️ 세포골격 (Cytoskeleton)")
st.caption("📍 위치: 세포질 전반에 그물망처럼 분포")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포의 형태를 유지하고, 소기관의 위치를 고정하며, 세포 내 물질 이동의 레일 역할을 합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("모터 단백질과 결합하여 소포체나 골지체에서 만들어진 수송 소포의 이동 경로를 제공합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("섬유 종류를 선택하세요", ["미세관 (Microtubule)", "중간섬유 (Intermediate Filament)", "미세섬유 (Microfilament)"])
    
    if struct == "미세관 (Microtubule)":
        st.success("튜불린 단백질로 구성되며 소기관 이동의 도로 및 세포 분열 시 방추사 역할을 합니다.")
    elif struct == "중간섬유 (Intermediate Filament)":
        st.success("세포의 기계적 강도를 유지하고 핵 등의 소기관 위치를 고정합니다.")
    elif struct == "미세섬유 (Microfilament)":
        st.success("액틴 단백질로 구성되며 세포 운동, 형태 변화, 세포질 분열에 관여합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
