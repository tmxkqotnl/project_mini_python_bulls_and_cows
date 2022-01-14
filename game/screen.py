from controller.db_controller import select_top10_minimum_attemps
from game.game_algorithm import create_numbers
from lib.lib import clear_terminal_by_os
from db.db import DB
from classes.player import Player
from classes.game import Game
from uuid import UUID, uuid4
import sys


@clear_terminal_by_os
def init_player():
    print('\n이름을 입력해주세요! : ',end='')
    name = sys.stdin.readline().replace('\n','').strip()
    this_player:Player = Player(uuid4(),0,name)
    return this_player   

def init_game(player_id:UUID):
    ans = create_numbers()
    this_game = Game(player_id,ans)
    return this_game

# @clear_terminal_by_os
def game_start(p:Player,g:Game):
    print(1)

@clear_terminal_by_os
def rank_output(db:DB):
    vals,columns = select_top10_minimum_attemps(db)
    print(columns)
    for i in vals:
        print('%d위: ' % (i+1), end='')
        print("%5s %5d" % (vals[i][0], vals[i][1]))

@clear_terminal_by_os
def in_game(db:DB):
    # print("뽜밤뽜밤 숫자 야구의 세계에 온것을 환영합니다!\n세계의 균형을 어지럽히는 악당을 부디 물리쳐주세요!\n")
    while True:
        print("1. 적을 무찌르자!")
        print("2. 랭?킹")
        print("3. 고만하고 집에가기\n")
        e_c = input("할 일을 정해주세요 : ")
        if e_c == '1':
            this_player = init_player()
            this_game = init_game(this_player.get_id())
            game_start(this_player,this_game)
        elif e_c == '2':
            rank_output(db)
        elif e_c == '3':
            print("다음번엔 꼭 적을 무찔러 주세요!")
            break
        else:
            print("그게 아니에요!")
        print(" ")

