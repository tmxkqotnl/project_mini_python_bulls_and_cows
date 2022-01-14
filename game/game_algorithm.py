from random import shuffle
from sys import stdin
from typing import Any, Union

from lib.lib import check_type_int


def create_numbers() -> list[int]:
    arr = [_ for _ in range(0, 10)]
    shuffle(arr)
    return arr[:4]


def get_input()->Any:
    print("\n숫자(0~9) 4개를 입력해주세요! EX. 1 2 3 4")
    print("\n** 포기하시려면 n을 입력해주세요! **\n")
    inp = []
    while True:
        inp:Union[list[str],list[int]] = stdin.readline().split()
        inp_set = set(inp)
        if 'n' in inp:
            return []
        if inp_set.__len__() != 4 or inp.__len__() != 4 or not check_type_int(inp):
            print("띄어쓰기 구분 고유한 4개의 숫자(0~9)를 입력해주세요!")
            continue
        else:
            inp = list(map(int,inp))    
        if list(filter(lambda x:x >= 10 or x < 0, inp)).__len__() > 0:
            print("0부터 9까지의 숫자를 입력해주세요!")
            continue
        break

    return inp


def Check_number(ans: list[int], my_ans: list[int])->list[int]:
    Strike = 0
    Ball = 0
    for i in range(0, 4):
        if my_ans[i] in ans:
            if my_ans[i] == ans[i]:
                Strike = Strike + 1
            else:
                Ball = Ball + 1
    return [Strike, Ball]

