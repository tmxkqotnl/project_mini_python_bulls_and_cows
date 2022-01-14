from random import shuffle
from sys import stdin


#정답 생성
def create_numbers()-> list[int]:
    arr = [str(_) for _ in range(0,10)]
    shuffle(arr)
    partial = arr[:4]
    

    print("정답 생성 완료")
    print("게임 시작")
    return list(map(int,partial))

#입력값 체크 #######
def get_input() :
    print('숫자(0~9) 4개를 입력해주세요! EX. 1 2 3 4')
    
    inp = None
    while True:
        input = stdin.readline
        inp = list(map(int,input().split()))
        if inp.__len__() !=4:
            print('띄어쓰기 구분 4개의 숫자(0~9)를 입력해주세요!')
            continue
        elif list(filter(lambda x:x>=10 or x<0,inp)).__len__() > 0:
            print('0부터 9까지의 숫자를 입력해주세요!')
            continue
        break
    
    return inp

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