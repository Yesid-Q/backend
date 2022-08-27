from tortoise.fields import IntField, CharField

from models.base_model import BaseModel

class NationModel(BaseModel):
    id = IntField(pk=True, generated=False, description='Campo primario de la nacion.')
    name = CharField(max_length=100, description='Nombre de la nacion')

    class Meta:
        table = 'nations'
        table_description = 'Tabla de nacionalidades.'
