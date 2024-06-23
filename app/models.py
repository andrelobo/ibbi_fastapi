from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    categories = relationship("Category", back_populates="owner", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="owner", cascade="all, delete-orphan")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship("User", back_populates="categories")
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    value = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    category = relationship("Category", back_populates="products")
    owner = relationship("User", back_populates="products")

class Config:
        orm_mode = True