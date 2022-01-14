import datetime
import uuid


class Player:
    def __init__(self, id:uuid.UUID, attempt:int, name:str):
        self.id = id
        self.attempt:int = attempt
        self.name:str = name

    def set_id(self, id:int):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name:str):
        self.name = name

    def get_name(self):
        return self.name

    def set_attemp(self, attempt):
        self.attempt = attempt

    def get_attempt(self):
        return self.attempt


class Time(Player):
    def __init__(self, starttime, endtime):
        self.starttime = datetime.datetime(datetime.datetime.today())
        self.endtime = None

    def set_starttime(self):
        self.start_time = datetime.datetime(datetime.datetime.today())

    def set_endtime(self):
        self.end_time = datetime.datetime(datetime.datetime.today())
