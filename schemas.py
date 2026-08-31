from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ExpenseCreate(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100
    )

    amount: float = Field(
        gt=0
    )

    category: str = Field(
        min_length=2,
        max_length=50
    )

    description: Optional[str] = None


class ExpenseResponse(BaseModel):

    id: int
    title: str
    amount: float
    category: str
    description: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True