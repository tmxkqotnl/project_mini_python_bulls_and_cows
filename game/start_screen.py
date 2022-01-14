from time import sleep


# 시작화면 함수
def start_screen():
    print("장로 : 숫자 야구의 세계에 온것을 환영하네!\n숫자 야구로 세계의 균형을 어지럽히는 악당을 부디 무찔러 주게!\n")
    while True:
        print("1. 적을 무찌르기")
        print("2. 랭킹 확인하기")
        print("3. 다음에 무찌르기\n")
        e_c = input("할 일을 정하게나 : ")
        if e_c == '1':
            id_input()
        elif e_c == '2':
            rank_output()
        elif e_c == '3':
            print("다음번엔 꼭 적을 무찔러 주게나!")
            sleep(3)
            quit()
        else:
            print("목록의 숫자를 입력해 주시게")
        print(" ")


def id_input():
    global p_id
    p_id = input("당신의 이름은 : ")
    game_start()    


def game_start():
    print("장로 : 적이 나타났네! 건투를 비네 %s용사여!\n야구알파고 : 인간 시대의 끝이 도래했다." % p_id)


def rank_output():
    print("상위 랭킹")