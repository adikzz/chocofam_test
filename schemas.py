from pydantic import BaseModel
from datetime import datetime
from typing import Any, List


class RequestBase(BaseModel):
    search_id: str
    provider_a: List[dict]
    provider_b: List[dict]