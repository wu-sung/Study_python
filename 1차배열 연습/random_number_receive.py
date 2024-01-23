import random

def password():
    numstr = "0123456789"
    password = " "

    for i in range(6):
        index = random.randrange(len(numstr))
        password = password + numstr[index]
    return password
    

print("본인인증을 위해서 발송된 숫자를 입력하세요 : ", password())
