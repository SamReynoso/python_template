from sqlalchemy import ForeignKey, Column, String, Integer, CHAR
from db import Base


class New_Table(Base):
    __tablename__ = "new_table"

    id = Column("id", Integer, primary_key=True)

    def __init__(self, id: int, size: int):
        self.id = id

    def __str__(self):
        return f"New_table: Item { self.id }"

    def __reper__(self):
        return self.__str__()