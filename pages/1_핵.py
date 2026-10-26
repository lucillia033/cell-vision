
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Cell Vision - 핵", layout="wide")

ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "nucleus.png"

st.markdown("""
<style>
.stApp {background:#101820;color:#F1F5F9}
[data-testid="stHeader"] {background:#101820}
[data-testid="stSidebar"] {background:#17232E}
h1,h2,h3,h4,p,li,label {color:#F1F5F9}
.section-title {
    font-size: 1.55rem; font-weight: 700; color: #F1F5F9;
    border-left: 4px solid #7C9BB5; padding: 3px 0 3px 13px;
    margin: 30px 0 15px 0;
}
.sub-title {
    font-size: 1.12rem; font-weight: 650; color: #B8D7F0;
    margin: 20px 0 7px 0;
}
.body-text {font-size: 1rem; line-height: 1.9; color:#E2E8F0}
div.stButton>button {
    background:#243746;color:#F1F5F9;border:1px solid #405568;
    border-radius:10px;padding:7px 15px
}
div.stButton>button:hover {background:#344D60;color:white}
hr {border-color:#34495A}
</style>
""", unsafe_allow_html=True)

def section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

def sub(title):
    st.markdown(f'<div class="sub-title">{title}</div>', unsafe_allow_html=True)

if st.button("← 세포소기관 목록으로"):
    st.switch_page("app.py")

st.title("핵")
st.caption("유전 정보를 보관하고 유전자 발현을 조절하는 세포소기관")
st.divider()

left, right = st.columns([1, 2], gap="large")
with left:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("images/nucleus.png 파일을 확인해 주세요.")

with right:
    section("개념과 기능")
    st.markdown("""
    핵은 대부분의 진핵세포에서 유전 물질인 DNA를 보관하는 세포소기관이다.
    DNA에는 세포의 구조와 기능을 유지하는 데 필요한 유전 정보가 저장되어 있다.
    핵은 유전 정보의 발현을 조절하여 단백질 합성과 세포의 생명 활동에 관여한다.
    """)

section("세부 구조")

sub("핵막")
st.write("핵막은 핵을 둘러싸는 이중막 구조이다. 핵 내부와 세포질을 구분하며, 핵 내부의 환경을 유지하는 역할을 한다. 핵막의 바깥쪽 막은 소포체 막과 연결되어 있다.")

sub("핵공")
st.write("핵공은 핵막에 존재하는 단백질 복합체이다. 핵과 세포질 사이의 물질 이동을 조절하며, mRNA가 핵 밖으로 이동하거나 핵에서 기능하는 단백질이 핵 안으로 들어오는 과정에 관여한다.")

sub("염색질")
st.write("염색질은 DNA와 단백질로 이루어진 물질이다. DNA를 효율적으로 포장하고 유전 정보의 발현을 조절하는 데 관여한다. 세포 분열 과정에서는 염색질이 응축되어 염색체를 형성한다.")

sub("인")
st.write("인은 핵 내부에 존재하는 구조로, 리보솜 RNA(rRNA)의 합성과 리보솜 소단위체의 조립이 이루어지는 장소이다. 조립된 리보솜 소단위체는 핵공을 통해 세포질로 이동하여 단백질 합성에 참여한다.")

section("유전 정보의 발현")
st.write("유전 정보의 발현은 DNA에 저장된 정보가 RNA나 단백질과 같은 기능적 산물로 이어지는 과정이다. 단백질을 암호화하는 유전자의 경우 DNA의 정보가 mRNA로 전사되며, mRNA는 핵공을 통해 세포질로 이동한다. 이후 리보솜에서 mRNA의 유전 정보가 해독되어 아미노산이 연결되고 단백질이 합성된다.")

section("다른 소기관과의 관계")
st.write("핵에서 전사된 mRNA는 리보솜에서 번역된다. 핵막의 바깥쪽 막은 소포체와 연결되어 있으며, 인에서는 리보솜 구성 요소의 합성과 조립이 이루어진다.")

section("핵심 정리")
st.write("핵은 DNA를 보관하고 유전자 발현을 조절한다. 핵공은 핵과 세포질 사이의 물질 이동을 조절하며, 인은 리보솜 구성 요소의 생산과 조립에 관여한다.")
