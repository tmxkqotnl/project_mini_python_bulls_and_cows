from datetime import datetime
from typing import Optional
from uuid import UUID
from lib.consts import GAME_STATE


class Game:
    def __init__(
        self,
        id_: UUID,
        answer: list[int] = [0, 0, 0, 0],
        ball: int = 0,
        strike: int = 0,
        situation: int = GAME_STATE["게임시작 전"],
        start_dt: datetime = datetime.now(),
        end_dt: Optional[datetime] = None,
    ):
        self.__start_dt = start_dt
        self.__end_dt = end_dt
        self.__id = id_
        self.__ball = ball
        self.__strike = strike
        self.__situation = situation
        self.__answer = answer

    def set_starttime(self)->None:
        self.__start_time = datetime.now()
        self.__end_time = datetime.now()

    def get_starttime(self) -> datetime:
        return self.__start_dt

    def get_endtime(self) -> Optional[datetime]:
        return self.__end_dt

    def get_id(self) -> UUID:  # id
        return self.__id

    def set_id(self, ids:UUID):  # str은 객체라서 이름을 피해주는 것이 좋음
        self.__id = ids

    def get_answer(self) -> list[int]:
        return self.__answer

    def set_answer(self, l: list[int]) -> None:
        self.__answer = l

    def get_ball(self)->int:  # ball, 불러오는 값이라서 self 여러번 써도 노상관
        return self.__ball

    def set_ball(self, ball:int)->None:
        self.__ball = ball

    def get_strike(self)->int:  # strike
        return self.__strike

    def set_strike(self, strike:int)->None:
        self.__strike = strike

    def get_situation(self)->int:  # situation
        return self.__situation

    def set_stituation(self, situation:int)->None:
        self.__stituation = situation

