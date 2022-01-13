from db.db import DB
from lib.lib import error_logger, spread_dict
from psycopg2 import sql
import db.query as q
from uuid import uuid4

@error_logger
def insert_game_result(db:DB,game:Game)->None:
    data:dict[str,str] = {
        'id':uuid4(),
        'name':game.name,
        'start_dt':game.start,
        'end_dt':game.end,
        'attemps':game.attemps
    }
    data_str = spread_dict(data,',')
    q = "insert into rank values({})".format(data_str)

    
@error_logger
def drop_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("drop database if exists {};").format(sql.Identifier(db_name))
    )
@error_logger
def drop_all_tables(db:DB)->None:
    db.execute_query_no_return("drop table *")

@error_logger
def create_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("create database {};").format(sql.Identifier(db_name))
    )


@error_logger
def create_table(db: DB, query: str) -> None:
    db.execute_query_no_return(query)


@error_logger
def init_table(db: DB) -> None:
    db.execute_query_no_return(q.create_table)

@error_logger
def init_database(db_info: dict[str, str]) -> DB:
    db = DB()

    # 데이터베이스 생성을 위한 시나리오
    info_str = spread_dict(db_info)
    db.connect(info_str)
    db_name = "test"

    # 데이터베이스 drop and create
    drop_database(db, db_name) # DB 사용중이면 에러터짐
    create_database(db, db_name)
    db.close()

    # DB 재연결 및 테이블 재생성 시나리오
    db_info["dbname"] = db_name
    info_str = spread_dict(db_info)
    db.connect(info_str)

    # rank 테이블 생성
    create_table(db, q.create_table)

    print("DB initialized")

    return db