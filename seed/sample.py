## 개판 5분전 코드.. 리팩토링 할 것

import datetime
from random import randrange
from typing import Union
from uuid import UUID, uuid4
from controller.db_controller import create_database, drop_database
from db.db import DB
from lib.consts import DB_INFO
from lib.lib import spread_dict
import os

def seed_db_init():
    db = DB()
    # 데이터베이스 생성을 위한 시나리오
    copied:dict[str,str] = {}
    for k,v in DB_INFO.items():
        if k != 'dbname':
            copied[k] = v
    
    info_str = spread_dict(copied)
    db.connect(info_str)
    
    # 데이터베이스 drop and create
    db_name = os.environ['dbname']
    drop_database(db, db_name)  # DB 사용중이면 에러터짐
    create_database(db, db_name)
    
    db.close()

    # DB 재연결 및 테이블 재생성 시나리오
    copied['dbname'] = DB_INFO['dbname']
    info_str = spread_dict(copied)
    db.connect(info_str)

    # rank 테이블 생성
    create_table_query = """
    create table rank(id uuid primary key,name varchar(100), start_dt timestamp, end_dt timestamp, attemps integer);
    """
    db.execute_query_no_return(create_table_query)
    
    # sample 데이터 생성
    for _ in range(10):
        sample_data: dict[str, Union[str, UUID, datetime.date, int]] = {
            "id_": uuid4(),
            "name": "A" + str(randrange(10, 100)),
            "start_dt": datetime.date(
                randrange(2000, 2010), randrange(1, 12), randrange(1, 28)
            ),
            "end_dt": datetime.date(
                randrange(2011, 2021), randrange(1, 12), randrange(1, 28)
            ),
            "attemps": randrange(10, 100),
        }
        sample_data_query: str = "insert into rank(id,name,start_dt,end_dt,attemps) values('{}','{}','{}','{}',{})".format(
            sample_data["id_"],
            sample_data["name"],
            sample_data["start_dt"],
            sample_data["end_dt"],
            sample_data["attemps"],
        )
        db.execute_query_no_return(sample_data_query)

    db.close()
