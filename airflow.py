import uuid
import requests
import db_airflow
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database import get_db
from provider_a import search_provider_a
from provider_b import search_provider_b
from schemas import RequestBase

router = APIRouter(
    prefix="/airflow",
    tags=['airflow']
)


@router.post('')
async def airflow(
    db: Session = Depends(get_db),
    skip_a: int = 0,
    limit_a: int = 10,
    skip_b: int = 0,
    limit_b: int = 10
):
    result_a = await search_provider_a(skip=skip_a, limit=limit_a)
    result_b = await search_provider_b(skip=skip_b, limit=limit_b)

    data = {
        "search_id": f"{uuid.uuid4()}",
        "provider_a": result_a,
        "provider_b": result_b
    }

    return db_airflow.create_request(db, data)

@router.get("/results/{search_id}/{currency}")
async def get_by_id_and_currency(
    search_id: str,
    currency: str,
    db: Session = Depends(get_db),
):
    found = db_airflow.get_request(db, search_id, currency) 
    data = {
        "search_id": search_id,
        "status": "COMPLETED",
        "items": found
    }
    return data

@router.get("converter_eu_to_kzt")
def converter_eu_to_kzt(
    eur: int
):
    link = "http://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40%22"
    data = requests.get(link)
    rates = data.json()["rates"]

    eur = float(eur)
    dollar = eur/rates["EUR"]
    eur = rates["KZT"]*dollar
    return eur
