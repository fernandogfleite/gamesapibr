
from sqlalchemy import Table
from app.api.schemas import GameIn
from app.db import database
from app.api.models import Game

games: Table = Game.__table__

async def get_all_games():
    query = games.select()

    return await database.fetch_all(query)

async def create_game(game: GameIn):

    query = games.insert().values(**game.dict())

    game_id = await database.execute(query=query)

    return {"id": game_id, **game.dict()}


async def get_game_by_id(game_id: int):
    query = games.select().where(games.c.id == game_id)

    game_db = await database.fetch_one(query)

    return dict(game_db) if game_db else None


async def delete_game_by_id(game_id: int):
    query = games.delete().where(games.c.id == game_id)

    await database.execute(query=query)
