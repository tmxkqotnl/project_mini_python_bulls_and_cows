from db.db import DB
from lib.lib import error_logger, spread_dict
from psycopg2 import sql
import db.query as q
from uuid import uuid4

# @error_logger
# def insert_game_result(db:DB,game:Game)->None:
#     data:dict[str,str] = {
#         'id':uuid4(),
#         'name':game.name,
#         'start_dt':game.start,
#         'end_dt':game.end,
#         'attemps':game.attemps
#     }
#     data_str = spread_dict(data,',')
#     q = "insert into rank values({})".format(data_str)
    
#     return db.execute_query_has_return(q) 

    
@error_logger
def drop_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("drop database if exists {};").format(sql.Identifier(db_name))
    )

@error_logger
def create_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("create database {};").format(sql.Identifier(db_name))
    )