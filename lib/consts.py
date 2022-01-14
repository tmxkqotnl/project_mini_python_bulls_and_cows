from dotenv import load_dotenv
import os

STATE: dict[str, int] = {"start": 1, "end": 0}

load_dotenv()
DB_INFO: dict[str, str] = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "host": os.environ["host"],
    "port": os.environ["port"],
    "dbname": os.environ["dbname"],
}

MENU: dict[str, str] = {"game_start": '1', "ranking_list": '2', "quit": '3'}

