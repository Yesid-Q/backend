from tortoise.models import Model
from tortoise.fields import IntField, CharField

from models.base_model import BaseModel

class ClubModel(BaseModel):
    id = IntField(pk=True, generated=False, description='Campo primario del club.')
    name = CharField(max_length=100, description='Nombre del club.')

    class Meta:
        table = 'clubs'
        table_description = 'Tabla de Clubs.'
