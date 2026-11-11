
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.background_task import BackgroundTask
from app.models.user import User
from app.worker.tasks import fetch_market_quote

router = APIRouter(tags=["Background Tasks"])


@router.post("/market-quote/{symbol}")
def queue_market_quote(
    symbol: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    symbol = symbol.strip().upper()

    if not symbol or len(symbol) > 20:
        raise HTTPException(
            status_code=400,
            detail="Invalid stock symbol",
        )

    task_id = str(uuid4())

    background_task = BackgroundTask(
        task_id=task_id,
        user_id=current_user.id,
        task_type="market_quote",
    )

    db.add(background_task)
    db.commit()

    try:
        fetch_market_quote.apply_async(
            args=[symbol],
            task_id=task_id,
        )
    except Exception as exc:
        db.delete(background_task)
        db.commit()
        raise HTTPException(
            status_code=503,
            detail="Unable to queue background task",
        ) from exc

    return {
        "message": "Market quote task queued",
        "task_id": task_id,
        "symbol": symbol,
        "status": "queued",
    }
