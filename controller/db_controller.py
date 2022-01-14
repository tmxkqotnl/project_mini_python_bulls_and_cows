from ctypes import Union
from datetime import datetime
from typing import Any
from classes.game import Game
from classes.player import Player
from db.db import DB
from lib.lib import error_logger, spread_dict
from psycopg2 import sql
from uuid import UUID, uuid4


@error_logger
def insert_game_result(db: DB, p: Player, g: Game) -> None:
    q = "insert into rank values('{}','{}','{}','{}',{})".format(
        p.get_id(), p.get_name(), g.get_starttime(), datetime.now(), p.get_attempt()
    )

    return db.execute_query_no_return(q)


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


@error_logger
def select_top10_minimum_attemps(db: DB) -> list[list[tuple], list[str]]:
    query = """select name, attemps from rank order by attemps limit 10;"""
    return db.execute_query_has_return(query)


@error_logger
def select_top10_minimum_time(db: DB) -> list[list[tuple], list[str]]:
    query = """select name, min(end_dt - start_dt) as takes_time from rank group by name order by takes_time limit 5;"""
    return db.execute_query_has_return(query)
