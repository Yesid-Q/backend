from typing import List, Optional

from strawberry import ID

from models.nation_model import NationModel

from schemas.base_schema import PageInfo
from schemas.nation_schema import Nation, Nations


async def get_nations(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
    name: Optional[str] = None
) -> Nations:
    nations = await NationModel.filter(
        name__icontains = '' if name is None else name
    ).limit(limit).offset((limit* (page-1)))

    response = await NationModel.paginate(page, limit, name__icontains = '' if name is None else name)

    return Nations(items=nations, page_info=PageInfo(**response))


async def get_nation_by_id(id: ID) -> Nation:
    nation = await NationModel.filter(pk= id).first()
    return nation

