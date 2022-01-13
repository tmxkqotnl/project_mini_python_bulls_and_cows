from inspect import trace
import logging
import traceback

def error_logger(f):
    def Wrapper(*args,**kargs):
        try:
            return f(*args)
        except:
            logging.error(traceback.format_exc())
    return Wrapper

def spread_dict(d:dict[str,str],separator:str=' ') -> str:
    items = []
    for k,v in d.items():
        val = '{}={}'.format(k,v)
        items.append(val)
        
    return separator.join(items)