from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

engine = create_engine('sqlite:///films.db', echo = True)

meta = MetaData(engine)

film_table = Table('films', meta, 
    Column('title', String),
    Column('director', String),
    Column('year', String),
)

with engine.connect() as conn:
    film_table.create()
    # insert - Create
    insert_statement = film_table.insert().values(title= 'Alien', director = 'Ridley Scott')
    conn.execute(insert_statement)

    # Read - Select
    select_statement = film_table.select()
    result_set = conn.execute(select_statement)

    for item in result_set:
        print(item)

    # Update
    update_statement = film_table.update().where(film_table.c.title=='Alien').values(year = '1979')
    conn.execute(update_statement)

    # Delete- ugyan az mint az update csak .delete
