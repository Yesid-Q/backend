from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import strawberry
from strawberry.fastapi import GraphQLRouter

from config.settings import settings, TORTOISE_ORM
from resolvers import Query

schema = strawberry.Schema(Query)

graphql = GraphQLRouter(schema=schema)

app: FastAPI = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.add_middleware( 
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup_event():
    await Tortoise.init(config=TORTOISE_ORM)
    #await Tortoise.generate_schemas()

@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()

@app.get("/")
async def index():
    return {"msg": "Hola gente"}

app.include_router(graphql, prefix='/graphql')
