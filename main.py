from controller.dbController import init_database
from dotenv import load_dotenv
import os

load_dotenv()
db_info: dict[str, str] = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "host": os.environ["host"],
    "port": os.environ["port"],
}


if __name__ == "__main__":
    db = init_database(db_info)

    db.close()

