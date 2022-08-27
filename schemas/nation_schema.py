from typing import List, Optional

import strawberry

from schemas.base_schema import PageInfo

@strawberry.type
class Nation:
    id: strawberry.ID
    name: Optional[str]


@strawberry.type
class Nations:
    page_info: PageInfo
    items: List[Nation]
