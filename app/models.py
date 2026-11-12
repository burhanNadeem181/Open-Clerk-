from pydantic import BaseModel, EmailStr, Field


class LeadCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    business: str = Field(min_length=2, max_length=120)
    message: str = Field(min_length=5, max_length=3000)


class LeadResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    business: str
    message: str
    priority: str
    created_at: str
