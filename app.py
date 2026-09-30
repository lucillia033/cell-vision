import streamlit as st
import os

st.set_page_config(
    page_title="Cell Explorer - 동물세포 탐구",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 상단 헤더 섹션
st.title("Cell Explorer")
st.write("동물세포 내부의 소기관을 탐구하고 각 구조의 메커니즘을 학습해보세요.")

st.markdown("---")

# 상단 메인 대시보드 안내 (푸른 톤 안내 박스)
st.info("""
**동물세포 탐구 안내**  
아래 카드에서 탐구하고 싶은 세포소기관의 '상세 탐구하기' 버튼을 선택하면, 해당 소기관의 세부 구조와 biological mechanism을 상세히 확인하실 수 있습니다.
""")

st.markdown("---")

# 9개 소기관 데이터 정의
organelles = [
    {
        "name": "핵 (Nucleus)",
        "eng": "Nucleus",
        "page": "pages/1_핵.py",
        "img": "nucleus.png",
        "desc": "유전 정보(DNA)를 보관하고 전사를 조절하는 세포의 컨트롤 센터입니다.",
        "tag": "유전 정보 저장 / 전사 조절"
    },
    {
        "name": "리보솜 (Ribosome)",
        "eng": "Ribosome",
        "page": "pages/2_리보솜.py",
        "img": "ribosome.png",
        "desc": "mRNA 유전 코드를 읽어 아미노산을 연결하는 단백질 합성 공장입니다.",
        "tag": "단백질 번역 / 아미노산 결합"
    },
    {
        "name": "미토콘드리아 (Mitochondria)",
        "eng": "Mitochondria",
        "page": "pages/3_미토콘드리아.py",
        "img": "mitochondria.png",
        "desc": "세포 호흡과 산화적 인산화를 통해 ATP 에너지를 생성하는 발전소입니다.",
        "tag": "세포 호흡 / ATP 생성"
    },
    {
        "name": "소포체 (Endoplasmic Reticulum)",
        "eng": "Endoplasmic Reticulum",
        "page": "pages/4_소포체.py",
        "img": "er.png",
        "desc": "단백질 접힘 가공과 지질 합성, 세포 내 수송망을 담당합니다.",
        "tag": "단백질 수선 / 지질 합성"
    },
    {
        "key_id": "golgi_btn",
        "name": "골지체 (Golgi Apparatus)",
        "eng": "Golgi Apparatus",
        "page": "pages/5_골지체.py",
        "img": "golgi.png",
        "desc": "소포체에서 온 물질을 최종 수선하고 목적지 표지를 부착해 분비합니다.",
        "tag": "단백질 가공 / 최종 분류"
    },
    {
        "name": "리소좀 (Lysosome)",
        "eng": "Lysosome",
        "page": "pages/6_리소좀.py",
        "img": "lysosome.png",
        "desc": "가수분해 효소로 손상된 소기관과 이물질을 분해하는 재활용 센터입니다.",
        "tag": "세포 내 소화 / 자가포식"
    },
    {
        "name": "세포막 (Cell Membrane)",
        "eng": "Cell Membrane",
        "page": "pages/7_세포막.py",
        "img": "membrane.png",
        "desc": "선택적 투과성을 통해 물질 출입을 통제하는 인지질 이중층 장벽입니다.",
        "tag": "선택적 투과성 / 신호 수용"
    },
    {
        "name": "세포질 (Cytoplasm)",
        "eng": "Cytoplasm",
        "page": "pages/8_세포질.py",
        "img": "cytosol.png",
        "desc": "소기관이 배치되고 해당작용 등 초기 대사 반응이 일어나는 점성 매질입니다.",
        "tag": "해당작용 / 매질 반응"
    },
    {
        "name": "세포골격 (Cytoskeleton)",
        "eng": "Cytoskeleton",
        "page": "pages/9_세포골격.py",
        "img": "cytoskeleton.png",
        "desc": "세포 형태를 지지하고 내부 수송 레일 및 운동을 구동하는 단백질 섬유망입니다.",
        "tag": "형태 유지 / 수송 레일"
    }
]

# 3x3 그리드 구성
st.subheader("주요 세포소기관 목록")

for row_idx in range(0, 9, 3):
    cols = st.columns(3, gap="medium")
    for col_idx in range(3):
        item_idx = row_idx + col_idx
        if item_idx < len(organelles):
            item = organelles[item_idx]
            with cols[col_idx]:
                # 이미지 출력 구문
                img_path = os.path.join(BASE_DIR, "images", item["img"])
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info(f"images/{item['img']}")
                
                st.markdown(f"### {item['name']}")
                st.caption(f"핵심 역할: {item['tag']}")
                st.write(item["desc"])
                
                # 페이지 이동 버튼
                btn_key = item.get("key_id", f"btn_{item_idx}")
                if st.button("상세 탐구하기 →", key=btn_key, use_container_width=True, type="primary"):
                    st.switch_page(item["page"])
    st.markdown("---")
