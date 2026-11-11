
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class HoldingCreate(BaseModel):
    ticker: str = Field(min_length=1, max_length=20)
    company_name: str | None = Field(default=None, max_length=150)
    quantity: Decimal = Field(gt=0)
    average_buy_price: Decimal = Field(gt=0)
    currency: str = Field(default="USD", min_length=3, max_length=10)

    @field_validator("ticker")
    @classmethod
    def normalize_ticker(cls, value: str) -> str:
        return value.strip().upper()

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str) -> str:
        return value.strip().upper()


class HoldingUpdate(BaseModel):
    ticker: str | None = Field(default=None, min_length=1, max_length=20)
    company_name: str | None = Field(default=None, max_length=150)
    quantity: Decimal | None = Field(default=None, gt=0)
    average_buy_price: Decimal | None = Field(default=None, gt=0)
    currency: str | None = Field(default=None, min_length=3, max_length=10)

    @field_validator("ticker")
    @classmethod
    def normalize_ticker(cls, value: str | None) -> str | None:
        return value.strip().upper() if value is not None else None

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str | None) -> str | None:
        return value.strip().upper() if value is not None else None


class HoldingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ticker: str
    company_name: str | None
    quantity: Decimal
    average_buy_price: Decimal
    currency: str
    created_at: datetime
    updated_at: datetime
