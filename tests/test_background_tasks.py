
from unittest.mock import MagicMock, patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.deps import get_current_user
from app.api.v1.endpoints.background_tasks import router as background_router
from app.api.v1.endpoints.task_status import router as status_router
from app.db.session import get_db
from app.models.user import User

app = FastAPI()
app.include_router(background_router, prefix="/tasks")
app.include_router(status_router, prefix="/tasks")

mock_db = MagicMock()
mock_user = MagicMock(spec=User)
mock_user.id = 1

app.dependency_overrides[get_db] = lambda: mock_db
app.dependency_overrides[get_current_user] = lambda: mock_user

client = TestClient(app)


def test_queue_market_quote():
    with patch(
        "app.api.v1.endpoints.background_tasks.fetch_market_quote.apply_async"
    ) as mock_task:
        mock_task.return_value.id = "test-task-123"

        response = client.post("/tasks/market-quote/aapl")

    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
    assert response.json()["task_id"] == "test-task-123"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()


def test_task_status_not_owned():
    mock_db.scalar.return_value = None

    response = client.get("/tasks/unknown-task")

    assert response.status_code == 404
    assert response.json()["detail"] == "Background task not found"


def test_task_status_successful():
    background_task = MagicMock()
    background_task.task_id = "test-task-123"
    background_task.task_type = "market_quote"
    mock_db.scalar.return_value = background_task

    mock_result = MagicMock()
    mock_result.status = "SUCCESS"
    mock_result.successful.return_value = True
    mock_result.result = {"symbol": "AAPL"}

    with patch(
        "app.api.v1.endpoints.task_status.AsyncResult",
        return_value=mock_result,
    ):
        response = client.get("/tasks/test-task-123")

    assert response.status_code == 200
    assert response.json()["status"] == "SUCCESS"
    assert response.json()["result"]["symbol"] == "AAPL"
