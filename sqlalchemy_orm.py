from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///alien.db', echo = True)

base = declarative_base()

class Film(base):
    __tablename__ = "films"

    title = Column(String, primary_key = True)
    director = Column(String)
    year = Column(String)

class Film2(base):
    __tablename__ = "film_2"

    title = Column(String, primary_key = True)
    director = Column(String)
    year = Column(String)


# MVC - Model View Controller - webes szemlélet 

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


# Create - Insert
alien = Film(title = 'Alien', director = 'Ridley Scott')
aliens = Film2(title = 'Aliens', director = 'James Cameron')
breaveheart = Film2(title = 'Braveheart', director = 'Mel Gibson')

session.add(alien)
session.add(aliens)
session.add(breaveheart)

session.commit()

# Read - select

films = session.query(Film)
films2 = session.query(Film2)

for film in films:
    print(film.title)

for film in films2:
    print(film.title)

# Update

alien.year = '1979'
aliens.year = '1986'

session.commit()

# Delete

session.delete(breaveheart)
session.commit()