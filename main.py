from dotenv import load_dotenv
import os
from db.db import DB
from game.screen import in_game
from lib.lib import spread_dict
from seed.sample import db_init

load_dotenv()
db_info: dict[str, str] = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "host": os.environ["host"],
    "port": os.environ["port"],
    "dbname":os.environ['dbname']
}


if __name__ == "__main__":
    db_init() # python에서 seeding 방법을 모릅니다..
    
    db = DB()
    db.connect(spread_dict(db_info))
    in_game(db)
    
    db.close()
    exit(0)

