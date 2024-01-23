import winsound as sd

def beepsound():
    fr = 2000
    du = 1000
    sd.Beep(fr,du)


def info(name, age, career):
    print("인적사항 = 이름 : ", name, "나이", age, "직업 : ", career)
    return

people_list = []  # 여러 사람에 대한 정보를 저장하는 리스트

while True:
    name = input("이름을 입력하세요 : ")
    age = int(input("나이를 입력하세요 : "))
    career = input("직업을 입력하세요 : ")

    person_info = {"name": name, "age": age, "career": career}
    people_list.append(person_info)

    print("입력하신 신분사항이 맞으신지 확인해 주십시요 : ", person_info)
    add = input("신분사항을 더 입력하시겠습니까? (y 또는 n)")

    if add.lower() != "y":
        print("지금까지 입력하신 정보입니다. ", people_list, end = "\n")
        beepsound()
        break