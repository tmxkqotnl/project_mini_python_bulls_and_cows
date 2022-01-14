from dotenv import load_dotenv
import os
from db.db import DB
from game.screen import in_game
from lib.lib import spread_dict
from seed.sample import seed_db_init

load_dotenv()
db_info: dict[str, str] = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "host": os.environ["host"],
    "port": os.environ["port"],
    "dbname":os.environ['dbname']
}


if __name__ == "__main__":
    # DB 초기 세팅(데이터베이스, 테이블 등)
    # python에서 seeding 방법을 모릅니다..
    seed_db_init() 
    
    # DB connect
    db = DB()
    db.connect(spread_dict(db_info))
    
    # game start
    in_game(db) 
    
    db.close()
    exit(0)

