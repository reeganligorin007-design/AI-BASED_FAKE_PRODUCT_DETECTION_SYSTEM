from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from core.security import hash_password


def create_user(
    db: Session,
    user_in: UserCreate
):

    db_user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(
            user_in.password
        ),
        role=user_in.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(
    db: Session,
    user_id: int
):
    return db.query(User).filter(
        User.id == user_id
    ).first()



def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    update_data = user.model_dump(exclude_unset=True)

    for key, value in update_data . items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
