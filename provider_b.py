from fastapi import APIRouter
import json 
import asyncio

router = APIRouter(
    prefix="/provider_b",
    tags=['provider_b']
)


@router.post('')
async def search_provider_b(
    skip: int = 0,
    limit: int = 10
):
    with open("response_b.json") as f:
        data = json.load(f)[skip:limit]
    
    await asyncio.sleep(1)
    return data
