import datetime

class Player :
    def __init__(self, id, attempt) :
        self.id = id
        self.attempt = attempt

    def set_id(self, id) :
        self.id = id
    def get_id(self) :
        return self.id

    def set_attemp(self, attempt) :
        self.attempt = attempt    
    def get_attempt(self) :
        return self.attempt
    
class Time(Player) :
    
    def __init__(self, starttime, endtime) :
        self.starttime =  datetime.datetime(datetime.datetime.today())
        self.endtime = None

    def set_starttime(self) :
        self.start_time = datetime.datetime(datetime.datetime.today())

    def set_endtime(self) :
        self.end_time = datetime.datetime(datetime.datetime.today())


#낙현님이 
a=Player('mj', 5)
#a.set_id(input('ID를 입력하세요 : '))
print(a.get_id())
#a.set_attempt(int(input('#게임이 종료되면 자동으로 시도횟수가 나올것')))
print(a.get_attempt())
#print(a.get_id)
#print(a.get_attempt)