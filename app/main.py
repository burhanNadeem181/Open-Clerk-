from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import init_db, list_leads, save_lead
from app.models import LeadCreate
from app.qualification import qualify_lead


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="OpenClerk API",
    description="A small-business lead intake and qualification prototype.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok", "project": "OpenClerk"}


@app.post("/leads", status_code=201)
def create_lead(lead: LeadCreate):
    priority = qualify_lead(lead.message)
    return save_lead(
        name=lead.name,
        email=str(lead.email),
        business=lead.business,
        message=lead.message,
        priority=priority,
    )


@app.get("/leads")
def get_leads():
    return list_leads()
