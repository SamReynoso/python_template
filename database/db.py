from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.decl_api import registry
from config import DB_URL

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread":False}

)

SessionLocal = sessionmaker(
    bind=engine
)

Base: registry = declarative_base()

class DBContext:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db
    
    def __exit__(self, et, ev, traceback):
        self.db.close()