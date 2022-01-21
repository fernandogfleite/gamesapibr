from typing import List
from fastapi import APIRouter, Body
from app.api import db_manager
from app.api.schemas import Game, GameIn

router = APIRouter(prefix="/games")


@router.get('/')
async def get_all_games():
    games =  list(map(dict, await db_manager.get_all_games()))

    return {"games": games}

@router.post('/')
async def create_game(game: GameIn = Body(...)):
    return await db_manager.create_game(game)


@router.delete('/{id}',status_code=204)
async def delete_game(id: int):
    game_db = await db_manager.get_game_by_id(id)

    if game_db:
        await db_manager.delete_game_by_id(id)
