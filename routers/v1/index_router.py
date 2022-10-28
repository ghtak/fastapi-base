from fastapi import APIRouter

index_router = APIRouter()


@index_router.get('/', tags=['index'])
async def get():
    return 'hello fastapi'
