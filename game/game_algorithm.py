from random import randrange,shuffle
from sys import stdin
input = stdin.readline()

#정답 생성
def Create_numbers() :
    arr = [str(_) for _ in range(0,10)]
    arr = shuffle(arr)[:4]

#def Create_numbers() :
#    s = set()
#    while s.__len__()<4:
#        s.add(randrange(0,10))

    print("정답 생성 완료")
    print("게임 시작")

#입력값 체크 #######
def Check_input(num) :
    num.split()


#정답 체크
def Check_number(num, number) :
    Strike = 0
    Ball = 0
    for i in range(0,4):
        if num[i] in number :
            if num[i] == number[i] :
                Strike = Strike + 1
            else :
                Ball = Ball + 1
    return Strike , Ball

#게임 진행
Count = 0  #시도 횟수
Strike = 0  #스트라이크
Ball = 0  #볼

while Strike != 4 :
    num = input("0~9 사이의 중복되지 않는 숫자 4개를 입력하세요. ")
    if not Check_number(num) :
        print("0~9 사이의 중복되지 않는 숫자 4개를 입력하세요. ")
        continue
    count = count + 1
    Strike, Ball = Check_number(num)
    print(" %d번째 시도 => %d Strike, %d Ball" %Count, Strike, Ball)