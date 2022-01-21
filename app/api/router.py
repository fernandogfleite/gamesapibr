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