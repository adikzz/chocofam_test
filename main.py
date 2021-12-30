from fastapi import FastAPI
import provider_a, provider_b, airflow, models
from database import engine
from datetime import datetime
import requests

app = FastAPI()

app.include_router(provider_a.router)
app.include_router(provider_b.router)
app.include_router(airflow.router)

models.Base.metadata.create_all(engine)

# date = datetime.today().strftime('%d-%m-%Y')

# link = f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={date}"

# response_API = requests.get(link) 
# data = response_API.json()
