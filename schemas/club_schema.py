from typing import List, Optional

import strawberry

from schemas.base_schema import PageInfo

@strawberry.type
class Club:
    id: strawberry.ID
    name: Optional[str]

@strawberry.type
class Clubs:
    page_info: PageInfo
    items: List[Club]