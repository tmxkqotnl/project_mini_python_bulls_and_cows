from time import sleep


def start_screen():
    print("뽜밤뽜밤 숫자 야구의 세계에 온것을 환영합니다!\n세계의 균형을 어지럽히는 악당을 부디 물리쳐주세요!\n")
    while True:
        print("1. 적을 무찌르자!")
        print("2. 랭?킹")
        print("3. 고만하고 집에가기\n")
        e_c = input("할 일을 정해주세요 : ")
        if e_c == '1':
            id_input()
        elif e_c == '2':
            rank_output()
        elif e_c == '3':
            print("다음번엔 꼭 적을 무찔러 주세요!")
            sleep(3)
            quit()
        else:
            print("그게 아니에요!")
        print(" ")


def id_input():
    global p_id
    p_id = input("당신의 이름은 : ")
    print("뽜밤뽜밤 동료로 합류했습니다!")
    game_start()    


def game_start():
    print("장로 : 적이 나타났네! 건투를 비네 %s용사여!\n야구알파고 : 인간 시대의 끝이 도래했다." % p_id)


def rank_output():
    print("상위 랭킹")
