from datetime import datetime

import strawberry


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str
    password: str
    token: str
    created_at: datetime
    update_at: datetime
    delete_at: datetime
