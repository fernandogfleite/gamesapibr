from pydantic import BaseModel


class Game(BaseModel):
    id: int
    title: str
    description: str
    image: str


class GameIn(BaseModel):
    title: str
    description: str
    image: str
