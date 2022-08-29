from typing import List, Optional

from strawberry import ID

from models.player_model import PlayerModel

from schemas.base_schema import PageInfo
from schemas.player_schema import Player, Players


async def get_players(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
    name: Optional[str] = None
) -> Players:
    players = await PlayerModel.filter(
        name__icontains = '' if name is None else name
    ).limit(limit).offset((limit* (page-1)))

    response = await PlayerModel.paginate(page, limit, name__icontains = '' if name is None else name)

    return Players(items= players, page_info=PageInfo(**response))

async def get_player_by_id(id: ID) -> Player:
    player = await PlayerModel.filter(pk= id).first()
    return player

