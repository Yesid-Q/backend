import jwt
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256

from tortoise import Model
from tortoise.fields import IntField, CharField, DatetimeField, TextField

from config import settings

class UserModel(Model):
    id = IntField(pk=True, description='Campo primario del usuario.')
    name = CharField(max_length=200, description='Nombre de un usuario.')
    email = CharField(max_length=255, unique=True, description='Correo electronico del usuario.')
    password = CharField(max_length=255, description='Contrasena de registro de usuario.')
    token = TextField(null=True, description='Token de inicio de sesion.')
    created_at = DatetimeField(auto_now_add=True, description="Fecha de creacion de un registro.")
    update_at = DatetimeField(auto_now=True, description="Fecha de actualizacion de un registro.")
    delete_at = DatetimeField(null=True, description="Fecha de eliminacion de un registro.")

    class Meta:
        table = 'users'
        table_description = 'Table de usuarios'
        ordering = ['created_at']

    async def delete(self)-> None:
        self.delete_at = datetime.now() if self.delete_at is None else None
        await self.save()

    async def hash_password(self)-> None:
        self.password = pbkdf2_sha256.hash(self.password)
        await self.save()

    async def verify_password(self, pwd: str)-> bool:
        return pbkdf2_sha256.verify(pwd, self.password)

    async def create_token(self)-> str:
        expire = datetime.utcnow() + timedelta(days=2)
        key = "465asd4"
        self.token = jwt.encode({'sub': self.id, 'exp': expire},key, algorithm='HS256')
