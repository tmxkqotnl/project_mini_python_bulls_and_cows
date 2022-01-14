from inspect import trace
import logging
import traceback
import platform
from os import system

# 에러 로깅 데코레이터
def error_logger(f):
    def Wrapper(*args, **kargs):
        try:
            return f(*args)
        except:
            logging.error(traceback.format_exc())

    return Wrapper


# 터미널 클리너 데코레이터
def clear_terminal_by_os(f):
    # only win, mac, linux classified
    name_system = platform.system()

    def Wrapper(*args, **kargs):
        if "Windows" in name_system:
            system("cls")
            logging.info("WINDOWS")
        else:
            system("clear")
            logging.info("ELSE")

        return f(*args)

    return Wrapper


# 터미널 클리너
def clear_terminal_by_os_f():
    name_system = platform.system()

    if "Windows" in name_system:
        system("cls")
        logging.info("WINDOWS")
    else:
        system("clear")
        logging.info("ELSE")


# dict items를 string으로 변환 및 연결
def spread_dict(d: dict[str, str], separator: str = " ") -> str:
    items = []
    for k, v in d.items():
        val = "{}={}".format(k, v)
        items.append(val)

    return separator.join(items)


# 문자열에 대한 숫자 타입변환 가능여부 검사
def check_type_int(data: list[str]) -> bool:
    if len(data) == 0:
        return False

    for i in data:
        if not i.isnumeric():
            return False
    return True
