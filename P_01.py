#개인이 하면서 필요하다고 생각해서 추가한것
#저장 없이 게임 나가기
#임무 저장도 추가함


import json
import os


#===입력기록리스트===
입력기록 = []


#===저장====
def 게임저장():
    저장데이터 = {
        "protagonist": {
            "배고픔": protagonist["배고픔"],
            "HP": protagonist["HP"],
            "현재위치": protagonist["현재위치"],
            "가방": protagonist["가방"],
            "주머니": protagonist["주머니"],
        },
        "environment": {
            "현재시각": enviroment["현재시각"]
        },
        "settings": {
            "난이도": settings["난이도"]
        },
        "입력기록": 입력기록,
        "임무목록": protagonist["임무목록"],
        "입장여부": protagonist["입장여부"]
    }
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(저장데이터, f, ensure_ascii=False, indent=4)
    print("저장 완료!")


#===불러오기===
def 불러오기():
    print("=== 저장 파일 목록 ===")
    
    # 현재 폴더의 json 파일 목록
    json파일들 = [f for f in os.listdir(".") if f.endswith(".json")]
    
    if len(json파일들) == 0:
        print("현재 폴더에 저장 파일이 없어.")
    else:
        for i, 파일 in enumerate(json파일들):
            print(f"{i+1}. {파일}")
    
    print("-----")
    파일입력 = input("숫자 입력 (현재폴더) 또는 경로 직접 입력: ")
    
    # 숫자로 입력한 경우
    if 파일입력.isdigit():
        인덱스 = int(파일입력) - 1
        if 0 <= 인덱스 < len(json파일들):
            파일경로 = json파일들[인덱스]
        else:
            print("없는 번호야.")
            return
    else:
        # 경로 직접 입력 (상대경로, 절대경로 모두 가능)
        파일경로 = 파일입력

    # 파일 불러오기
    try:
        with open(파일경로, "r", encoding="utf-8") as f:
            저장데이터 = json.load(f)
        
        # 각 변수에 할당
        protagonist["배고픔"] = 저장데이터["protagonist"]["배고픔"]
        protagonist["HP"] = 저장데이터["protagonist"]["HP"]
        protagonist["현재위치"] = tuple(저장데이터["protagonist"]["현재위치"])
        protagonist["가방"] = 저장데이터["protagonist"]["가방"]
        protagonist["주머니"] = 저장데이터["protagonist"]["주머니"]
        protagonist["임무목록"] = 저장데이터["임무목록"]
        protagonist["입장여부"] = 저장데이터["입장여부"]

        enviroment["현재시각"] = 저장데이터["environment"]["현재시각"]
        settings["난이도"] = 저장데이터["settings"]["난이도"]
        입력기록.clear()
        입력기록.extend(저장데이터["입력기록"])

        print(f"불러오기 완료! 현재 위치: {game_map[protagonist['현재위치']]}")

    except FileNotFoundError:
        print("파일을 찾을 수 없어.")
    except Exception as e:
        print(f"불러오기 실패: {e}")


#===게임설정===
settings = {
    "난이도": "보통"
}

enviroment = {
    "현재시각" : 11
}

protagonist = {
    "배고픔": True,
    "현재위치": (0, 0),
    # "연대앞 버스정류장"에서 (0,0)으로 고침 이유: game_map의 key는 (0, 0) 같은 좌표(tuple) 인데, 현재위치를 문자열로 저장해서 찾을 수가 없어서
    "HP": 10,
    "주머니": {
        "체크카드": {
            "이름": "체크카드",
            "계좌잔액": 10000
        }
    },
    "가방": [],
    "임무목록": [],
    "입장여부": False
}

#===MAP===
game_map = {
    (0, 0): "연대앞 버스정류장",
    (0, 1): "정문",
    (0, 2): "스타벅스",
    (0, 3): "세브란스병원 버스정류장",

    (1, 0): "공학원",
    (1, 1): "백양로1",
    (1, 2): "공터1",
    (1, 3): "암병원",
    (1, 4): "의과대학",

    (2, 0): "공학관",
    (2, 1): "백양로2",
    (2, 2): "백주년기념관",
    (2, 3): "안과병원",
    (2, 4): "제웅관",

    (3, 0): "체육관",
    (3, 1): "백양로3",
    (3, 2): "공터2",
    (3, 3): "광혜원",
    (3, 4): "어린이병원",
    (3, 5): "세브란스병원",

    (4, 0): "중앙도서관",
    (4, 1): "독수리상",
    (4, 2): "학생회관",
    (4, 3): "루스채플",
    (4, 4): "재활병원",
    (4, 5): "치과대학",

    (5, 0): "백양관",
    (5, 1): "백양로5",
    (5, 2): "대강당",
    (5, 3): "음악관",
    (5, 4): "알렌관",
    (5, 5): "ABMRC",

    (6, 4): "새천년관",
    (6, 5): "이윤재관",
}


#===MOVE===
방향키 = {
    "북": (1, 0),
    "남": (-1, 0),
    "동": (0, 1),
    "서": (0, -1),
}


#===난이도 설정===
while True:
    난이도 = input("난이도를 선택하세요 (쉬움/보통/어려움): ")
    if 난이도 in ["쉬움", "보통", "어려움"]:
        settings["난이도"] = 난이도
        print(f"난이도 {난이도}으로로 설정 완료 했습니다!")
        break
    else:
        print("쉬움, 보통, 어려움 중에서 입력해주세요.")


#===난이도보기===
def 난이도보기():
    print(f"현재 난이도: {settings['난이도']}")
    변경 = input("난이도를 변경하시겠습니까? (쉬움/보통/어려움/취소): ")
    if 변경 in ["쉬움", "보통", "어려움"]:
        settings["난이도"] = 변경
        print(f"난이도를 {변경}으로 변경했어.")
    else:
        print("변경 취소.")


#===INTRO===
def intro():
    print()
    print("="*50)
    print("텍스트기반게임")
    print("="*50)
    print("""
    송도 생활을 마치고 신촌에 처음 도착했다. 연대앞 버스정류장이다.
    현재 시각은 11시.
    1시 수업은 임무완료를 보고할 장소는 이윤재관 511호다.
    배가 고프다.""")
intro()


#===가방===
def 가방보기():
    if len(protagonist["가방"]) == 0:
        print("가방에는 아무것도 없어")
    else:
        print("===가방===")
        for i, 물건 in enumerate(protagonist["가방"]):
            print(f"{i+1}. {물건["이름"]}")
    
        사용 = input("사용할 물건의 이름 또는 번호를 입력하세요 (취소: 엔터): ")
        if 사용 == "":
            return
        
        for i, 물건 in enumerate(protagonist["가방"]):
            if 사용 == 물건["이름"] or 사용 == str(i+1):
                protagonist["HP"] += 물건["HP회복"]
                protagonist["가방"].pop(i)
                print(f"{물건['이름']}을 먹었어. HP가 {물건['HP회복']}만큼 회복됐어. HP: {protagonist['HP']}")
                return
        print("그런 물건은 없어.")


#===상태출력===
def 상태보기():
    현재좌표 = protagonist["현재위치"]
    print("=== 상태 ===")
    print(f"HP: {protagonist['HP']}")
    print(f"계좌 잔액: {protagonist['주머니']['체크카드']['계좌잔액']}원")
    print(f"현재 위치: {game_map[현재좌표]}")
    
    print("--- 이웃 칸 ---")
    for 방향, (행변화, 열변화) in 방향키.items():
        이웃좌표 = (현재좌표[0] + 행변화, 현재좌표[1] + 열변화)
        if 이웃좌표 in game_map:
            print(f"{방향}: {game_map[이웃좌표]}")
        else:
            print(f"{방향}: 막혀있음")

#===상호작용===
장소상호작용 = {
    "정문": {
        "입장": True
    },
    "학생회관": {
        "상점": [
            {"이름": "두쫀쿠", "가격": 5000, "HP회복": 25},
            {"이름": "카페라떼", "가격": 2500, "HP회복": 25},
        ]
    },
    "독수리상": {
        "임무수령": ["임무1", "임무2"]
    },
    "이윤재관": {
        "임무보고": True
    }
}


#==상점===
def 상점(장소이름):
    상점목록 = 장소상호작용[장소이름]["상점"]
    print(f"=== {장소이름} 상점 ===")
    for i, 물건 in enumerate(상점목록):
        print(f"{i+1}. {물건['이름']} - {물건['가격']}원")
    
    선택 = input("구매할 물건 번호를 입력하세요 (취소: 엔터): ")
    if 선택 == "":
        return
    
    for i, 물건 in enumerate(상점목록):
        if 선택 == str(i+1) or 선택 == 물건["이름"]:
            if protagonist["주머니"]["체크카드"]["계좌잔액"] >= 물건["가격"]:
                protagonist["주머니"]["체크카드"]["계좌잔액"] -= 물건["가격"]
                protagonist["가방"].append(물건)
                print(f"{물건['이름']}을 구매했어. 잔액: {protagonist['주머니']['체크카드']['계좌잔액']}원")
            else:
                print("잔액이 부족해.")
            return
    print("그런 물건은 없어.")


#===임무데이터===c
임무데이터 = {
    "임무0": {
        "이름": "첫 번째 임무",
        "설명": "독수리상에서 임무를 받고 이윤재관에 보고하라.",
        "완료": False
    },
    "임무1": {
        "이름": "교내 부조리 수사",
        "설명": "교내 어딘가에서 부조리가 일어나고있다. 이동하고 상호작용을 해서 부조리를 찾아서 보고하라.",
        "완료": False
    },
    "임무2": {
        "이름": "교내 위생사건 수사",
        "설명": "학생들이 단체로 식중독에 걸렸다. 이동하고 상호작용을 해서 위생사건의 원인을 찾아서 보고하라.",
        "완료": False
    }
}


#===임무데이터출력===c
def 임무보기():
    if len(protagonist["임무목록"]) == 0:
        print("현재 임무가 없어.")
    else:
        print("=== 임무 목록 ===")
        for 임무키 in protagonist["임무목록"]:
            임무 = 임무데이터[임무키]
            완료여부 = "✅" if 임무["완료"] else "❌"
            print(f"{완료여부} {임무['이름']}: {임무['설명']}")


#===상호작용===c
def 상호작용():
    현재장소 = game_map[protagonist["현재위치"]]

    if 현재장소 not in 장소상호작용:
        print("여기서는 상호작용할 수 없어.")
        return
    
    # 학생회관 - 상점
    if "상점" in 장소상호작용[현재장소]:
        상점(현재장소)
    
    # 정문 - 입장
    elif "입장" in 장소상호작용[현재장소]:
        print("학교에 입장하시겠습니까?")
        print("1. 예")
        선택 = input("입력: ")
        if 선택 == "예" or 선택 == "1":
            protagonist["입장여부"] = True
            print("학교에 입장했다.")
        else:
            print("입장을 취소했다.")

    # 독수리상 - 임무 수령
    elif "임무수령" in 장소상호작용[현재장소]:
        새임무들 = 장소상호작용[현재장소]["임무수령"]
        추가됨 = False
        for 임무키 in 새임무들:
            if 임무키 not in protagonist["임무목록"]:
                protagonist["임무목록"].append(임무키)
                print(f"새 임무를 받았어: {임무데이터[임무키]['이름']}")
                print(f"  {임무데이터[임무키]['설명']}")
                추가됨 = True
        if not 추가됨:
            print("이미 모든 임무를 받았어.")

    # 이윤재관 - 임무 보고
    elif "임무보고" in 장소상호작용[현재장소]:
        if "임무1" not in protagonist["임무목록"] and "임무2" not in protagonist["임무목록"]:
            print("독수리상에서 먼저 임무를 받아와.")
        else:
            미완료 = [k for k in protagonist["임무목록"] if not 임무데이터[k]["완료"]]
            if len(미완료) > 0:
                print("아직 완료하지 못한 임무가 있어.")
                for 임무키 in 미완료:
                    print(f"  - {임무데이터[임무키]['이름']}")
            else:
                print("모든 임무를 완료했어! 보고 완료!")


#===메인 루프===
while True:
    현재좌표 = protagonist["현재위치"]
    print(f"\n현재 위치: {game_map[현재좌표]}")

    명령 = input("입력 (북/남/동/서/가방/상태/임무/상호작용/난이도/저장/불러오기/end/exit): ")

    if 명령 == "가방":
        가방보기()
        continue

    elif 명령 == "상태":
        상태보기()
        continue

    elif 명령 == "저장":
        게임저장()
        continue

#임의로 게임 저장%종료 버튼 만듦
    elif 명령 == "end":
        게임저장()
        print("게임을 종료합니다.")
        break

#임의로 게임 종료 버튼 만듦
    elif 명령 == "exit":
        print("게임을 종료합니다.")
        break

    elif 명령 == "불러오기":
        불러오기()
        continue
    
    elif 명령 == "임무":
        임무보기()
        continue
    
    elif 명령 == "난이도":
        난이도보기()
        continue

    #방향키
    elif 명령 in 방향키:
        행변화, 열변화 = 방향키[명령]
        새좌표 = (현재좌표[0] + 행변화, 현재좌표[1] + 열변화)

        if 새좌표 not in game_map:
            print("그 방향은 막혔어.")
            continue

        # 정문 안쪽으로 이동 시 입장 여부 체크
        현재장소 = game_map[현재좌표]
        다음장소 = game_map[새좌표]
        정문안쪽 = ["백양로1", "공터1", "암병원", "의과대학",
                   "공학관", "공학원", "백양로2", "백주년기념관",
                   "안과병원", "제웅관", "체육관", "백양로3",
                   "공터2", "광혜원", "어린이병원", "세브란스병원",
                   "중앙도서관", "독수리상", "학생회관", "루스채플",
                   "재활병원", "치과대학", "백양관", "백양로5",
                   "대강당", "음악관", "알렌관", "ABMRC",
                   "새천년관", "이윤재관"]

        if 다음장소 in 정문안쪽 and not protagonist["입장여부"]:
            print("정문에서 먼저 입장해야 해.")
            continue

        protagonist["현재위치"] = 새좌표
        HP감소량 = {"쉬움": 0.5, "보통": 1, "어려움": 2}
        protagonist["HP"] -= HP감소량[settings["난이도"]]
        현재장소 = game_map[새좌표]
        print(f"{명령}쪽으로 이동했어. {현재장소}에 도착했어.")
        print(f"HP: {protagonist['HP']}")

        # 정문 도착 시 임무0 자동 부여
        if 현재장소 == "정문" and "임무0" not in protagonist["임무목록"]:
            protagonist["임무목록"].append("임무0")
            print("\n[임무] 독수리상에서 임무를 받고 이윤재관에 보고하라!")
    

    elif 명령 == "상호작용":
        상호작용()

    #메인루프 이동 부분에 입장 체크 추가
    

    else:
        print("북/남/동/서/가방/상태/저장/불러오기/end/exit 중에서 입력해줘.")