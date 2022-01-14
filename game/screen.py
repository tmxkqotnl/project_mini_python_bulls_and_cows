from typing import Any
from controller.db_controller import insert_game_result, select_top10_minimum_attemps
from game.game_algorithm import Check_number, create_numbers, get_input
from lib.consts import GAME_STATE
from lib.lib import clear_terminal_by_os, clear_terminal_by_os_f
from db.db import DB
from classes.player import Player
from classes.game import Game
from uuid import UUID, uuid4
import sys


@clear_terminal_by_os
def init_player()->Player:
    print("\n이름을 입력해주세요! : ", end="")
    name = sys.stdin.readline().replace("\n", "").strip()
    this_player: Player = Player(uuid4(), 0, name)
    return this_player


def init_game(player_id: UUID)->Game:
    ans = create_numbers()
    this_game = Game(player_id, ans)
    return this_game


def input_rank(db: DB, p: Player, g: Game)->Any:
    while True:
        res = input("랭킹을 저장하시겠습니까? 'y' or 'n' ")
        if res in ["y", "Y"]:
            return insert_game_result(db, p, g)
        elif res in ["n", "N"]:
            clear_terminal_by_os_f()
            print("okay goodbye")
            return
        else:
            print("yes or no 중에 입력하세요")


# @clear_terminal_by_os
def game_start(db: DB, p: Player, g: Game) -> Any:
    print(g.get_answer())  # 나중에 삭제
    my_ans: list[int] = get_input()

    if my_ans.__len__() == 0:
        print("\n이번 게임 종료\n")
        g.set_stituation(GAME_STATE["게임 끝"])
        return None

    clear_terminal_by_os_f()
    p.set_attemp(p.get_attempt() + 1)
    s, b = Check_number(my_ans, g.get_answer())

    if s == 4:
        print("이겼습니다!")
        g.set_stituation(GAME_STATE["게임 끝"])
        return input_rank(db, p, g)

    print("***************")
    print("\n\tStrike : {}, Ball : {}\n".format(s, b))
    print("***************")
    print("\n\t나의 답안 : {}\n".format(my_ans))
    print("***************")

    return game_start(db, p, g)


@clear_terminal_by_os
def rank_output(db: DB)->None:
    vals, columns = select_top10_minimum_attemps(db)
    print('\t순위%30s %3s'%('이름','횟수'))
    for i in range(len(vals)):
        print("\t%2d위: " % (i + 1), end="")
        print("%30s %5d" % (vals[i][0], vals[i][1]))


@clear_terminal_by_os
def in_game(db: DB)->None:
    while True:
        print("1. 게임 시작하기")
        print("2. 랭킹 확인하기")
        print("3. 끝내기")

        e_c = input("번호를 입력해주세요 : ").replace("\n", "")
        if e_c == "1":
            this_player = init_player()
            this_game = init_game(this_player.get_id())
            game_start(db, this_player, this_game)
        elif e_c == "2":
            rank_output(db)
        elif e_c == "3":
            print("안녕 ㅠㅠ")
            break
        else:
            print("1번부터 3번까지의 번호를 입력해주세요!")

