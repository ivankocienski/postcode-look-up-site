from sqlalchemy import create_engine

from app import config
import app.lib.postcode as postcode

db_engine = create_engine(config.db_url(), echo=True)

class Store:
    def __init__(self, values):
        self.id = values[0]
        self.name = values[1]
        self.postcode = values[2]
        self.latitude = values[3]
        self.longitude = values[4]

def stores_count():
    conn = db_engine.connect()
    result = conn.execute('select count(*) from stores')
    return result.fetchone()[0]

def stores_find_all():
    conn = db_engine.connect()
    sql = 'select id, name, postcode, latitude, longitude from stores order by name'
    stores = [ Store(row) for row in conn.execute(sql)]
    return stores

def stores_find_all_with_location(not_id):
    conn = db_engine.connect()
    sql = """
        select 
            id, name, postcode, latitude, longitude 
        from 
            stores 
        where 
            longitude is not null and latitude is not null and id != ?
    """
    stores = [ Store(row) for row in conn.execute(sql, (not_id,))]
    return stores

def stores_insert(name, postcode):
    sql = 'insert into stores (name, postcode) values (?, ?)'
    args = (name, postcode)

    conn = db_engine.connect()
    conn.execute(sql, args)

def stores_update_location(store, new_latitude, new_longitude):
    sql = 'update stores set latitude=?, longitude=? where id=?'
    args = (new_latitude, new_longitude, store.id)

    conn = db_engine.connect()
    conn.execute(sql, args)


def stores_find_like_postcode(postcode_regex):
    return list(filter(
        lambda store: store.latitude and postcode.postcode_match(postcode_regex, store.postcode),
        stores_find_all()))