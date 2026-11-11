from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    UserResponse,
    TokenResponse
)
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from app.api.deps import get_current_user


router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(
    body: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing = db.scalar(
        select(User).where(User.email == body.email)
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    user = User(
        email=body.email,
        full_name=body.full_name,
        hashed_password=hash_password(body.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login", response_model=TokenResponse)
def login(
    body: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.scalar(
        select(User).where(User.email == body.email)
    )

    if not user or not verify_password(
        body.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    return TokenResponse(
        access_token=create_access_token(user.id)
    )


@router.get("/me", response_model=UserResponse)
def get_me(
    user: User = Depends(get_current_user)
):
    return user