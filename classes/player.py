from uuid import UUID


class Player:
    def __init__(self, ids:UUID, attempt:int, name:str):
        self.__id = ids
        self.__attempt:int = attempt
        self.__name:str = name

    def set_id(self, ids:int)->None:
        self.__id = ids

    def get_id(self)->UUID:
        return self.__id

    def set_name(self, name:str)->None:
        self.__name = name

    def get_name(self)->str:
        return self.__name

    def set_attemp(self, attempt:int)->None:
        self.__attempt = attempt

    def get_attempt(self)->int:
        return self.__attempt