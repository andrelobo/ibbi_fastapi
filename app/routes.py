from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import get_db
from typing import List
from datetime import timedelta

router = APIRouter()

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, hashed_password=auth.get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_category = models.Category(**category.dict(), owner_id=current_user.id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_product = models.Product(**product.dict(), owner_id=current_user.id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products/", response_model=List[schemas.Product])
def get_all_products(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    products = db.query(models.Product).all()
    return products