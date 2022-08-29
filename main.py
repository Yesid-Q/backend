from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import strawberry
from strawberry.fastapi import GraphQLRouter

from config.settings import settings, TORTOISE_ORM

from resolvers import Query
from mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql = GraphQLRouter(schema=schema, debug=True)

app: FastAPI = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.add_middleware( 
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://0.0.0.0:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup_event():
    await Tortoise.init(config=TORTOISE_ORM)
    

@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()

app.include_router(graphql, prefix='/graphql')
app.add_websocket_route(path='/' , route=graphql)