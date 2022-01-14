from inspect import trace
import logging
import traceback
import platform
from os import system


def error_logger(f):
    def Wrapper(*args, **kargs):
        try:
            return f(*args)
        except:
            logging.error(traceback.format_exc())

    return Wrapper


def clear_terminal_by_os(f):
    # only win, mac, linux classified
    name_system = platform.system()
    def Wrapper(*args, **kargs):
        if "Windows" in name_system:
            system("cls")
        else:
            system("clear")
        
        return f(*args)

    return Wrapper
def clear_terminal_by_os_f():
    name_system = platform.system()
    
    if "Windows" in name_system:
        system("cls")
    else:
        system("clear")
        

def spread_dict(d: dict[str, str], separator: str = " ") -> str:
    items = []
    for k, v in d.items():
        val = "{}={}".format(k, v)
        items.append(val)

    return separator.join(items)


def check_type_int(data:list[str]):
    for i in data:
            if not i.isnumeric():
                return False
    return True