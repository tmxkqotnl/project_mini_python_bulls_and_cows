from db.db import DB
from game.screen import in_game
from lib.consts import DB_INFO
from lib.lib import spread_dict
from seed.sample import seed_db_init

if __name__ == "__main__":
    """
        - DB 초기 세팅(데이터베이스, 테이블 등)
        
        - 1회만 실행
        
        - python에서 seeding 방법을 모릅니다..
    """
    seed_db_init()

    # DB connect
    db = DB()
    db.connect(spread_dict(DB_INFO))

    # game start
    in_game(db)

    db.close()
    exit(0)

