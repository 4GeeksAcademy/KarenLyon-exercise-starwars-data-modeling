import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key =True)
    firstname = Column(String(40), index = True)
    lastname = Column(String(40))
    email = Column(String(40), unique = True, nullable = False)
    password = Column(String(40), unique = True, nullable = False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    home_word = Column(Integer, ForeignKey('planets.id'))
   
class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key = True)
    planet_name = Column(String(40))
    climate = Column(String(40))
    rotation_period = Column(String(40))
    population = Column(String(40))
 
class Favorites(Base):
     __tbalename__ = 'favorites'
     id = Column(Integer, primary_key = True)
     user_id = Column(Integer, ForeignKey('user'))
     favorite_id = Column(Integer)
     user = relationship('User', backref='favorites')  # Relación con User
     vehicle = relationship('Vehicles', backref='favorites')  # Relación con Vehicles
     planet = relationship('Planets', backref='favorites')  # Relación con Planets
     character = relationship('Character', backref='favorites')

class Vehicles(Base):
     __tablename__= 'vehicles'
     id = Column(Integer, primary_key = True)
     vehicle_name = Column(String(40))
     model = Column(String(String(40)))
     crew = Column(Integer)
     passengers = Column(Integer)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
