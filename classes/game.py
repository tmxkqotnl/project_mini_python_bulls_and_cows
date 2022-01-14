#  게임클래스

from uuid import UUID
from lib.consts import GAME_STATE


class Game:
    def __init__(self, id_:UUID, answer:list[int]=[0,0,0,0], ball:int=0, strike:int=0, situation:str=GAME_STATE['게임시작 전']):
        self.id = id_
        self.ball = ball
        self.strike = strike
        self.situation = situation
        self.answer = answer

    def get_id(self) -> UUID:         #id
        return self.id
    def set_id(self, id):     #str은 객체라서 이름을 피해주는 것이 좋음
        self.id = id

    def get_answer(self)->list[int]:
        return self.answer
    def set_answer(self, l:list[int])->None:
        self.answer = l

    def get_ball(self):        #ball, 불러오는 값이라서 self 여러번 써도 노상관
       return self.ball
    def set_ball(self, ball):
        self.ball = ball


    def get_strike(self):       #strike
        return self.strike
    def set_strike(self, strike):
        self.strike = strike


    def get_situation(self):    #situation
        return self.situation
    def set_stituation(self, situation):
        self.stituation = situation

