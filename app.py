
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Explorer - 동물세포 탐구",
    layout="wide"
)

# app.py가 위치한 루트 디렉터리
ROOT_DIR = Path(__file__).resolve().parent

st.title("Cell Explorer")
st.write("동물세포 내부의 구조와 주요 소기관을 탐구해 보세요.")

st.markdown("---")

# 메인 화면 전체 세포 구조 대표 이미지
cell_img_path = ROOT_DIR / "images" / "cell.png"

if cell_img_path.is_file():
    st.image(
        str(cell_img_path),
        caption="동물세포의 전체 구조와 주요 세포소기관",
        use_container_width=True
    )
else:
    st.info(
        "**전체 세포 구조 이미지 준비 중**\n\n"
        "`images/cell.png` 파일을 업로드하면 "
        "이 위치에 동물세포 대표 이미지가 표시됩니다."
    )

st.markdown("---")

st.info("""
**동물세포 탐구 안내**

아래에서 탐구하고 싶은 세포소기관을 선택하세요.
'상세 탐구하기' 버튼을 누르면 해당 소기관의 세부 구조와
작용 원리를 확인할 수 있습니다.
""")

st.markdown("---")

organelles = [
    {
        "name": "핵 (Nucleus)",
        "page": "pages/1_핵.py",
        "desc": "유전 정보(DNA)를 보관하고 전사를 조절하는 세포의 제어 센터입니다.",
        "tag": "유전 정보 저장 / 전사 조절"
    },
    {
        "name": "리보솜 (Ribosome)",
        "page": "pages/2_리보솜.py",
        "desc": "mRNA 유전 코드를 읽어 아미노산을 연결하는 단백질 합성 장소입니다.",
        "tag": "단백질 번역 / 아미노산 결합"
    },
    {
        "name": "미토콘드리아 (Mitochondria)",
        "page": "pages/3_미토콘드리아.py",
        "desc": "세포 호흡과 산화적 인산화를 통해 ATP 에너지를 생성합니다.",
        "tag": "세포 호흡 / ATP 생성"
    },
    {
        "name": "소포체 (Endoplasmic Reticulum)",
        "page": "pages/4_소포체.py",
        "desc": "단백질 가공과 지질 합성, 세포 내 물질 수송을 담당합니다.",
        "tag": "단백질 가공 / 지질 합성"
    },
    {
        "name": "골지체 (Golgi Apparatus)",
        "page": "pages/5_골지체.py",
        "desc": "소포체에서 전달받은 물질을 가공하고 분류하여 운반합니다.",
        "tag": "단백질 가공 / 물질 분류"
    },
    {
        "name": "리소좀 (Lysosome)",
        "page": "pages/6_리소좀.py",
        "desc": "효소를 이용해 세포 내 물질과 손상된 구성 요소를 분해합니다.",
        "tag": "세포 내 소화 / 자가포식"
    },
    {
        "name": "세포막 (Cell Membrane)",
        "page": "pages/7_세포막.py",
        "desc": "선택적 투과성을 통해 물질의 출입을 조절합니다.",
        "tag": "선택적 투과성 / 신호 수용"
    },
    {
        "name": "세포질 (Cytoplasm)",
        "page": "pages/8_세포질.py",
        "desc": "세포 내부를 채우며 다양한 대사 반응이 일어나는 환경을 제공합니다.",
        "tag": "해당작용 / 세포 내 반응"
    },
    {
        "name": "세포골격 (Cytoskeleton)",
        "page": "pages/9_세포골격.py",
        "desc": "세포 형태를 유지하고 세포 내부의 물질 수송과 운동을 돕습니다.",
        "tag": "형태 유지 / 물질 수송"
    }
]

st.subheader("주요 세포소기관 목록")

for row_idx in range(0, len(organelles), 3):
    cols = st.columns(3, gap="medium")

    for col_idx, col in enumerate(cols):
        item_idx = row_idx + col_idx

        if item_idx < len(organelles):
            item = organelles[item_idx]

            with col:
                st.markdown(f"### {item['name']}")
                st.caption(f"핵심 역할: {item['tag']}")
                st.write(item["desc"])

                if st.button(
                    "상세 탐구하기 →",
                    key=f"main_nav_btn_{item_idx}",
                    use_container_width=True,
                    type="primary"
                ):
                    st.switch_page(item["page"])

    st.markdown("---")
