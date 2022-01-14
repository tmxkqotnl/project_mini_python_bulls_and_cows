#  게임클래스

class Game:
    def __init__(self, id, ball, strike, situation):
        self.id = id
        self.ball = ball
        self.strike = strike
        self.situation = situation

    def get_id(self):         #id
        return self.id
    def set_id(self, id):     #str은 객체라서 이름을 피해주는 것이 좋음
        self.id = id


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

