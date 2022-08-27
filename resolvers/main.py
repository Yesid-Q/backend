import strawberry

from resolvers.club_resolver import get_clubs, get_club_by_id
from resolvers.nation_resolver import get_nations, get_nation_by_id
from resolvers.player_resolver import get_players, get_player_by_id


@strawberry.type
class Query:
    nations = strawberry.field(resolver=get_nations)
    nation_by_id = strawberry.field(resolver=get_nation_by_id)

    clubs = strawberry.field(resolver=get_clubs, )
    club_by_id = strawberry.field(resolver=get_club_by_id)

    players = strawberry.field(resolver=get_players)
    player_by_id = strawberry.field(resolver=get_player_by_id)
