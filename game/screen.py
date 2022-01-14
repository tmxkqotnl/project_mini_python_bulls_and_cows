from controller.db_controller import select_top5_minimum_attemps
from lib.lib import clear_terminal_by_os
from db.db import DB

def start_screen(db:DB):
    print("뽜밤뽜밤 숫자 야구의 세계에 온것을 환영합니다!\n세계의 균형을 어지럽히는 악당을 부디 물리쳐주세요!\n")
    while True:
        print("1. 적을 무찌르자!")
        print("2. 랭?킹")
        print("3. 고만하고 집에가기\n")
        e_c = input("할 일을 정해주세요 : ")
        if e_c == '1':
            id_input()
        elif e_c == '2':
            rank_output(db)
        elif e_c == '3':
            print("다음번엔 꼭 적을 무찔러 주세요!")
            break
        else:
            print("그게 아니에요!")
        print(" ")

@clear_terminal_by_os
def id_input():
    global p_id
    p_id = input("당신의 이름은 : ")
    print("뽜밤뽜밤 동료로 합류했습니다!")
    game_start()    

@clear_terminal_by_os
def game_start():
    print("장로 : 적이 나타났네! 건투를 비네 %s용사여!\n야구알파고 : 인간 시대의 끝이 도래했다." % p_id)

@clear_terminal_by_os
def rank_output(db:DB):
    vals,columns = select_top5_minimum_attemps(db)
    print(columns)
    for i in vals:
        print(i)
