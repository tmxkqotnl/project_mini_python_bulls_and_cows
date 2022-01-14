import datetime
from random import randrange
from typing import Union
from uuid import UUID, uuid4
from dotenv import load_dotenv
from controller.db_controller import create_database, drop_database
from db.db import DB
from lib.lib import spread_dict
import os
import db.query as q

load_dotenv()
db_info: dict[str, str] = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "host": os.environ["host"],
    "port": os.environ["port"],
}

def db_init():
    
    db = DB()
    # 데이터베이스 생성을 위한 시나리오
    info_str = spread_dict(db_info)
    db.connect(info_str)
    db_name = "test"

    # 데이터베이스 drop and create
    drop_database(db, db_name)  # DB 사용중이면 에러터짐
    create_database(db, db_name)
    db.close()

    # DB 재연결 및 테이블 재생성 시나리오
    db_info["dbname"] = db_name
    info_str = spread_dict(db_info)
    db.connect(info_str)

    # rank 테이블 생성
    db.execute_query_no_return(q.create_table)
    for i in range(10):
        sample_data: dict[str, Union[str,UUID, datetime.date, int]] = {
            "id_": uuid4(),
            "name": "A" + str(randrange(10, 100)),
            "start_dt": datetime.date(
                randrange(2000, 2022), randrange(1, 12), randrange(1, 28)
            ),
            "end_dt": datetime.date(
                randrange(2000, 2022), randrange(1, 12), randrange(1, 28)
            ),
            "attemps": randrange(10, 100),
        }
        sample_data_query: str = "insert into rank(id,name,start_dt,end_dt,attemps) values('{}','{}','{}','{}',{})".format(
            sample_data["id_"],
            sample_data["name"],
            sample_data["start_dt"],
            sample_data["end_dt"],
            sample_data["attemps"]
        )
        db.execute_query_no_return(sample_data_query)
    print("sample inserted")

    db.close()
