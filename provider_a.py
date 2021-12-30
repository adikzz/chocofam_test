from fastapi import APIRouter
import json 
import asyncio

router = APIRouter(
    prefix="/provider_a",
    tags=['provider_a']
)


@router.post('')
async def search_provider_a(
    skip: int = 0,
    limit: int = 10
):
    with open("response_a.json") as f:
        data = json.load(f)[skip:limit]
    
    await asyncio.sleep(1)
    return data
