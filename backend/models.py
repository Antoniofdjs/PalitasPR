#!/usr/bin/python3
"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Integer, Boolean
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base

# ASSOCIATION USER & SERVICE & TOWN CLASS
class UserServiceAssoc(BaseModel, Base):
    __tablename__ = 'user_service_assoc'


    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    service_id = Column(String, ForeignKey('services.id'), nullable=False)
    town_id = Column(String, ForeignKey('towns.id'), nullable=False)

    # Relationships
    user = relationship(
        'User',
        cascade='all, delete-orphan',
        single_parent=True,
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    town = relationship(
        'Town',
        cascade='all, delete-orphan',
        single_parent=True,
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    service = relationship(
        'Service',
        cascade='all, delete-orphan',
        single_parent=True,
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    __table_args__ = (UniqueConstraint('user_id', 'service_id', 'town_id'),)


# SERVICE CLASS
class Service(BaseModel, Base):
    __tablename__ = 'services'

    name = Column(String(50), unique=True, nullable=False)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='service'
        )

# USER CLASS
class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    verified = Column(Boolean, default=False)
    verification_token = Column(String(128), unique=True)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='user',
        cascade='all, delete'
        )

# TOWN CLASS
class Town(BaseModel, Base):
    __tablename__ = 'towns'

    name = Column(String(50), unique=True, nullable=False)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='town',
        cascade='all, delete'
        )

# Still missin Task class and need to work hereee relationships
class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    description = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    picture_paths = Column(String)

class Task(BaseModel, Base):
    __tablename__ = 'tasks'

    receiver_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    provider_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    service_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    status = Column(String(255), nullable=False, default='open')
    description = Column(String(255), nullable=False)
    review_id = Column(String(255), ForeignKey('reviews.id'))
