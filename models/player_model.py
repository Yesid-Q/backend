from tortoise.fields import IntField, CharField
from tortoise.fields.relational import ForeignKeyField

from models.base_model import BaseModel

class PlayerModel(BaseModel):
    id = IntField(pk=True, generated=False, description='Campo primario de un jugador.')
    name = CharField(max_length=255, description='Nombre de un jugador.')
    position = CharField(max_length=255, description='Posicion de un jugador.')
    nation = ForeignKeyField('models.NationModel', related_name='player_nation')
    club = ForeignKeyField('models.ClubModel', related_name='player_club')

    class Meta:
        table = 'players'
        table_description = 'Tabla de jugadores.'
