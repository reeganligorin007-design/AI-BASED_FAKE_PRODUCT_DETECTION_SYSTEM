from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from dependencies.db import get_db

from schemas.user import (
    UserCreate,
    UserLogin,
    UserUpdate,
    UserResponse,
    token
)

from crud import user as user_crud

from core.security import (
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = user_crud.get_user_by_email(
        db,
        user.email
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return user_crud.create_user(
        db,
        user
    )


@router.post(
    "/login",
    response_model=token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = user_crud.get_user_by_email(
        db,
        user.email
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": str(db_user.id),
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    return user_crud.get_users(db)




@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):

    db_user = user_crud.get_user(
        db,
        user_id
    )

    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return db_user


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):

    db_user = user_crud.update_user(
        db,
        user_id,
        user
    )

    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return db_user


@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    db_user = user_crud.delete_user(
        db,
        user_id
    )

    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }
