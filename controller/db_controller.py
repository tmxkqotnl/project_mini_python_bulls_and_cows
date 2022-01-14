from datetime import datetime
from classes.game import Game
from classes.player import Player
from db.db import DB
from lib.lib import error_logger
from psycopg2 import sql


@error_logger
def insert_game_result(db: DB, p: Player, g: Game) -> None:
    q = "insert into rank values('{}','{}','{}','{}',{})".format(
        p.get_id(), p.get_name(), g.get_starttime(), datetime.now(), p.get_attempt()
    )

    return db.execute_query_no_return(q)


# postgres의 DB 생성 및 처리 개별 처리
@error_logger
def drop_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("drop database if exists {};").format(sql.Identifier(db_name))
    )


# postgres의 DB 생성 및 처리 개별 처리
@error_logger
def create_database(db: DB, db_name: str) -> None:
    db.execute_query_no_return(
        sql.SQL("create database {};").format(sql.Identifier(db_name))
    )


# 최소 시도횟수 top 10
@error_logger
def select_top10_minimum_attemps(db: DB) -> list[list[tuple], list[str]]:
    query = """select name, attemps from rank order by attemps limit 10;"""
    return db.execute_query_has_return(query)


# 최소 경과시간 tp 10
@error_logger
def select_top10_minimum_time(db: DB) -> list[list[tuple], list[str]]:
    query = """select name, min(end_dt - start_dt) as takes_time from rank group by name order by takes_time limit 5;"""
    return db.execute_query_has_return(query)
