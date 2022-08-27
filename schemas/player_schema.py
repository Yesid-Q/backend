from typing import List, Optional

import strawberry

from schemas.base_schema import PageInfo
from schemas.club_schema import Club
from schemas.nation_schema import Nation

@strawberry.type
class Player:
    id: strawberry.ID
    name: Optional[str]
    position: Optional[str]
    nation: Optional[Nation]
    club: Optional[Club]


@strawberry.type
class Players:
    page_info: PageInfo
    items: List[Player]