import strawberry
from email_validator import validate_email, EmailNotValidError

from models.user_model import UserModel
from schemas.user_schema import User

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    async def register_user(
        self,
        name: str,
        email: str,
        password: str,
        very_password: str
    ) -> User:
        try:
            validation = validate_email(email, check_deliverability=True)
            email = validation.email
        except EmailNotValidError as e:
            return e
        if password != very_password:
            return
        user = await UserModel.create(name=name.lower(), email=email.lower(), password=password)
        await user.create_token()
        await user.hash_password()

        return user

    @strawberry.mutation
    async def login_user(
        self,
        email: str,
        password: str
    ) -> User:
        user = await UserModel.get_or_none(email=email.lower())
        if user is None:
            return
        
        check = await user.verify_password(password)

        if not check:
            return
        await user.create_token()
        await user.save()

        return user
