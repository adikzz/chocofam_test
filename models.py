from sqlalchemy.sql.sqltypes import ARRAY
from database import Base
from sqlalchemy import Column, String, JSON

class DbRequest(Base):
    __tablename__ = "requests"
    search_id = Column(String, primary_key=True, index=True)
    provider_a = Column(JSON)
    provider_b = Column(JSON)