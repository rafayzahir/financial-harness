
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class PortfolioHolding(Base):
    __tablename__ = "portfolio_holdings"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    ticker: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    company_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(20, 8),
        nullable=False,
    )

    average_buy_price: Mapped[Decimal] = mapped_column(
        Numeric(20, 8),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="USD",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
