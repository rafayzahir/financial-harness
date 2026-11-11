
from celery.result import AsyncResult
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.background_task import BackgroundTask
from app.models.user import User
from app.worker.celery_app import celery_app

router = APIRouter(tags=["Background Tasks"])


@router.get("/{task_id}")
def get_task_status(
    task_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    background_task = db.scalar(
        select(BackgroundTask).where(
            BackgroundTask.task_id == task_id,
            BackgroundTask.user_id == current_user.id,
        )
    )

    if background_task is None:
        raise HTTPException(
            status_code=404,
            detail="Background task not found",
        )

    task = AsyncResult(task_id, app=celery_app)

    response = {
        "task_id": task_id,
        "task_type": background_task.task_type,
        "status": task.status,
    }

    if task.successful():
        response["result"] = task.result
    elif task.failed():
        response["error"] = "Background task failed"

    return response
