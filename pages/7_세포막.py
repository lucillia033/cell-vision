import streamlit as st

st.set_page_config(page_title="세포막 탐구", page_icon="🛡️", layout="wide")

st.title("🛡️ 세포막 (Cell Membrane)")
st.caption("📍 위치: 세포의 최외곽 경계")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 내부를 보호하고 외부 환경과의 경계를 이루며, 물질의 출입을 선택적으로 조절(선택적 투과성)합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("골지체에서 온 분비 소포와 융합하여 물질을 밖으로 배출(외포 작용)하고 세포골격과 연결되어 형태를 유지합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["인지질 이중층", "막단백질", "유동 모자이크 모델"])
    
    if struct == "인지질 이중층":
        st.success("친수성 머리와 소수성 꼬리를 가진 인지질이 두 층으로 배열되어 기본 장벽을 만듭니다.")
    elif struct == "막단백질":
        st.success("인지질 사이에 파묻혀 있거나 관통해 있어 물질 수송, 신호 전달, 세포 인식 역할을 합니다.")
    elif struct == "유동 모자이크 모델":
        st.success("인지질과 단백질이 고정되어 있지 않고 측면으로 자유롭게 이동할 수 있는 유동성 구조입니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
