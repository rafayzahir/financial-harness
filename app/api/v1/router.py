
from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.background_tasks import router as background_tasks_router
from app.api.v1.endpoints.comparison import router as comparison_router
from app.api.v1.endpoints.fundamentals import router as fundamentals_router
from app.api.v1.endpoints.goals import router as goals_router
from app.api.v1.endpoints.market_data import router as market_data_router
from app.api.v1.endpoints.portfolio import router as portfolio_router
from app.api.v1.endpoints.portfolio_analytics import (
    router as portfolio_analytics_router,
)
from app.api.v1.endpoints.portfolio_risk import (
    router as portfolio_risk_router,
)
from app.api.v1.endpoints.projections import router as projections_router
from app.api.v1.endpoints.scenarios import router as scenarios_router
from app.api.v1.endpoints.task_status import router as task_status_router
from app.api.v1.endpoints.technical_analysis import (
    router as technical_analysis_router,
)

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(portfolio_router, prefix="/portfolio")
api_router.include_router(portfolio_analytics_router, prefix="/portfolio")
api_router.include_router(portfolio_risk_router, prefix="/portfolio")
api_router.include_router(projections_router, prefix="/projections")
api_router.include_router(scenarios_router, prefix="/scenarios")
api_router.include_router(background_tasks_router, prefix="/tasks")
api_router.include_router(task_status_router, prefix="/tasks")
api_router.include_router(goals_router, prefix="/goals")
api_router.include_router(market_data_router, prefix="/market")
api_router.include_router(technical_analysis_router, prefix="/technical")
api_router.include_router(fundamentals_router, prefix="/fundamentals")
api_router.include_router(comparison_router, prefix="/comparison")
