from datetime import datetime
from contextlib import contextmanager

import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Base, Car

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def create_database_object():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def load_yaml():
    with session_scope() as e:
        for data in yaml.load_all(open('ORM\Miniproject/cars.yaml')):
            data['year_of_manufacture'] = datetime.strptime(data['year_of_manufacture'], '%m-%d-%Y')
            car = Car(**data)
            print(car.__repr__)
            e.add(car)

if __name__ == '__main__':
    create_database_object()
    load_yaml()
