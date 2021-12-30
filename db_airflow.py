import re
from types import resolve_bases
from models import DbRequest
from schemas import RequestBase
from sqlalchemy.orm import Session

def create_request(db: Session, request: RequestBase):
    new_request = DbRequest(
        search_id = request["search_id"],
        provider_a = request["provider_a"],
        provider_b = request["provider_b"]
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def get_request(db: Session, search_id: str, currency: str):
    return db.query(DbRequest).filter(DbRequest.search_id == search_id).all()