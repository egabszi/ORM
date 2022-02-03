from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    car_name= Column(String)
    engine_type= Column(String)
    color= Column(String)
    year_of_manufacture= Column(Date)
    price= Column(Integer)

    def __repr__(self):
        return "<Car(car_name='{}', engine_type='{}', color='{}'\
            year_of_manufature={}, price={})>"\
                .format(self.car_name, self.engine_type, self.color, self.year_of_manufacture,\
                    self.price)

if __name__ == '__main__':
    print(Car)