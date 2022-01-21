from app.db import Base

from sqlalchemy import (
    Column,
    Integer,
    String
)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    image = Column(String(255))
