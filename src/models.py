import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer(), nullable=False) # tengo que agregar mas campos
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
