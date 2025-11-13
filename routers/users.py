from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.orm import Session
from database import database
from models.users import Users
from schemas.users import UserSchema
from utils.auth import password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user

user_router = APIRouter()


@user_router.post("/sign_up")
def register(form: UserSchema, db: Session =Depends(database)):
    user_email = db.query(Users).filter(Users.email == form.email).first()
    if user_email:
        raise HTTPException(400, "User already exists")

    user = Users(
        full_name=form.full_name,
        email=form.email,
        password=password_hash(form.password),
        role="admin"
    )
    db.add(user)
    db.commit()
    raise HTTPException(201, "User created successfully")



@user_router.post("/sign_in")
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database)):
    user = db.query(Users).filter(Users.email == form_data.username).first()

    if not user or not pbkdf2_sha256.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login yoki parolda xatolik",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "id": user.id},
        expires_delta=access_token_expires
    )

    return {
        "id": user.id,
        "role": user.role,
        "access_token": access_token,
        "token_type": "bearer"
    }

@user_router.get("/users")
def profil(user_data: Users =Depends(get_current_user)):
    return user_data

@user_router.put("/update")
def update_profil(form: UserSchema, db: Session = Depends(database),
                  user_data: Users = Depends(get_current_user)):
    db.query(Users).filter(Users.id == user_data.id).update({
        Users.full_name: form.full_name,
        Users.email: form.email,
        Users.password: password_hash(form.password)
    })
    db.commit()
    raise HTTPException(200, "User updated successfully")

@user_router.delete("/delete")
def delete_profil(db: Session = Depends(database),
                  user_data: Users = Depends(get_current_user)):
    db.query(Users).filter(Users.id == user_data.id).delete()
    db.commit()
    raise HTTPException(200, "User deleted successfully")

