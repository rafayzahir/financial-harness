from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class GoalCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    target_amount: Decimal = Field(gt=0)
    current_amount: Decimal = Field(default=0, ge=0)
    currency: str = Field(default="USD", min_length=3, max_length=10)
    target_date: date | None = None
    status: Literal["active", "completed", "cancelled"] = "active"

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str) -> str:
        return value.strip().upper()


class GoalUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=150)
    target_amount: Decimal | None = Field(default=None, gt=0)
    current_amount: Decimal | None = Field(default=None, ge=0)
    currency: str | None = Field(default=None, min_length=3, max_length=10)
    target_date: date | None = None
    status: Literal["active", "completed", "cancelled"] | None = None

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str | None) -> str | None:
        return value.strip().upper() if value is not None else None


class GoalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    target_amount: Decimal
    current_amount: Decimal
    currency: str
    target_date: date | None
    status: str
    created_at: datetime
    updated_at: datetime