
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.portfolio import PortfolioHolding
from app.models.user import User
from app.schemas.portfolio import (
    HoldingCreate,
    HoldingResponse,
    HoldingUpdate,
)

router = APIRouter(tags=["Portfolio"])


@router.post(
    "/holdings",
    response_model=HoldingResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_holding(
    payload: HoldingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    holding = PortfolioHolding(
        **payload.model_dump(),
        user_id=current_user.id,
    )

    db.add(holding)
    db.commit()
    db.refresh(holding)

    return holding


@router.get("/holdings", response_model=list[HoldingResponse])
def list_holdings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    statement = (
        select(PortfolioHolding)
        .where(PortfolioHolding.user_id == current_user.id)
        .order_by(PortfolioHolding.created_at.desc())
    )

    return db.scalars(statement).all()


@router.put("/holdings/{holding_id}", response_model=HoldingResponse)
def update_holding(
    holding_id: int,
    payload: HoldingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    holding = db.scalar(
        select(PortfolioHolding).where(
            PortfolioHolding.id == holding_id,
            PortfolioHolding.user_id == current_user.id,
        )
    )

    if holding is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio holding not found",
        )

    updates = payload.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(holding, field, value)

    db.commit()
    db.refresh(holding)

    return holding


@router.delete(
    "/holdings/{holding_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_holding(
    holding_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    holding = db.scalar(
        select(PortfolioHolding).where(
            PortfolioHolding.id == holding_id,
            PortfolioHolding.user_id == current_user.id,
        )
    )

    if holding is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio holding not found",
        )

    db.delete(holding)
    db.commit()
