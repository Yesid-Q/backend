from math import ceil
from typing import Optional

from tortoise import Model

class BaseModel(Model):

    class Meta:
        abstract = True
    
    @classmethod
    async def paginate(cls, page: int, limit: int, **kwargs):
        counts: int = await cls.filter(**kwargs).count()
        pages = ceil(counts / limit)
        return {
            'count': limit,
            'count_total': counts,
            'page': page,
            'page_total': pages,
            'items_per_page': limit,
        }
