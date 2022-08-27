import strawberry

@strawberry.type
class PageInfo():
    count: int
    count_total: int
    page: int
    page_total: int
    items_per_page: int
