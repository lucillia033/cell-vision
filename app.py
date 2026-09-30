import streamlit as st
import os

st.set_page_config(
    page_title="Cell Explorer - 동물세포 탐구",
    layout="wide"
)

# 루트 경로 계산
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 상단 헤더
st.title("Cell Explorer")
st.write("동물세포 내부의 구조와 주요 소기관을 탐구해 보세요.")

st.markdown("---")

# -----------------------------------------------------------------------------
# 1. 메인 화면 전체 세포 구조 대표 이미지 영역
# -----------------------------------------------------------------------------
cell_img_path = os.path.join(BASE_DIR, "images", "cell.png")

if os.path.exists(cell_img_path):
    st.image(cell_img_path, caption="동물세포의 입체 구조 및 소기관 배치도", use_container_width=True)
else:
    # 대처용 대체 파일명 탐색 (cell.png가 없을 경우 nucleus.png 등 테스트 표출)
    st.info("💡 `images/cell.png` 파일(전체 세포 구조도)을 깃허브에 추가하면 메인 대표 이미지가 표시됩니다.")

st.markdown("---")

st.info("""
**동물세포 탐구 안내**  
아래 탐구하고 싶은 세포소기관의 '상세 탐구하기' 버튼을 누르면, 해당 소기관의 세부 구조와 메커니즘을 상세히 확인하실 수 있습니다.
""")

st.markdown("---")

# -----------------------------------------------------------------------------
# 2. 소기관 이동 카드 목록 (3x3 그리드)
# -----------------------------------------------------------------------------
organelles = [
    {
        "name": "핵 (Nucleus)",
        "page": "pages/1_핵.py",
        "desc": "유전 정보(DNA)를 보관하고 전사를 조절하는 세포의 컨트롤 센터입니다.",
        "tag": "유전 정보 저장 / 전사 조절"
    },
    {
        "name": "리보솜 (Ribosome)",
        "page": "pages/2_리보솜.py",
        "desc": "mRNA 유전 코드를 읽어 아미노산을 연결하는 단백질 합성 공장입니다.",
        "tag": "단백질 번역 / 아미노산 결합"
    },
    {
        "name": "미토콘드리아 (Mitochondria)",
        "page": "pages/3_미토콘드리아.py",
        "desc": "세포 호흡과 산화적 인산화를 통해 ATP 에너지를 생성하는 발전소입니다.",
        "tag": "세포 호흡 / ATP 생성"
    },
    {
        "name": "소포체 (Endoplasmic Reticulum)",
        "page": "pages/4_소포체.py",
        "desc": "단백질 접힘 가공과 지질 합성, 세포 내 수송망을 담당합니다.",
        "tag": "단백질 수선 / 지질 합성"
    },
    {
        "name": "골지체 (Golgi Apparatus)",
        "page": "pages/5_골지체.py",
        "desc": "소포체에서 온 물질을 최종 수선하고 목적지 표지를 부착해 분비합니다.",
        "tag": "단백질 가공 / 최종 분류"
    },
    {
        "name": "리소좀 (Lysosome)",
        "page": "pages/6_리소좀.py",
        "desc": "가수분해 효소로 손상된 소기관과 이물질을 분해하는 재활용 센터입니다.",
        "tag": "세포 내 소화 / 자가포식"
    },
    {
        "name": "세포막 (Cell Membrane)",
        "page": "pages/7_세포막.py",
        "desc": "선택적 투과성을 통해 물질 출입을 통제하는 인지질 이중층 장벽입니다.",
        "tag": "선택적 투과성 / 신호 수용"
    },
    {
        "name": "세포질 (Cytoplasm)",
        "page": "pages/8_세포질.py",
        "desc": "소기관이 배치되고 해당작용 등 초기 대사 반응이 일어나는 점성 매질입니다.",
        "tag": "해당작용 / 매질 반응"
    },
    {
        "name": "세포골격 (Cytoskeleton)",
        "page": "pages/9_세포골격.py",
        "desc": "세포 형태를 지지하고 내부 수송 레일 및 운동을 구동하는 단백질 섬유망입니다.",
        "tag": "형태 유지 / 수송 레일"
    }
]

st.subheader("주요 세포소기관 목록")

for row_idx in range(0, 9, 3):
    cols = st.columns(3, gap="medium")
    for col_idx in range(3):
        item_idx = row_idx + col_idx
        if item_idx < len(organelles):
            item = organelles[item_idx]
            with cols[col_idx]:
                st.markdown(f"### {item['name']}")
                st.caption(f"핵심 역할: {item['tag']}")
                st.write(item["desc"])
                
                # 버튼 클릭 시 해당 소기관 페이지로 직접 전환
                if st.button("상세 탐구하기 →", key=f"main_nav_btn_{item_idx}", use_container_width=True, type="primary"):
                    try:
                        st.switch_page(item["page"])
                    except Exception as e:
                        st.error(f"페이지 이동 실패: `{item['page']}` 파일 경로를 깃허브 `pages/` 폴더 내에서 확인해 주세요.")
    st.markdown("---")
