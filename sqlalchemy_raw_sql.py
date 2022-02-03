# CRUD - Create, Read, Update, Delete

from sqlalchemy import create_engine

engine = create_engine('sqlite:///movies.db', echo = True)
# engine = create_engine('postgres+psycopg2:///user:password@localhost:5432/movies') --POSTGRES KAPCSOLAT

engine.execute('create table if not exists films (title text, director text, year text)')
engine.execute("insert into films (title, director, year) values ('Alien', 'Ridley Scott', '1979')")
engine.execute("insert into films (title, director, year) values ('Aliens', 'James Cameron', '1986')")
engine.execute("insert into films (title, director, year) values ('Alien 3', 'Fincher', '1993')")

result_set = engine.execute('select * from films')

for item in result_set:
    print(item)

engine.execute("delete from films where year = '1993'")

