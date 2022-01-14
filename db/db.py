from typing import Any, Optional
import psycopg2 as pg2
from typing import Optional
from lib.lib import error_logger


class DB:
    def __init__(self) -> None:
        self.__connection: Optional[pg2.connection] = None
        self.__cursor: Optional[pg2.cursor] = None  # typing 해결 안됌..

    def connect(self, options: str) -> None:
        self.__connection = pg2.connect(options)
        self.__connection.autocommit = True
        # self.set_isolation_level()
        self.__cursor = self.__connection.cursor()

    @error_logger
    def execute_query_has_return(self, query: str) -> [list[tuple], list[str]]:
        self.__cursor.execute(query)
        column_names = [r[0] for r in self.__cursor.description]

        return [self.__cursor.fetchall(), column_names]

    @error_logger
    def execute_query_no_return(self, query: str)->None:
        self.__cursor.execute(query)

    def close(self) -> None:
        try:
            self.__connection.close()
        except pg2.DatabaseError as e:
            exit(0)

    @error_logger
    def get_connection(self) -> Optional[Any]:
        return self.__connection

    @error_logger
    def get_cursor(self) -> Optional[Any]:
        return self.__cursor
