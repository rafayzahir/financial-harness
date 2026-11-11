from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.core.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = decode_access_token(token)
        user_id = int(payload["sub"])
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user = db.get(User, user_id)

    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    return user