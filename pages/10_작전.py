import streamlit as st
# Streamlit 라이브러리를 불러옵니다.
# 파이썬으로 웹 애플리케이션을 만들 때 사용하는 라이브러리입니다.

import streamlit.components.v1 as components
# Streamlit에서 HTML, CSS, JavaScript를 웹페이지에 삽입하기 위한 기능입니다.


# 웹페이지의 기본 설정을 지정합니다.
st.set_page_config(
    page_title="Cell Vision - Operation Cell Vision",  # 브라우저 탭에 표시되는 페이지 이름입니다.
    layout="wide",  # 화면을 넓게 사용하는 레이아웃으로 설정합니다.
    initial_sidebar_state="collapsed",  # 처음 접속했을 때 사이드바를 접힌 상태로 표시합니다.
)


# 웹페이지에 CSS를 삽입하여 전체적인 디자인을 설정합니다.
st.markdown(
    """
    <style>
    /* 웹페이지 메인 화면과 상단 헤더의 배경색을 지정합니다. */
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {
        background: #070C13;
    }

    /* 사이드바의 배경색을 지정합니다. */
    [data-testid="stSidebar"] {
        background: #101923;
    }

    /* 웹페이지 콘텐츠 영역의 여백과 최대 너비를 설정합니다. */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1500px;
    }

    /* 메인 화면으로 돌아가는 페이지 링크의 기본 디자인입니다. */
    div[data-testid="stPageLink"] a {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 38px;
        border: 1px solid #75869a;
        background: #17212d;
        color: #e3ebf4;
        text-decoration: none;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: .7px;
        border-radius: 0;
    }

    /* 마우스를 버튼 위에 올렸을 때 적용되는 디자인입니다. */
    div[data-testid="stPageLink"] a:hover {
        border-color: #9bcfff;
        background: #2a3a4b;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
    # Streamlit이 HTML과 CSS 코드를 실제로 적용하도록 허용합니다.
)


# 웹페이지 상단을 두 개의 열로 나눕니다.
# [5, 1]은 첫 번째 열과 두 번째 열의 너비 비율입니다.
title_col, exit_col = st.columns([5, 1])

# 첫 번째 열에 프로젝트 제목과 작전 정보를 표시합니다.
with title_col:
    st.markdown(
        """
        <div style="color:#8ABCE8;font-size:12px;letter-spacing:3px;">
            CELL VISION / BIOLOGICAL OPERATIONS UNIT
        </div>
        <div style="color:#F0F5FA;font-size:30px;font-weight:800;
                    letter-spacing:2px;margin-top:4px;">
            OPERATION CELL VISION
        </div>
        <div style="color:#8598AD;font-size:13px;margin-top:5px;
                    margin-bottom:16px;">
            BLACK VEIL INTERCEPTION PROTOCOL
        </div>
        """,
        unsafe_allow_html=True,
        # HTML 태그와 CSS를 웹페이지에 적용합니다.
    )

# 두 번째 열에 메인 화면으로 돌아가는 버튼을 배치합니다.
with exit_col:
    st.write("")  # 버튼 위쪽에 빈 공간을 추가합니다.
    st.page_link("app.py", label="EXIT TO BASE")
    # app.py에 해당하는 메인 페이지로 이동하는 링크를 생성합니다.


# HTML, CSS, JavaScript 코드를 하나의 문자열 변수에 저장합니다.
# r은 raw string의 약자로, 문자열 내부의 특수문자 처리를 단순화합니다.
game_html = r"""
<!DOCTYPE html>
<!-- HTML5 문서 형식임을 브라우저에 알려줍니다. -->

<html lang="ko">
<!-- HTML 문서의 시작이며 기본 언어를 한국어로 지정합니다. -->

<head>
<!-- 웹페이지의 설정과 스타일 정보를 작성하는 영역입니다. -->

<meta charset="UTF-8">
<!-- 한글이 깨지지 않도록 문자 인코딩을 UTF-8로 설정합니다. -->

<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- 모바일 화면에서도 화면 너비에 맞게 표시되도록 설정합니다. -->

<style>
/* =========================================================
   1. 전체 화면 및 기본 디자인
   ========================================================= */

/* 모든 요소의 크기 계산에 테두리와 여백을 포함하도록 설정합니다. */
*{box-sizing:border-box}

/* 웹페이지 전체의 기본 여백, 글자색, 배경색, 글꼴을 지정합니다. */
body{margin:0;color:#edf4fc;background:#070c13;font-family:Arial,"Malgun Gothic",sans-serif}

/* 버튼에도 웹페이지에서 지정한 글꼴을 적용합니다. */
button{font-family:inherit}

/* 게임 전체 화면의 크기, 테두리, 배경 및 배치 방식을 설정합니다. */
.game{position:relative;width:100%;min-height:720px;overflow:hidden;border:1px solid #293d51;border-radius:10px;background:radial-gradient(ellipse at 50% 30%,#183653,transparent 48%),linear-gradient(180deg,#111e2d,#101927 55%,#070b11)}

/* 게임 배경에 격자무늬를 추가합니다. */
.grid{position:absolute;inset:0;opacity:.13;pointer-events:none;background-image:linear-gradient(#5c8cb1 1px,transparent 1px),linear-gradient(90deg,#5c8cb1 1px,transparent 1px);background-size:42px 42px}

/* 게임 상단 영역의 요소를 가로 방향으로 배치합니다. */
.topbar{position:relative;z-index:3;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:19px 18px}

/* 상단의 작은 프로젝트 이름 디자인입니다. */
.kicker{color:#8dbce9;font-size:10px;letter-spacing:2px;margin-bottom:6px}

/* 게임의 주요 제목 디자인입니다. */
.heading{font-size:clamp(16px,2.5vw,22px);font-weight:900;letter-spacing:1.3px}

/* 제목 아래 부제목 디자인입니다. */
.sub{color:#8194aa;font-size:10px;margin-top:5px;letter-spacing:1px}

/* 적의 체력 표시 영역 너비를 설정합니다. */
.enemy-hud{width:min(250px,32vw)}

/* 적의 체력 표시 이름과 숫자를 양쪽에 배치합니다. */
.hud-label{display:flex;justify-content:space-between;gap:8px;margin-bottom:7px;color:#d6e0eb;font-size:10px;letter-spacing:1px}

/* 적의 체력 막대 전체 영역을 디자인합니다. */
.bar-track{display:flex;gap:3px;height:12px;padding:2px;border:1px solid #85414b;background:#281b24}

/* 적의 체력 한 칸을 나타냅니다. */
.enemy-cell{flex:1;background:#e24e5d;box-shadow:0 0 6px #a72c3b66}

/* 적이 피해를 입어 사라진 체력 칸의 디자인입니다. */
.enemy-cell.empty{background:#241b25;box-shadow:none}


/* =========================================================
   2. 전투 공간과 캐릭터 디자인
   ========================================================= */

/* 플레이어와 적이 등장하는 전투 공간입니다. */
.arena{position:relative;height:300px;overflow:hidden;border-top:1px solid #233548;border-bottom:1px solid #314358;background:radial-gradient(ellipse at 50% 100%,#27445c77,transparent 55%),linear-gradient(180deg,transparent 65%,#070c13)}

/* 화면 중앙에 생물학적 코어를 배치합니다. */
.machine{position:absolute;left:50%;top:15px;width:190px;height:205px;transform:translateX(-50%);border:2px solid #32648c88;border-radius:48% 48% 12% 12%;background:linear-gradient(180deg,#214b6c33,#07111d99);box-shadow:0 0 45px #1678ba22,inset 0 0 30px #287db322}

/* 코어 내부에 타원형 구조를 추가합니다. */
.machine:before{content:"";position:absolute;left:50%;top:12px;width:80px;height:150px;transform:translateX(-50%);border:3px solid #69baf2;border-radius:50%;box-shadow:0 0 20px #4ba9ff66,inset 0 0 20px #4ba9ff44}

/* 코어 아래쪽에 이름을 표시합니다. */
.machine:after{content:"BIOLOGICAL CORE";position:absolute;bottom:12px;left:0;right:0;color:#8bc8f2;text-align:center;font-size:9px;letter-spacing:2px}

/* 전투 공간의 바닥을 디자인합니다. */
.floor{position:absolute;z-index:1;bottom:0;left:0;right:0;height:45px;border-top:2px solid #476580;background:linear-gradient(180deg,#1c2b3b,#070b11)}

/* 바닥에 가로 방향의 빛 효과를 추가합니다. */
.floor:after{content:"";position:absolute;top:12px;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,#54a9ec,transparent)}

/* 플레이어와 적의 이름표에 공통으로 적용되는 디자인입니다. */
.unit-label{position:absolute;bottom:185px;z-index:4;color:#a9c7df;font-size:9px;letter-spacing:1px;white-space:nowrap}

/* 플레이어 이름표를 왼쪽에 배치합니다. */
.player-label{left:5%}

/* 적 이름표를 오른쪽에 배치합니다. */
.enemy-label{right:5%;color:#e59aa4}

/* 캐릭터의 기본 크기와 위치 기준을 설정합니다. */
.fighter{position:absolute;z-index:3;bottom:34px;width:112px;height:158px}

/* 플레이어는 왼쪽, 적은 오른쪽에 배치합니다. */
.enemy{right:12%;transform:scaleX(-1)}.player{left:12%}

/* 캐릭터의 몸통 모양을 만듭니다. */
.body-shape{position:absolute;z-index:2;left:29px;top:53px;width:55px;height:68px;border:1px solid #71859a;background:linear-gradient(90deg,#263a4b,#405469 42%,#152332 75%);clip-path:polygon(20% 0,80% 0,100% 28%,88% 100%,12% 100%,0 28%)}

/* 몸통 내부의 장식 요소를 추가합니다. */
.body-shape:before{content:"";position:absolute;top:12px;left:12px;width:28px;height:34px;border:1px solid #6d8296;background:linear-gradient(135deg,#273c4f,#111b27)}

/* 몸통 중앙에 세로 장식을 추가합니다. */
.body-shape:after{content:"";position:absolute;top:8px;left:20px;width:8px;height:46px;border-left:1px solid #8295a8;border-right:1px solid #8295a8;background:#101a25}

/* 캐릭터의 헬멧을 디자인합니다. */
.helmet{position:absolute;z-index:4;top:10px;left:32px;width:49px;height:49px;border:2px solid #8798a8;border-radius:43% 43% 27% 27%;background:linear-gradient(135deg,#586b7e,#202c3a 60%,#0b1119);box-shadow:inset 0 -5px 0 #101925}

/* 헬멧 앞부분에 빛나는 바이저를 추가합니다. */
.helmet:before{content:"";position:absolute;top:18px;left:5px;right:5px;height:8px;border:1px solid #c5eaff;background:#8bcfff;box-shadow:0 0 12px #4bb6ff}

/* 헬멧 위쪽에 장식 요소를 추가합니다. */
.helmet:after{content:"";position:absolute;top:4px;left:10px;width:24px;height:5px;border:1px solid #71869a;background:#182635}

/* 캐릭터의 어깨 부분을 디자인합니다. */
.shoulder{position:absolute;z-index:3;top:57px;width:25px;height:28px;border:1px solid #788b9e;border-radius:5px;background:linear-gradient(135deg,#52687b,#1b2937)}

/* 왼쪽과 오른쪽 어깨의 위치와 각도를 설정합니다. */
.shoulder.left{left:14px;transform:rotate(12deg)}.shoulder.right{left:75px;transform:rotate(-12deg)}

/* 캐릭터의 팔 부분을 디자인합니다. */
.arm{position:absolute;z-index:1;top:77px;width:15px;height:39px;border:1px solid #5c7084;border-radius:4px;background:linear-gradient(90deg,#182431,#3b4d5f)}

/* 양팔의 위치와 회전 각도를 설정합니다. */
.arm.left{left:20px;transform:rotate(9deg)}.arm.right{left:81px;transform:rotate(-9deg)}

/* 캐릭터의 허리띠를 디자인합니다. */
.belt{position:absolute;z-index:4;top:115px;left:32px;width:49px;height:9px;border:1px solid #677b8e;background:#101923}

/* 캐릭터의 다리 부분을 디자인합니다. */
.leg{position:absolute;z-index:2;top:119px;width:20px;height:34px;border:1px solid #52687b;background:linear-gradient(90deg,#172331,#354657)}

/* 양쪽 다리의 위치와 회전 각도를 설정합니다. */
.leg.left{left:35px;transform:rotate(4deg)}.leg.right{left:57px;transform:rotate(-4deg)}

/* 캐릭터의 신발을 디자인합니다. */
.boot{position:absolute;z-index:3;top:146px;width:25px;height:9px;border:1px solid #526477;border-radius:3px;background:#0a1119}

/* 양쪽 신발의 위치를 설정합니다. */
.boot.left{left:31px}.boot.right{left:56px}

/* 캐릭터 허리에 장비 주머니를 추가합니다. */
.pouch{position:absolute;z-index:4;top:91px;left:72px;width:13px;height:17px;border:1px solid #718398;background:#182b3b}

/* 적 캐릭터의 몸통 색상을 붉은색 계열로 변경합니다. */
.enemy .body-shape{border-color:#a45a66;background:linear-gradient(90deg,#34252f,#54404a 42%,#17151e 75%)}

/* 적의 헬멧 색상을 변경합니다. */
.enemy .helmet{border-color:#bd6975;background:linear-gradient(135deg,#58404a,#251a24 70%,#0b0b11)}

/* 적의 헬멧 바이저를 붉은색으로 표시합니다. */
.enemy .helmet:before{border-color:#ff9aa2;background:#fa4856;box-shadow:0 0 12px #fa3349}

/* 적의 어깨, 팔, 다리 테두리 색상을 변경합니다. */
.enemy .shoulder,.enemy .arm,.enemy .leg{border-color:#8f515c}

/* 적의 어깨 색상을 변경합니다. */
.enemy .shoulder{background:linear-gradient(135deg,#58313b,#211922)}

/* 적 몸통 내부 장식의 색상을 변경합니다. */
.enemy .body-shape:before{border-color:#98515d;background:linear-gradient(135deg,#422833,#17121a)}


/* =========================================================
   3. 무기와 공격 효과 디자인
   ========================================================= */

/* 캐릭터가 들고 있는 기본 무기의 위치와 크기를 설정합니다. */
.weapon-model{position:absolute;z-index:6;top:70px;left:57px;width:59px;height:22px}

/* 총의 개머리판 부분을 디자인합니다. */
.weapon-stock{position:absolute;top:4px;left:0;width:13px;height:8px;border:1px solid #8ba0b2;background:#283b4b}

/* 총의 몸통 부분을 디자인합니다. */
.weapon-body{position:absolute;top:2px;left:10px;width:31px;height:12px;border:1px solid #c1d1df;background:linear-gradient(180deg,#9aaaba,#37495a 60%,#172330)}

/* 총의 총열 부분을 디자인합니다. */
.weapon-barrel{position:absolute;top:5px;left:39px;width:20px;height:5px;border:1px solid #c6d5e2;background:#8b9bab}

/* 총 위쪽의 조준경을 디자인합니다. */
.weapon-scope{position:absolute;top:-3px;left:19px;width:11px;height:5px;border:1px solid #8ca0b2;background:#182432}

/* 총 아래쪽의 손잡이를 디자인합니다. */
.weapon-grip{position:absolute;top:11px;left:24px;width:6px;height:10px;border:1px solid #718497;background:#263848;transform:rotate(12deg)}

/* 수류탄이나 중폭탄을 장착했을 때 기본 총 부품을 숨깁니다. */
.weapon-model.grenade-mode,.weapon-model.heavy-mode{top:59px;left:68px;width:34px;height:34px;transform:rotate(-15deg)}

/* 수류탄 모드와 중폭탄 모드에서 총의 각 부품을 표시하지 않습니다. */
.weapon-model.grenade-mode .weapon-stock,.weapon-model.grenade-mode .weapon-body,.weapon-model.grenade-mode .weapon-barrel,.weapon-model.grenade-mode .weapon-scope,.weapon-model.grenade-mode .weapon-grip,.weapon-model.heavy-mode .weapon-stock,.weapon-model.heavy-mode .weapon-body,.weapon-model.heavy-mode .weapon-barrel,.weapon-model.heavy-mode .weapon-scope,.weapon-model.heavy-mode .weapon-grip{display:none}

/* 수류탄의 둥근 몸체를 CSS로 만듭니다. */
.weapon-model.grenade-mode:before{content:"";position:absolute;inset:3px;border:2px solid #c2d0dc;border-radius:40%;background:radial-gradient(circle at 30% 25%,#b8c4cc,#566675 55%,#1b2937);box-shadow:0 0 9px #ffad5d66}

/* 수류탄 위쪽의 안전장치 부분을 표현합니다. */
.weapon-model.grenade-mode:after{content:"";position:absolute;top:-1px;left:12px;width:7px;height:5px;border:1px solid #f8d4a8;background:#e7a66a}

/* 세 번째 무기인 폭탄의 몸체와 붉은색 표시를 표현합니다. */
.weapon-model.heavy-mode:before{content:"";position:absolute;inset:3px;border:2px solid #ffb4a2;border-radius:35%;background:radial-gradient(circle at 30% 25%,#fff1c9,#ff795a 50%,#812536);box-shadow:0 0 15px #ff593c}

/* 폭탄 가운데에 B 표시를 추가합니다. */
.weapon-model.heavy-mode:after{content:"B";position:absolute;top:9px;left:11px;color:white;font-size:12px;font-weight:900}

/* 적 캐릭터가 들고 있는 무기의 위치를 설정합니다. */
.enemy .weapon-model{left:-7px}

/* 적의 총 몸통을 붉은색 계열로 표시합니다. */
.enemy .weapon-body{border-color:#d6a0a6;background:linear-gradient(180deg,#a76a73,#54313b 60%,#23151d)}

/* 적의 총열 색상을 변경합니다. */
.enemy .weapon-barrel{border-color:#d6a0a6;background:#9e626d}

/* 캐릭터가 공격을 받았을 때 밝게 표시하는 효과입니다. */
.player.hit,.enemy.hit{filter:brightness(2.5) drop-shadow(0 0 14px #ff5267)}

/* 플레이어가 공격받으면 왼쪽으로 살짝 이동합니다. */
.player.hit{translate:-7px 0}

/* 적이 공격받으면 좌우 반전 상태를 유지하면서 이동합니다. */
.enemy.hit{transform:scaleX(-1) translateX(-7px)}

/* 플레이어가 공격할 때 적용되는 애니메이션입니다. */
.player.attack{animation:recoil .22s ease}

/* 반동 애니메이션의 시작, 중간, 끝 위치를 지정합니다. */
@keyframes recoil{0%{translate:0 0}40%{translate:-7px 0}100%{translate:0 0}}

/* 발사체의 기본 크기와 색상, 위치를 설정합니다. */
.projectile{position:absolute;z-index:7;display:none;width:28px;height:4px;border-radius:4px;background:#80d5ff;box-shadow:0 0 13px 4px #318dff;pointer-events:none}

/* 수류탄 발사체의 모양을 설정합니다. */
.projectile.grenade{width:14px;height:14px;border:1px solid #ffd09a;border-radius:50%;background:radial-gradient(circle at 30% 25%,#fff0bf,#ff9b55 45%,#a64029);box-shadow:0 0 20px 8px #ff5c3588}

/* 세 번째 무기인 폭탄 발사체의 모양을 설정합니다. */
.projectile.heavy{width:26px;height:26px;border:2px solid #ffd6a0;border-radius:38%;background:radial-gradient(circle at 30% 25%,#fff8d8,#ffb65a 42%,#fa4856 78%);box-shadow:0 0 25px 12px #ff653c99}

/* 폭발 효과를 표현하는 원형 요소의 기본 디자인입니다. */
.blast{position:absolute;z-index:8;display:none;width:24px;height:24px;border-radius:50%;background:#ffd7a1;box-shadow:0 0 25px 18px #ff603b,0 0 65px 35px #ffb34d88;pointer-events:none}


/* =========================================================
   4. 플레이어 상태 및 문제 화면 디자인
   ========================================================= */

/* 아래쪽 화면을 플레이어 정보와 문제 영역 두 부분으로 나눕니다. */
.bottom{position:relative;z-index:4;display:grid;grid-template-columns:190px minmax(0,1fr);gap:13px;padding:13px}

/* 플레이어의 체력과 무기 정보를 표시하는 패널입니다. */
.player-panel{padding:13px;border:1px solid #2a4056;background:#101b28}

/* 플레이어 상태 패널의 제목 디자인입니다. */
.panel-title{margin-bottom:12px;color:#9cc9ee;font-size:11px;letter-spacing:1.5px}

/* 체력과 콤보 등의 작은 제목 디자인입니다. */
.small-label{margin:12px 0 6px;color:#91a4b8;font-size:10px}

/* 플레이어 체력 막대의 전체 영역입니다. */
.hp-track,.energy-track{display:flex;gap:4px;height:9px;padding:1px;background:#253243}

/* 플레이어의 남은 체력 한 칸을 표시합니다. */
.hp-unit{flex:1;background:#62baff;box-shadow:0 0 5px #45a6ff77}

/* 잃은 체력 한 칸을 어두운 색으로 표시합니다. */
.hp-unit.lost{background:#3b2029;box-shadow:none}

/* 콤보 진행도를 나타내는 막대입니다. */
.energy-fill{width:0%;height:100%;background:#65d8db;transition:width .2s}

/* 무기 목록의 기본 디자인입니다. */
.weapon{margin-top:6px;padding:8px;border:1px solid #344a60;background:#142131;color:#91a4b8;font-size:10px}

/* 현재 기본 무기가 선택된 상태를 표시합니다. */
.weapon.active{border-color:#65baff;background:#1b344a;color:white;box-shadow:inset 3px 0 #65baff}

/* 수류탄이 선택된 상태를 표시합니다. */
.weapon.grenade-active{border-color:#ffad61;background:#3b2a20;color:#ffe0b8;box-shadow:inset 3px 0 #ffad61}

/* 중폭탄이 선택된 상태를 표시합니다. */
.weapon.heavy-active{border-color:#ff7180;background:#3a2029;color:#ffd4d9;box-shadow:inset 3px 0 #ff7180}

/* 현재 장착한 무기에 대한 안내 문구 디자인입니다. */
.weapon-hint{margin-top:8px;color:#8da7bf;font-size:9px;line-height:1.6}

/* 문제 영역의 최소 너비와 내부 여백, 테두리, 배경색을 설정합니다. */
.question-panel{min-width:0;padding:16px;border:1px solid #30475e;background:#0b121d}

/* 문제 번호와 정답·오답 수를 양쪽에 배치합니다. */
.question-meta{display:flex;justify-content:space-between;gap:10px;color:#8ebce7;font-size:10px;letter-spacing:1px}

/* 문제 본문의 글자 크기와 간격을 설정합니다. */
.question{margin:13px 0 15px;font-size:16px;line-height:1.6;font-weight:700}

/* 선택지를 두 열로 배치합니다. */
.answers{display:grid;grid-template-columns:1fr 1fr;gap:8px}

/* 선택지 버튼의 기본 디자인입니다. */
.answer{min-height:43px;padding:10px 12px;border:1px solid #34475d;background:#101b29;color:#d4dfeb;text-align:left;font-size:12px;cursor:pointer}

/* 마우스를 선택지 위에 올렸을 때의 디자인입니다. */
.answer:hover:not(:disabled){border-color:#76bfff;background:#1b3044}

/* 선택지가 비활성화되었을 때 클릭할 수 없도록 표시합니다. */
.answer:disabled{cursor:default;opacity:.8}

/* 정답 선택지의 디자인입니다. */
.answer.correct{border-color:#61d5a0;background:#15372f;color:#b7f4d8}

/* 오답 선택지의 디자인입니다. */
.answer.wrong{border-color:#f16b78;background:#3a1c27;color:#ffc3c8}

/* 정답 여부를 알려주는 피드백 영역입니다. */
.feedback{min-height:35px;margin-top:12px;color:#b2c3d5;font-size:11px;line-height:1.7}

/* 다음 문제 버튼을 배치하는 영역입니다. */
.action-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}

/* 다음 문제 등 일반적인 기능 버튼의 디자인입니다. */
.action{padding:10px 13px;border:1px solid #52728e;background:#17293a;color:#e8f4ff;font-size:11px;font-weight:700;cursor:pointer}

/* 마우스를 버튼 위에 올렸을 때의 배경색입니다. */
.action:hover:not(:disabled){background:#244664}

/* 버튼이 비활성화되었을 때의 디자인입니다. */
.action:disabled{opacity:.35;cursor:not-allowed}

/* 게임 진행 규칙을 알려주는 안내 문구입니다. */
.status{margin-top:10px;color:#9eb3c9;font-size:10px;line-height:1.6}


/* =========================================================
   5. 게임 성공 및 실패 화면 디자인
   ========================================================= */

/* 게임 종료 시 화면 전체를 덮는 결과 창입니다. */
.overlay{position:absolute;z-index:20;inset:0;display:none;align-items:center;justify-content:center;padding:20px;background:#03070df2;text-align:center}

/* show 클래스가 추가되면 결과 창을 화면에 표시합니다. */
.overlay.show{display:flex}

/* 결과 창 내부의 상자 디자인입니다. */
.result-box{width:min(560px,100%);padding:30px 20px;border:1px solid #536c85;background:#101a27;box-shadow:0 0 60px #1a5b8a33}

/* 결과 제목의 크기와 굵기를 설정합니다. */
.result-title{margin-bottom:12px;font-size:clamp(25px,5vw,39px);font-weight:900;letter-spacing:2px}

/* 실패 결과를 붉은색으로 표시합니다. */
.fail{color:#ff6a79}

/* 성공 결과를 푸른색으로 표시합니다. */
.win{color:#7bc9ff}

/* 결과 창의 작은 상단 제목 디자인입니다. */
.result-kicker{margin-bottom:12px;color:#8dbce9;font-size:10px;letter-spacing:2px}

/* 성공 또는 실패 상태 문구의 디자인입니다. */
.result-status{margin-bottom:15px;color:#7bc9ff;font-size:12px;font-weight:800;letter-spacing:1.5px}

/* 결과 설명 문구의 디자인입니다. */
.result-desc{margin-bottom:22px;color:#c1cfde;font-size:13px;line-height:1.9}

/* 결과 창의 버튼들을 가운데에 배치합니다. */
.result-actions{display:flex;justify-content:center;flex-wrap:wrap;gap:10px}

/* 재시작 버튼의 디자인입니다. */
.retry{padding:13px 18px;border:1px solid #6abaff;background:#193b57;color:#f2f8ff;font-size:11px;font-weight:800;letter-spacing:.7px;cursor:pointer}

/* 재시작 버튼에 마우스를 올렸을 때의 디자인입니다. */
.retry:hover{background:#255a80}

/* 메인 화면 복귀 버튼의 디자인입니다. */
.return-base{border-color:#78d5b0;background:#12362f;color:#c8ffe8}

/* 복귀 버튼에 마우스를 올렸을 때의 디자인입니다. */
.return-base:hover{background:#1b5145}


/* =========================================================
   6. 모바일 화면에 맞춘 반응형 디자인
   ========================================================= */

/* 화면 너비가 680px 이하일 때 아래 디자인을 적용합니다. */
@media(max-width:680px){

/* 모바일에서는 게임 화면의 최소 높이를 늘립니다. */
.game{min-height:760px}.topbar{align-items:flex-start;padding:14px}.enemy-hud{width:145px;max-width:42vw}

/* 모바일에서는 전투 공간과 코어 크기를 줄입니다. */
.arena{height:255px}.machine{width:140px;height:155px}.machine:before{width:65px;height:110px}

/* 캐릭터 크기를 줄이고 위치 기준점을 아래쪽으로 설정합니다. */
.fighter{scale:.8;transform-origin:bottom center}.player{left:1%}.enemy{right:1%;transform:scaleX(-.8)}

/* 플레이어 정보와 문제 영역을 세로 방향으로 배치합니다. */
.bottom{grid-template-columns:1fr;padding:9px}.player-panel{display:grid;grid-template-columns:1fr 1fr;gap:8px}

/* 플레이어 상태 제목이 두 열 전체를 차지하도록 합니다. */
.panel-title{grid-column:1/-1;margin-bottom:0}.small-label{margin-top:4px}

/* 모바일 화면에 맞게 문제 글자 크기를 줄이고 선택지를 한 열로 배치합니다. */
.question{font-size:14px}.answers{grid-template-columns:1fr}

/* 결과 창의 내부 여백을 줄입니다. */
.result-box{padding:24px 15px}
}
</style>
</head>

<body>
<!-- 실제 게임 화면에 표시되는 HTML 요소들이 시작됩니다. -->

<div class="game" id="game">
<!-- 게임 전체를 감싸는 영역입니다. id는 JavaScript에서 이 요소를 찾을 때 사용합니다. -->

<div class="grid"></div>
<!-- CSS로 만든 배경 격자무늬를 표시합니다. -->

<div class="topbar">
<!-- 게임 상단의 제목과 적 체력 정보를 담는 영역입니다. -->

<div>
<div class="kicker">CELL VISION / OPERATION CELL VISION</div>
<!-- 프로젝트의 이름을 표시합니다. -->

<div class="heading">BLACK VEIL INTERCEPTION</div>
<!-- 게임의 주요 작전 이름을 표시합니다. -->

<div class="sub">BIOLOGICAL THREAT ELIMINATION</div>
<!-- 작전의 부제목을 표시합니다. -->
</div>

<div class="enemy-hud">
<!-- 적의 체력 정보를 표시하는 영역입니다. -->

<div class="hud-label"><span>ENEMY INTEGRITY</span><span id="enemyCount">10 / 10</span></div>
<!-- 적의 현재 체력을 숫자로 표시합니다. -->

<div class="bar-track" id="enemyBars"></div>
<!-- JavaScript가 적의 체력 칸 10개를 생성하는 영역입니다. -->
</div>
</div>

<div class="arena" id="arena">
<!-- 플레이어와 적이 전투하는 공간입니다. -->

<div class="machine"></div>
<!-- 화면 중앙의 생물학적 코어를 표시합니다. -->

<div class="unit-label player-label">PLAYER / OPERATIVE</div>
<!-- 플레이어의 이름표입니다. -->

<div class="unit-label enemy-label">BLACK VEIL / ELITE</div>
<!-- 적의 이름표입니다. -->

<div class="fighter player" id="player">
<!-- 플레이어 캐릭터를 구성하는 영역입니다. -->

<div class="helmet"></div><div class="body-shape"></div>
<!-- 플레이어의 헬멧과 몸통입니다. -->

<div class="shoulder left"></div><div class="shoulder right"></div>
<!-- 플레이어의 양쪽 어깨입니다. -->

<div class="arm left"></div><div class="arm right"></div><div class="belt"></div>
<!-- 플레이어의 양팔과 허리띠입니다. -->

<div class="leg left"></div><div class="leg right"></div>
<!-- 플레이어의 양쪽 다리입니다. -->

<div class="boot left"></div><div class="boot right"></div><div class="pouch"></div>
<!-- 플레이어의 신발과 장비 주머니입니다. -->

<div class="weapon-model" id="playerWeapon">
<!-- 플레이어가 들고 있는 무기입니다. JavaScript에서 무기 종류를 변경합니다. -->

<div class="weapon-stock"></div><div class="weapon-body"></div>
<!-- 총의 개머리판과 몸통입니다. -->

<div class="weapon-barrel"></div><div class="weapon-scope"></div>
<!-- 총열과 조준경입니다. -->

<div class="weapon-grip"></div>
<!-- 총의 손잡이입니다. -->
</div>
</div>

<div class="fighter enemy" id="enemy">
<!-- 적 캐릭터를 구성하는 영역입니다. -->

<div class="helmet"></div><div class="body-shape"></div>
<!-- 적의 헬멧과 몸통입니다. -->

<div class="shoulder left"></div><div class="shoulder right"></div>
<!-- 적의 양쪽 어깨입니다. -->

<div class="arm left"></div><div class="arm right"></div><div class="belt"></div>
<!-- 적의 양팔과 허리띠입니다. -->

<div class="leg left"></div><div class="leg right"></div>
<!-- 적의 양쪽 다리입니다. -->

<div class="boot left"></div><div class="boot right"></div><div class="pouch"></div>
<!-- 적의 신발과 장비 주머니입니다. -->

<div class="weapon-model">
<!-- 적이 들고 있는 무기입니다. -->

<div class="weapon-stock"></div><div class="weapon-body"></div>
<div class="weapon-barrel"></div><div class="weapon-scope"></div>
<div class="weapon-grip"></div>
<!-- 적의 무기를 구성하는 각 부분입니다. -->
</div>
</div>

<div class="projectile" id="projectile"></div>
<!-- 플레이어가 발사하는 총알, 수류탄, 중폭탄이 이동하는 요소입니다. -->

<div class="blast" id="blast"></div>
<!-- 무기가 적에게 도달했을 때 나타나는 폭발 효과입니다. -->

<div class="floor"></div>
<!-- 전투 공간의 바닥입니다. -->
</div>

<div class="bottom">
<!-- 화면 아래쪽에 플레이어 정보와 문제를 배치합니다. -->

<div class="player-panel">
<!-- 플레이어의 체력, 콤보, 무기 정보를 표시하는 패널입니다. -->

<div class="panel-title">OPERATIVE STATUS</div>
<!-- 플레이어 상태 패널의 제목입니다. -->

<div>
<div class="small-label">PLAYER HP <span id="hpCount">4 / 4</span></div>
<!-- 플레이어의 현재 체력을 숫자로 표시합니다. -->

<div class="hp-track" id="hpBars"></div>
<!-- JavaScript가 플레이어의 체력 막대 4개를 생성하는 영역입니다. -->
</div>

<div>
<div class="small-label">COMBO <span id="comboCount">0</span> / 3</div>
<!-- 연속 정답 횟수를 표시합니다. -->

<div class="energy-track"><div class="energy-fill" id="energyFill"></div></div>
<!-- 연속 정답 횟수에 따라 차오르는 콤보 게이지입니다. -->
</div>

<div style="grid-column:1/-1">
<!-- 이 영역이 플레이어 정보 패널의 두 열 전체를 차지하도록 설정합니다. -->

<div class="small-label">EQUIPPED WEAPONS</div>
<!-- 장착된 무기 목록의 제목입니다. -->

<div class="weapon active" id="rifleSlot">1 — PULSE RIFLE</div>
<!-- 기본 무기인 펄스 라이플입니다. -->

<div class="weapon" id="grenadeSlot">2 — GRENADE / 2 COMBO</div>
<!-- 연속 2정답 시 사용하는 수류탄입니다. -->

<div class="weapon" id="heavySlot">3 — AIRSTRIKE BOMB / 3 COMBO</div>
<!-- 모든 문제를 맞혔을 때 사용하는 마지막 무기입니다. -->

<div class="weapon-hint" id="weaponHint">PULSE RIFLE 장착 중</div>
<!-- 현재 장착된 무기에 대한 설명을 표시합니다. -->
</div>
</div>

<div class="question-panel">
<!-- 문제와 선택지, 정답 피드백을 표시하는 영역입니다. -->

<div class="question-meta">
<!-- 문제 번호와 전체 정답·오답 수를 표시합니다. -->

<span id="questionNumber">MISSION QUESTION 01</span>
<!-- 현재 문제의 번호를 표시합니다. -->

<span id="accuracy">CORRECT 0 · WRONG 0</span>
<!-- 지금까지 맞힌 문제와 틀린 문제의 수를 표시합니다. -->
</div>

<div class="question" id="questionText"></div>
<!-- JavaScript가 현재 문제의 내용을 넣는 영역입니다. -->

<div class="answers" id="answers"></div>
<!-- JavaScript가 문제의 선택지 버튼을 생성하는 영역입니다. -->

<div class="feedback" id="feedback">문제를 풀어 작전을 진행하십시오.</div>
<!-- 정답 또는 오답을 선택했을 때 결과와 해설을 표시합니다. -->

<div class="action-row">
<!-- 다음 문제 버튼을 배치하는 영역입니다. -->

<button class="action" id="nextButton" disabled>NEXT QUESTION</button>
<!-- 다음 문제로 이동하는 버튼입니다. 처음에는 비활성화되어 있습니다. -->
</div>

<div class="status" id="status">연속 2정답: 수류탄 공격 / 연속 3정답: 폭탄 투하 / 체력 소진: 임무 실패</div>
<!-- 게임 진행 규칙을 안내합니다. -->
</div>
</div>

<div class="overlay" id="overlay">
<!-- 게임이 끝났을 때 화면 위에 표시되는 결과 창입니다. -->

<div class="result-box">
<!-- 결과 창의 내용을 담는 상자입니다. -->

<div class="result-kicker" id="resultKicker">CELL VISION // MISSION REPORT</div>
<!-- 성공 또는 실패 보고서의 종류를 표시합니다. -->

<div class="result-title" id="resultTitle">MISSION FAILED</div>
<!-- 임무 성공 또는 실패 결과를 크게 표시합니다. -->

<div class="result-status" id="resultStatus">MISSION STATUS / FAILED</div>
<!-- 임무의 최종 상태를 표시합니다. -->

<div class="result-desc" id="resultDesc"></div>
<!-- 정답 수, 오답 수, 임무 결과에 대한 설명을 표시합니다. -->

<div class="result-actions">
<!-- 결과 창의 버튼들을 배치하는 영역입니다. -->

<button class="retry" id="retryButton">RETRY MISSION</button>
<!-- 실패했을 때 게임을 다시 시작하는 버튼입니다. -->

<button class="retry return-base" id="returnButton">
RETURN TO BASE
</button>
<!-- 게임을 종료하고 메인 화면으로 돌아가는 버튼입니다. -->
</div>
</div>
</div>
</div>

<script>
"use strict";
// JavaScript에서 엄격 모드를 사용합니다.
// 선언하지 않은 변수를 사용하거나 허용되지 않는 문법을 사용하는 실수를 방지합니다.


/* =========================================================
   7. 문제 데이터
   ========================================================= */

// 게임에서 출제할 생물학 문제 12개를 저장하는 배열입니다.
// 배열은 여러 데이터를 하나의 변수에 순서대로 저장하는 자료구조입니다.
const questionBank = [

{q:"세포에서 ATP 생성과 밀접한 관련이 있는 소기관은 무엇인가요?",a:["리보솜","미토콘드리아","골지체","리소좀"],correct:1,explain:"미토콘드리아는 세포 호흡을 통해 ATP를 생성하는 데 중요한 역할을 합니다."},

// q는 문제 내용, a는 선택지, correct는 정답의 배열 번호, explain은 해설입니다.
// 배열의 번호는 0부터 시작하므로 correct:1은 두 번째 선택지가 정답이라는 뜻입니다.

{q:"단백질 합성이 일어나는 주요 장소는 어디인가요?",a:["리보솜","핵","리소좀","세포막"],correct:0,explain:"리보솜은 유전 정보를 바탕으로 단백질을 합성합니다."},

{q:"세포의 유전 정보가 주로 저장되는 곳은 어디인가요?",a:["골지체","세포질","핵","액포"],correct:2,explain:"핵에는 DNA가 들어 있으며 세포의 활동을 조절하는 데 중요한 역할을 합니다."},

{q:"세포 안팎의 물질 이동을 조절하는 구조는 무엇인가요?",a:["리보솜","세포막","핵소체","미토콘드리아"],correct:1,explain:"세포막은 세포 내부와 외부 사이의 물질 이동을 선택적으로 조절합니다."},

{q:"단백질의 가공과 분류, 포장에 관여하는 소기관은 무엇인가요?",a:["골지체","핵","리소좀","세포골격"],correct:0,explain:"골지체는 단백질과 지질을 가공하고 분류해 목적지로 보내는 데 관여합니다."},

{q:"세포 내 물질을 분해하는 효소를 포함하는 소기관은 무엇인가요?",a:["리보솜","골지체","리소좀","핵"],correct:2,explain:"리소좀은 여러 분해 효소를 이용해 세포 내 물질을 분해합니다."},

{q:"세포질에서 다양한 대사 반응이 일어나는 영역은 무엇인가요?",a:["세포질","핵막","세포벽","염색체"],correct:0,explain:"세포질은 세포막 안쪽에서 핵을 제외한 영역으로, 다양한 대사 반응이 일어납니다."},

{q:"세포의 형태 유지와 세포 내 구조물 이동에 관여하는 것은 무엇인가요?",a:["세포골격","리소좀","핵소체","골지체"],correct:0,explain:"세포골격은 세포의 형태를 유지하고 세포 내 구조물의 이동에도 관여합니다."},

{q:"단백질 합성에 필요한 정보를 담고 있는 분자는 무엇인가요?",a:["DNA","지방산","포도당","물"],correct:0,explain:"DNA의 유전 정보는 RNA를 거쳐 단백질 합성에 이용됩니다."},

{q:"세포 호흡에 사용되는 대표적인 에너지원은 무엇인가요?",a:["포도당","산소만","핵산","셀룰로스만"],correct:0,explain:"포도당은 세포 호흡에서 분해되어 ATP 생성에 필요한 에너지를 제공합니다."},

{q:"거친면 소포체 표면에 리보솜이 붙어 있는 이유는 무엇인가요?",a:["단백질 합성","DNA 복제만","ATP 직접 저장","세포 분열 중단"],correct:0,explain:"거친면 소포체의 리보솜은 주로 막 단백질이나 분비 단백질 합성에 관여합니다."},

{q:"농도 기울기를 따라 에너지 투입 없이 일어나는 물질 이동은 무엇인가요?",a:["능동 수송","확산","소낭 수송만","DNA 복제"],correct:1,explain:"확산은 입자가 농도가 높은 곳에서 낮은 곳으로 순이동하는 현상입니다."}
];


/* =========================================================
   8. 게임 상태를 저장하는 변수
   ========================================================= */

// 화면에 있는 HTML 요소를 id를 이용해 쉽게 찾기 위한 함수입니다.
// document.getElementById()는 HTML에서 특정 id를 가진 요소를 가져옵니다.
const $ = id => document.getElementById(id);


// 실제 게임에서 사용할 문제들을 저장하는 배열입니다.
let questions = [];

// 현재 몇 번째 문제를 풀고 있는지 저장합니다.
let questionIndex = 0;

// 플레이어의 현재 체력입니다. 처음에는 4입니다.
let playerHP = 4;

// 적의 현재 체력입니다. 처음에는 10입니다.
let enemyHP = 10;

// 연속으로 맞힌 문제의 개수를 저장합니다.
let combo = 0;

// 지금까지 맞힌 문제의 총개수입니다.
let correctTotal = 0;

// 지금까지 틀린 문제의 총개수입니다.
let wrongTotal = 0;

// 현재 정답 판정이나 공격 애니메이션이 진행 중인지 확인합니다.
// true이면 추가 선택을 막습니다.
let locked = false;

// 게임이 끝났는지 확인하는 변수입니다.
let finished = false;

// 한 문제도 틀리지 않았는지 확인하는 변수입니다.
// 마지막 중폭탄 공격의 조건을 판단할 때 사용합니다.
let perfectRun = true;

// 공격이나 애니메이션의 순서를 구분하는 번호입니다.
// 이전에 실행된 공격이 나중에 영향을 주는 것을 방지합니다.
let actionToken = 0;

// 실행 중인 타이머들을 저장하는 배열입니다.
// 게임 재시작이나 종료 시 타이머를 정리할 때 사용합니다.
let timers = [];


/* =========================================================
   9. 시간 지연 및 타이머 관리 함수
   ========================================================= */

// 일정 시간이 지난 뒤 특정 함수를 실행하는 기능입니다.
function later(callback, delay) {

    // setTimeout()은 지정한 시간이 지난 뒤 callback 함수를 실행합니다.
    // timer에는 생성된 타이머의 번호가 저장됩니다.
    const timer = setTimeout(() => {

        // 실행이 끝난 타이머를 timers 배열에서 제거합니다.
        timers = timers.filter(t => t !== timer);

        // 지정된 시간이 지나면 전달받은 함수를 실행합니다.
        callback();

    }, delay);

    // 생성된 타이머를 배열에 저장합니다.
    timers.push(timer);
}


// 현재 실행 중인 모든 타이머를 취소하는 함수입니다.
function clearTimers() {

    // timers 배열에 저장된 모든 타이머를 하나씩 취소합니다.
    timers.forEach(clearTimeout);

    // 타이머 목록을 빈 배열로 초기화합니다.
    timers = [];
}


/* =========================================================
   10. 문제 순서를 무작위로 섞는 함수
   ========================================================= */

// 배열에 저장된 요소들의 순서를 무작위로 바꾸는 함수입니다.
function shuffle(array) {

    // 원본 배열을 직접 변경하지 않도록 복사본을 만듭니다.
    const result = [...array];

    // 배열의 마지막 요소부터 첫 번째 요소까지 반복합니다.
    for (let i = result.length - 1; i > 0; i--) {

        // 현재 위치보다 앞쪽에 있는 무작위 위치를 선택합니다.
        const j = Math.floor(Math.random() * (i + 1));

        // 두 위치의 요소를 서로 바꿉니다.
        // 이 방법을 Fisher-Yates 셔플이라고 합니다.
        [result[i], result[j]] = [result[j], result[i]];
    }

    // 순서가 바뀐 배열을 반환합니다.
    return result;
}


/* =========================================================
   11. 무기 변경 함수
   ========================================================= */

// 무기 종류에 따라 캐릭터의 무기 모양과 무기 목록을 변경합니다.
function setWeapon(type) {

    // 플레이어가 들고 있는 무기 요소를 가져옵니다.
    const model = $("playerWeapon");

    // 기존에 적용된 수류탄 또는 중폭탄 모드를 제거합니다.
    model.classList.remove("grenade-mode", "heavy-mode");

    // 세 무기의 선택 상태를 모두 초기화합니다.
    $("rifleSlot").className = "weapon";
    $("grenadeSlot").className = "weapon";
    $("heavySlot").className = "weapon";


    // 선택한 무기가 수류탄이라면 실행합니다.
    if (type === "grenade") {

        // 무기 모양을 수류탄으로 변경합니다.
        model.classList.add("grenade-mode");

        // 수류탄이 선택되었다는 표시를 추가합니다.
        $("grenadeSlot").classList.add("grenade-active");

        // 현재 무기에 대한 설명을 변경합니다.
        $("weaponHint").textContent =
            "GRENADE 장착 · 연속 2정답 공격";

    // 선택한 무기가 중폭탄이라면 실행합니다.
    } else if (type === "heavy") {

        // 무기 모양을 중폭탄으로 변경합니다.
        model.classList.add("heavy-mode");

        // 중폭탄이 선택되었다는 표시를 추가합니다.
        $("heavySlot").classList.add("heavy-active");

        // 중폭탄에 대한 설명을 표시합니다.
        $("weaponHint").textContent =
            "AIRSTRIKE BOMB 투하 준비 · 연속 3정답";

    // 수류탄이나 중폭탄이 아니라면 기본 무기를 사용합니다.
    } else {

        // 펄스 라이플이 선택되었다는 표시를 추가합니다.
        $("rifleSlot").classList.add("active");

        // 기본 무기에 대한 설명을 표시합니다.
        $("weaponHint").textContent = "PULSE RIFLE 장착 중";
    }
}


/* =========================================================
   12. 체력과 콤보 화면 갱신 함수
   ========================================================= */

// 현재 게임 데이터를 화면에 반영하는 함수입니다.
function renderBars() {

    // 기존 적 체력 막대의 내용을 모두 지웁니다.
    $("enemyBars").innerHTML = "";

    // 적의 최대 체력인 10만큼 반복합니다.
    for (let i = 0; i < 10; i++) {

        // 새로운 체력 칸을 만들고 div 요소로 설정합니다.
        const cell = document.createElement("div");

        // 현재 체력보다 큰 번호라면 empty 클래스를 추가합니다.
        // 예를 들어 enemyHP가 8이면 8번부터 9번까지 비어 있는 상태로 표시합니다.
        cell.className = "enemy-cell" + (i >= enemyHP ? " empty" : "");

        // 생성한 체력 칸을 적 체력 영역에 추가합니다.
        $("enemyBars").appendChild(cell);
    }

    // 적의 현재 체력을 숫자로 표시합니다.
    $("enemyCount").textContent = `${enemyHP} / 10`;

    // 기존 플레이어 체력 막대의 내용을 모두 지웁니다.
    $("hpBars").innerHTML = "";

    // 플레이어의 최대 체력인 4만큼 반복합니다.
    for (let i = 0; i < 4; i++) {

        // 새로운 체력 칸을 생성합니다.
        const cell = document.createElement("div");

        // 현재 체력보다 큰 번호라면 잃은 체력으로 표시합니다.
        cell.className = "hp-unit" + (i >= playerHP ? " lost" : "");

        // 생성한 체력 칸을 플레이어 체력 영역에 추가합니다.
        $("hpBars").appendChild(cell);
    }

    // 플레이어의 현재 체력을 숫자로 표시합니다.
    $("hpCount").textContent = `${playerHP} / 4`;

    // 현재 연속 정답 횟수를 표시합니다.
    $("comboCount").textContent = combo;

    // 콤보 횟수에 따라 게이지의 너비를 변경합니다.
    // 콤보가 1이면 50%, 2이면 100%입니다.
    $("energyFill").style.width = `${combo * 100 / 3}%`;

    // 지금까지 맞힌 문제와 틀린 문제의 개수를 표시합니다.
    $("accuracy").textContent =
        `CORRECT ${correctTotal} · WRONG ${wrongTotal}`;
}


/* =========================================================
   13. 문제 화면을 불러오는 함수
   ========================================================= */

// 현재 문제를 화면에 표시하는 함수입니다.
function loadQuestion() {

    // 게임이 끝났다면 더 이상 문제를 불러오지 않습니다.
    if (finished) return;

    // 새로운 문제를 풀 수 있도록 잠금 상태를 해제합니다.
    locked = false;

    // 다음 문제 버튼을 비활성화합니다.
    // 답을 선택하기 전에는 다음 문제로 넘어갈 수 없습니다.
    $("nextButton").disabled = true;

    // 현재 문제 데이터를 가져옵니다.
    const item = questions[questionIndex];

    // 현재 문제 번호를 두 자리 숫자로 표시합니다.
    // padStart(2, "0")은 한 자리 숫자 앞에 0을 붙입니다.
    $("questionNumber").textContent =
        `MISSION QUESTION ${String(questionIndex + 1).padStart(2, "0")}`;

    // 문제 내용을 화면에 표시합니다.
    $("questionText").textContent = item.q;

    // 문제를 불러올 때 안내 문구를 초기화합니다.
    $("feedback").textContent = "정답을 선택하십시오.";

    // 기존 선택지 내용을 모두 제거합니다.
    $("answers").innerHTML = "";

    // 현재 문제의 선택지를 하나씩 반복합니다.
    item.a.forEach((answer, index) => {

        // 각 선택지를 표시할 버튼을 생성합니다.
        const button = document.createElement("button");

        // 버튼에 answer 클래스를 적용하고 선택지의 알파벳과 내용을 표시합니다.
        // String.fromCharCode(65 + index)는 0부터 A, B, C, D를 만들어 줍니다.
        button.className = "answer";
        button.textContent = `${String.fromCharCode(65 + index)}. ${answer}`;

        // 버튼을 클릭하면 선택지 번호를 submitAnswer 함수에 전달합니다.
        button.addEventListener("click", () => submitAnswer(index));

        // 생성한 버튼을 선택지 영역에 추가합니다.
        $("answers").appendChild(button);
    });
}


/* =========================================================
   14. 무기 발사 애니메이션
   ========================================================= */

// 무기 종류에 따라 발사체가 적에게 이동하는 애니메이션을 실행합니다.
function animateShot(type, token) {

    // 게임이 끝났거나 현재 공격 번호가 이전 공격 번호와 다르면 실행을 중단합니다.
    if (finished || token !== actionToken) return;

    // 발사체, 전투 공간, 플레이어, 적 요소를 가져옵니다.
    const projectile = $("projectile");
    const arena = $("arena");
    const player = $("player");
    const enemy = $("enemy");

    // 플레이어 위치를 기준으로 발사 시작 지점을 계산합니다.
    const startX = type === "heavy"
        ? enemy.offsetLeft + enemy.offsetWidth * 0.35
        : player.offsetLeft + player.offsetWidth * 0.8;

    // 폭탄은 전투 공간 상단에서 떨어지고, 다른 무기는 아래쪽에서 발사됩니다.
    const startY = type === "heavy" ? 0 : arena.clientHeight - 105;

    // 적 캐릭터의 위치를 기준으로 도착 지점을 계산합니다.
    const endX = enemy.offsetLeft + enemy.offsetWidth * 0.2;

    // 발사체의 기존 모양을 초기화합니다.
    projectile.className = "projectile";

    // 수류탄이라면 수류탄 디자인을 추가합니다.
    if (type === "grenade") projectile.classList.add("grenade");

    // 중폭탄이라면 중폭탄 디자인을 추가합니다.
    if (type === "heavy") projectile.classList.add("heavy");

    // 발사체를 화면에 표시합니다.
    projectile.style.display = "block";

    // 발사체의 시작 위치를 설정합니다.
    projectile.style.left = `${startX}px`;
    projectile.style.top = `${startY}px`;

    // 플레이어의 기존 공격 애니메이션을 초기화합니다.
    player.classList.remove("attack");

    // offsetWidth를 읽어 브라우저가 스타일 변경을 다시 계산하도록 합니다.
    // 이를 이용해 같은 애니메이션을 연속으로 실행할 수 있습니다.
    void player.offsetWidth;

    // 플레이어에게 공격 애니메이션을 적용합니다.
    player.classList.add("attack");

    // 무기 종류에 따라 발사체가 이동하는 시간을 다르게 설정합니다.
    const duration =
        type === "heavy" ? 850 : type === "grenade" ? 480 : 300;

    // 애니메이션이 시작된 시각을 저장합니다.
    const start = performance.now();

    // requestAnimationFrame으로 반복 실행되는 발사체 이동 함수입니다.
    function step(now) {

        // 게임이 끝났거나 공격 번호가 변경되었다면 애니메이션을 중단합니다.
        if (finished || token !== actionToken) {
            projectile.style.display = "none";
            return;
        }

        // 현재까지 진행된 애니메이션의 비율을 계산합니다.
        // 0은 시작, 1은 종료를 의미합니다.
        const progress = Math.min((now - start) / duration, 1);

        // 수류탄과 중폭탄은 포물선처럼 이동하도록 높이 변화를 계산합니다.
        // Math.sin()은 사인 함수이며, 진행 비율에 따라 이동 궤적을 만듭니다.
        const curve =
            type === "grenade"
                ? Math.sin(progress * Math.PI) * -65
                : 0;

        // 시작 지점에서 도착 지점까지 발사체의 가로 위치를 이동시킵니다.
        projectile.style.left =
            `${startX + (endX - startX) * progress}px`;

        // 포물선 이동 높이를 반영하여 세로 위치를 변경합니다.
        projectile.style.top = type === "heavy"
            ? `${startY + (arena.clientHeight - 115) * progress}px`
            : `${startY + curve}px`;

        // 아직 애니메이션이 끝나지 않았다면 다음 화면 프레임에서 다시 실행합니다.
        if (progress < 1) {
            requestAnimationFrame(step);

        // 발사체가 목적지에 도달했다면 실행합니다.
        } else {

            // 발사체를 화면에서 숨깁니다.
            projectile.style.display = "none";

            // 중폭탄이나 수류탄이면 폭발 효과를 실행합니다.
            if (type === "heavy" || type === "grenade") {
                showBlast(endX, type === "heavy" ? arena.clientHeight - 115 : startY, type, token);

            // 기본 총이라면 적에게 체력 1의 피해를 주고 다음 문제로 넘어갈 준비를 합니다.
            } else {
                hitEnemy(1);
                finishAnswerAction();
            }
        }
    }

    // 브라우저의 다음 화면 갱신 시점에 step 함수를 실행합니다.
    requestAnimationFrame(step);
}


/* =========================================================
   15. 폭발 효과 함수
   ========================================================= */

// 수류탄이나 중폭탄이 적에게 도달했을 때 폭발 효과를 표시합니다.
function showBlast(x, y, type, token) {

    // 게임이 끝났거나 공격 번호가 달라졌다면 실행하지 않습니다.
    if (finished || token !== actionToken) return;

    // 폭발 효과를 표시할 HTML 요소를 가져옵니다.
    const blast = $("blast");

    // 폭발 효과가 적의 위치에 나타나도록 가로 위치를 지정합니다.
    blast.style.left = `${x - 10}px`;

    // 폭발 효과의 세로 위치를 지정합니다.
    blast.style.top = `${y - 10}px`;

    // 폭발 효과를 화면에 표시합니다.
    blast.style.display = "block";

    // animate()를 이용해 폭발의 크기와 투명도가 시간에 따라 변하도록 합니다.
    blast.animate(
        [
            { transform: "scale(.2)", opacity: 1 },
            { transform: "scale(3.8)", opacity: .95 },
            { transform: "scale(6)", opacity: 0 }
        ],
        {
            // 중폭탄은 900ms, 수류탄은 650ms 동안 폭발 애니메이션을 실행합니다.
            duration: type === "heavy" ? 900 : 650,

            // 애니메이션이 자연스럽게 끝나도록 속도 변화를 설정합니다.
            easing: "ease-out"
        }
    );

    // 중폭탄 공격이라면 완벽한 작전 수행 메시지를 표시합니다.
    if (type === "heavy") {
        $("feedback").textContent =
            "AIRSTRIKE BOMB IMPACT! 폭탄 투하 완료.";
    }

    // 일정 시간이 지난 후 폭발 효과를 종료하고 피해를 적용합니다.
    later(() => {

        // 게임이 끝났거나 공격 번호가 변경되었다면 실행하지 않습니다.
        if (finished || token !== actionToken) return;

        // 폭발 효과를 화면에서 숨깁니다.
        blast.style.display = "none";

        // 세 번째 무기인 폭탄은 적에게 체력 3의 피해를 줍니다.
        if (type === "heavy") {
            hitEnemy(3);
            finishAnswerAction();

        // 수류탄이라면 적에게 체력 2의 피해를 줍니다.
        } else {
            hitEnemy(2);
            finishAnswerAction();
        }

    }, type === "heavy" ? 650 : 420);
}


/* =========================================================
   16. 적에게 피해를 주는 함수
   ========================================================= */

// 적의 체력을 감소시키고 화면을 갱신하는 함수입니다.
function hitEnemy(damage) {

    // 게임이 끝났다면 피해를 적용하지 않습니다.
    if (finished) return;

    // 적에게 피격 효과를 추가합니다.
    $("enemy").classList.add("hit");

    // 220ms가 지나면 피격 효과를 제거합니다.
    later(() => $("enemy").classList.remove("hit"), 220);

    // 적의 체력에서 피해량을 뺍니다.
    // Math.max(0, ...)를 사용하여 체력이 음수가 되지 않도록 합니다.
    enemyHP = Math.max(0, enemyHP - damage);

    // 변경된 적 체력을 화면에 반영합니다.
    renderBars();

    // 적의 체력이 0 이하가 되었다면 게임을 승리로 종료합니다.
    if (enemyHP <= 0) {
        endGame(true);
    }
}


/* =========================================================
   17. 공격 이후 다음 문제를 진행할 수 있도록 설정
   ========================================================= */

// 공격 애니메이션이 끝난 뒤 다음 문제 버튼을 활성화하는 함수입니다.
function finishAnswerAction() {

    // 게임이 끝났다면 아무 작업도 하지 않습니다.
    if (finished) return;

    // 선택을 막았던 잠금 상태를 해제합니다.
    locked = false;

    // 다음 문제 버튼을 활성화합니다.
    $("nextButton").disabled = false;
}


/* =========================================================
   18. 정답과 오답 판정
   ========================================================= */

// 사용자가 선택한 답을 확인하고 게임 상태를 변경하는 핵심 함수입니다.
function submitAnswer(selected) {

    // 이미 답을 선택했거나 게임이 끝났다면 추가 실행을 막습니다.
    if (locked || finished) return;

    // 답을 처리하는 동안 다른 선택을 하지 못하도록 잠급니다.
    locked = true;

    // 새로운 공격 번호를 생성합니다.
    // 이전에 실행된 애니메이션과 현재 애니메이션을 구분하는 데 사용합니다.
    const token = ++actionToken;

    // 현재 문제의 데이터를 가져옵니다.
    const item = questions[questionIndex];

    // 현재 화면에 표시된 모든 선택지 버튼을 배열로 가져옵니다.
    const buttons = [...$("answers").querySelectorAll("button")];

    // 답을 선택한 뒤 모든 선택지 버튼을 비활성화합니다.
    buttons.forEach(button => button.disabled = true);


    // 사용자가 선택한 답과 실제 정답의 번호가 같다면 실행합니다.
    if (selected === item.correct) {

        // 전체 정답 수를 1 증가시킵니다.
        correctTotal++;

        // 연속 정답 횟수를 1 증가시킵니다.
        combo++;

        // 선택한 정답 버튼에 정답 디자인을 적용합니다.
        buttons[selected].classList.add("correct");


        // 세 번째 연속 정답이면 폭탄 투하 공격을 실행합니다.
        if (combo >= 3) {

            // 폭탄 공격 후 콤보를 0으로 초기화합니다.
            combo = 0;

            // 세 번째 무기인 폭탄을 장착합니다.
            setWeapon("heavy");
            renderBars();

            $("feedback").textContent =
                `3연속 정답! AIRSTRIKE BOMB 투하 · 적 체력 3칸 감소. ${item.explain}`;
            $("nextButton").disabled = true;

            // 잠시 뒤 폭탄이 상공에서 떨어지는 애니메이션을 실행합니다.
            later(() => {
                if (!finished && token === actionToken) {
                    animateShot("heavy", token);
                }
            }, 350);

            return;
        }


        // 두 번째 연속 정답이면 수류탄 공격을 실행합니다.
        if (combo === 2) {

            // 두 번째 무기인 수류탄을 장착합니다.
            setWeapon("grenade");

            // 변경된 체력과 콤보 정보를 화면에 반영합니다.
            renderBars();

            // 수류탄 공격과 문제 해설을 표시합니다.
            $("feedback").textContent =
                `연속 2정답! GRENADE 발사 · 적 체력 2칸 감소. ${item.explain}`;

            // 공격이 끝날 때까지 다음 문제 버튼을 비활성화합니다.
            $("nextButton").disabled = true;

            // 수류탄 발사 애니메이션을 실행합니다.
            animateShot("grenade", token);

        // 연속 정답이 2회가 아니라면 기본 무기로 공격합니다.
        } else {

            // 기본 무기인 펄스 라이플을 장착합니다.
            setWeapon("rifle");

            // 정답 수와 콤보를 화면에 반영합니다.
            renderBars();

            // 기본 무기 공격 메시지와 해설을 표시합니다.
            $("feedback").textContent =
                `정답입니다. PULSE RIFLE 발사 · 적 체력 1칸 감소. ${item.explain}`;

            // 공격이 끝날 때까지 다음 문제 버튼을 비활성화합니다.
            $("nextButton").disabled = true;

            // 펄스 라이플 발사 애니메이션을 실행합니다.
            animateShot("rifle", token);
        }


    // 사용자가 선택한 답이 실제 정답과 다르면 실행합니다.
    } else {

        // 전체 오답 수를 1 증가시킵니다.
        wrongTotal++;

        // 연속 정답 횟수를 0으로 초기화합니다.
        combo = 0;

        // 한 번이라도 틀렸으므로 완벽한 작전 상태를 해제합니다.
        perfectRun = false;

        // 플레이어의 체력을 1 감소시킵니다.
        // Math.max를 사용해 체력이 0보다 작아지지 않도록 합니다.
        playerHP = Math.max(0, playerHP - 1);

        // 사용자가 틀린 선택지에 오답 디자인을 적용합니다.
        buttons[selected].classList.add("wrong");

        // 실제 정답 선택지에 정답 디자인을 적용합니다.
        buttons[item.correct].classList.add("correct");

        // 오답이므로 기본 무기를 장착 상태로 되돌립니다.
        setWeapon("rifle");

        // 변경된 체력과 정답·오답 수를 화면에 반영합니다.
        renderBars();

        // 플레이어에게 피격 효과를 적용합니다.
        $("player").classList.add("hit");

        // 250ms 후 피격 효과를 제거합니다.
        later(() => $("player").classList.remove("hit"), 250);

        // 오답 안내와 문제 해설을 표시합니다.
        $("feedback").textContent =
            `오답입니다. 플레이어 HP -1, 콤보 초기화. ${item.explain}`;

        // 플레이어의 체력이 0 이하라면 임무 실패로 처리합니다.
        if (playerHP <= 0) {

            // 다음 문제 버튼을 비활성화합니다.
            $("nextButton").disabled = true;

            // 300ms 후 실패 화면을 표시합니다.
            later(() => endGame(false), 300);

            // 아래 코드를 실행하지 않고 함수를 종료합니다.
            return;
        }

        // 체력이 남아 있다면 다음 문제로 넘어갈 수 있도록 잠금을 해제합니다.
        locked = false;

        // 다음 문제 버튼을 활성화합니다.
        $("nextButton").disabled = false;
    }
}


/* =========================================================
   19. 메인 화면으로 돌아가는 함수
   ========================================================= */

/*
 * 부모 Streamlit 페이지의 실제 메인 페이지 링크를 찾아 이동합니다.
 * 배포 주소의 루트 URL로 이동하는 방식은 사용하지 않습니다.
 */

// 메인 화면으로 돌아가는 기능을 수행하는 함수입니다.
function returnToBase() {

    // 외부 문서에 접근하는 과정에서 오류가 발생할 수 있으므로 try-catch를 사용합니다.
    try {

        // 현재 HTML을 포함하고 있는 부모 창의 문서에 접근합니다.
        const parentDocument = window.parent.document;

        // 부모 문서 안에 있는 Streamlit 페이지 이동 링크들을 배열로 가져옵니다.
        const links = Array.from(
            parentDocument.querySelectorAll(
                '[data-testid="stPageLink"] a, ' +
                'a[data-testid="stPageLink-NavLink"]'
            )
        );

        // 링크 중 EXIT TO BASE라는 글자가 포함된 링크를 찾습니다.
        const baseLink = links.find(link =>
            (link.innerText || link.textContent || "")
                .trim()
                .includes("EXIT TO BASE")
        );

        // 해당 링크를 찾았다면 실행합니다.
        if (baseLink) {

            // 실제 링크를 클릭하여 Streamlit 메인 페이지로 이동합니다.
            baseLink.click();

            // 복귀가 시작되었으므로 함수를 종료합니다.
            return;
        }

        // 일부 Streamlit 버전에서는 링크의 HTML 구조가 다를 수 있으므로
        // 모든 링크를 대상으로 다시 검색합니다.
        const fallbackLinks = Array.from(
            parentDocument.querySelectorAll("a")
        );

        // 링크의 글자가 EXIT TO BASE와 정확히 일치하는 요소를 찾습니다.
        const fallbackLink = fallbackLinks.find(link =>
            (link.innerText || link.textContent || "")
                .trim() === "EXIT TO BASE"
        );

        // 대체 검색으로 링크를 찾았다면 실행합니다.
        if (fallbackLink) {

            // 해당 링크를 클릭합니다.
            fallbackLink.click();

            // 함수를 종료합니다.
            return;
        }

        // 두 가지 방법으로도 링크를 찾지 못했다면 안내 문구를 표시합니다.
        $("resultDesc").innerHTML +=
            '<br><br><span style="color:#ffb4a2;">' +
            '복귀 링크를 찾지 못했습니다. 화면 상단의 ' +
            'EXIT TO BASE 버튼을 이용하십시오.' +
            '</span>';

    // try 안의 코드에서 오류가 발생하면 catch 부분을 실행합니다.
    } catch (error) {

        // 자동 복귀가 제한되었음을 알리는 안내 문구를 표시합니다.
        $("resultDesc").innerHTML +=
            '<br><br><span style="color:#ffb4a2;">' +
            '자동 복귀가 제한되었습니다. 화면 상단의 ' +
            'EXIT TO BASE 버튼을 이용하십시오.' +
            '</span>';
    }
}


/* =========================================================
   20. 게임 종료 함수
   ========================================================= */

// victory 값에 따라 성공 또는 실패 결과를 표시하는 함수입니다.
// true를 전달하면 성공, false를 전달하면 실패입니다.
function endGame(victory) {

    // 이미 게임이 끝났다면 중복 실행하지 않습니다.
    if (finished) return;

    // 게임 종료 상태로 변경합니다.
    finished = true;

    // 추가적인 정답 선택을 막습니다.
    locked = true;

    // 기존 애니메이션이 더 이상 유효하지 않도록 공격 번호를 증가시킵니다.
    actionToken++;

    // 실행 중인 타이머를 모두 취소합니다.
    clearTimers();

    // 결과 화면에 show 클래스를 추가하여 결과 창을 표시합니다.
    $("overlay").classList.add("show");

    // 성공 여부에 따라 결과 보고서 제목을 변경합니다.
    $("resultKicker").textContent = victory
        ? "CELL VISION // FINAL MISSION REPORT"
        : "CELL VISION // OPERATION FAILURE REPORT";

    // 성공이면 MISSION COMPLETE, 실패이면 MISSION FAILED를 표시합니다.
    $("resultTitle").textContent = victory
        ? "MISSION COMPLETE"
        : "MISSION FAILED";

    // 성공과 실패에 따라 결과 제목의 색상 클래스를 변경합니다.
    $("resultTitle").className =
        "result-title " + (victory ? "win" : "fail");

    // 임무 결과 상태를 표시합니다.
    $("resultStatus").textContent = victory
        ? "HOSTILE FORCE NEUTRALIZED"
        : "MISSION STATUS / FAILED";

    // 성공과 실패에 따라 결과 상태 글자의 색상을 변경합니다.
    $("resultStatus").style.color =
        victory ? "#7bc9ff" : "#ff6a79";

    // 성공과 실패에 따라 서로 다른 결과 설명을 표시합니다.
    // ${}는 템플릿 문자열 안에 변수 값을 삽입하는 문법입니다.
    $("resultDesc").innerHTML = victory
        ? `BLACK VEIL의 적대 세력이 무력화되었습니다.<br>
           세포 교란 계획이 차단되었으며, 생물학적 위협이 제거되었습니다.<br>
           확보한 생물학적 정보를 바탕으로 임무 목표를 완수했습니다.<br><br>
           정답: ${correctTotal} / 오답: ${wrongTotal}<br>
           <strong style="color:#7bc9ff;letter-spacing:1px;">
           ALL OBJECTIVES COMPLETE
           </strong><br><br>
           <span style="color:#c9d8e7;">
           작전 성공. 모든 대원은 기지로 복귀하십시오.
           </span>`
        : `작전 수행 중 대원의 체력이 모두 소진되었습니다.<br>
           정답: ${correctTotal} / 오답: ${wrongTotal}<br>
           임무에 실패했습니다. 재정비 후 다시 작전을 시작하십시오.`;

    // 성공·실패 화면 모두 복귀 버튼을 제공합니다.
    $("retryButton").style.display =
        victory ? "none" : "inline-block";

    // 메인 화면 복귀 버튼을 표시합니다.
    $("returnButton").style.display = "inline-block";

    // 다음 문제 버튼을 비활성화합니다.
    $("nextButton").disabled = true;

    // 화면에 남아 있는 발사체를 숨깁니다.
    $("projectile").style.display = "none";

    // 화면에 남아 있는 폭발 효과를 숨깁니다.
    $("blast").style.display = "none";

    // 모든 선택지 버튼을 비활성화합니다.
    [...$("answers").querySelectorAll("button")].forEach(
        button => button.disabled = true
    );
}


/* =========================================================
   21. 게임 재시작 함수
   ========================================================= */

// 게임을 처음 상태로 되돌리고 새로운 문제를 준비하는 함수입니다.
function restartGame() {

    // 이전 공격의 애니메이션이 현재 게임에 영향을 주지 않도록 번호를 증가시킵니다.
    actionToken++;

    // 이전 게임에서 실행 중이던 모든 타이머를 취소합니다.
    clearTimers();

    // 현재 문제 번호를 첫 번째 문제로 초기화합니다.
    questionIndex = 0;

    // 플레이어 체력을 처음 상태인 4로 되돌립니다.
    playerHP = 4;

    // 적 체력을 처음 상태인 10으로 되돌립니다.
    enemyHP = 10;

    // 콤보 횟수를 0으로 초기화합니다.
    combo = 0;

    // 전체 정답 수를 초기화합니다.
    correctTotal = 0;

    // 전체 오답 수를 초기화합니다.
    wrongTotal = 0;

    // 문제 선택 잠금 상태를 해제합니다.
    locked = false;

    // 게임 종료 상태를 해제합니다.
    finished = false;

    // 완벽한 작전 상태를 다시 활성화합니다.
    perfectRun = true;

    // 문제 12개 중 무작위로 10개를 선택하여 새 게임에 사용합니다.
    questions = shuffle(questionBank).slice(0, 10);

    // 결과 창을 숨깁니다.
    $("overlay").classList.remove("show");

    // 이전 발사체를 숨깁니다.
    $("projectile").style.display = "none";

    // 이전 폭발 효과를 숨깁니다.
    $("blast").style.display = "none";

    // 플레이어의 피격 및 공격 애니메이션을 초기화합니다.
    $("player").classList.remove("hit", "attack");

    // 적의 피격 및 공격 애니메이션을 초기화합니다.
    $("enemy").classList.remove("hit", "attack");

    // 재시작 버튼을 다시 표시합니다.
    $("retryButton").style.display = "inline-block";

    // 메인 화면 복귀 버튼을 표시합니다.
    $("returnButton").style.display = "inline-block";

    // 기본 무기를 장착합니다.
    setWeapon("rifle");

    // 체력과 콤보 정보를 화면에 반영합니다.
    renderBars();

    // 첫 번째 문제를 화면에 표시합니다.
    loadQuestion();
}


/* =========================================================
   22. 버튼 이벤트 연결 및 게임 시작
   ========================================================= */

// NEXT QUESTION 버튼을 클릭했을 때 실행되는 이벤트입니다.
$("nextButton").addEventListener("click", () => {

    // 게임이 끝났거나 버튼이 비활성화되어 있다면 실행하지 않습니다.
    if (finished || $("nextButton").disabled) return;

    // 다음 문제로 이동하기 위해 문제 번호를 1 증가시킵니다.
    questionIndex++;

    // 현재 문제 번호가 준비된 문제 개수 이상이라면 추가 문제를 준비합니다.
    if (questionIndex >= questions.length) {

        // 문제 은행의 순서를 섞어 기존 문제 배열 뒤에 추가합니다.
        questions = questions.concat(shuffle(questionBank));
    }

    // 다음 문제를 화면에 표시합니다.
    loadQuestion();
});


// 재시작 버튼을 클릭하면 restartGame 함수를 실행합니다.
$("retryButton").addEventListener("click", restartGame);

// 메인 화면 복귀 버튼을 클릭하면 returnToBase 함수를 실행합니다.
$("returnButton").addEventListener("click", returnToBase);


// HTML 문서가 실행되면 게임을 처음 상태로 초기화하고 시작합니다.
restartGame();
</script>
</body>
</html>
"""

# 위에서 작성한 HTML, CSS, JavaScript 문자열을 Streamlit 화면에 출력합니다.
# height=900은 게임 화면의 높이를 900px로 설정한다는 의미입니다.
# scrolling=True는 내용이 화면 높이를 넘어가면 스크롤할 수 있도록 설정합니다.
components.html(game_html, height=900, scrolling=True)
