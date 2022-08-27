from typing import List, Optional

from strawberry import ID

from models.club_model import ClubModel

from schemas.base_schema import PageInfo
from schemas.club_schema import Club, Clubs


async def get_clubs(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
    name: Optional[str] = None
) -> Clubs:
    clubs = await ClubModel.filter(
        name__icontains = '' if name is None else name
    ).limit(limit).offset((limit* (page-1)))
    
    response = await ClubModel.paginate(page, limit, name__icontains = '' if name is None else name)

    return Clubs(items=clubs, page_info=PageInfo(**response))


async def get_club_by_id(id: ID) -> Club:
    club = await ClubModel.filter(pk= id).first()
    return club



