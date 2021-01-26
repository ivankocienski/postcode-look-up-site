from sqlalchemy import create_engine

from app import config

db_engine = create_engine(config.db_url(), echo=True)

class Store:
    def __init__(self, values):
        self.id = values[0]
        self.name = values[1]
        self.postcode = values[2]
        self.longitude = values[3]
        self.latitude = values[4]

def stores_count():
    conn = db_engine.connect()
    result = conn.execute('select count(*) from stores')
    return result.fetchone()[0]

def stores_find_all():
    conn = db_engine.connect()
    sql = 'select id, name, postcode, longitude, latitude from stores order by name'
    stores = [ Store(row) for row in conn.execute(sql)]
    return stores

def stores_insert(name, postcode):
    for store in data:
    name = store['name']
    postcode = store['postcode']

    cursor.execute('insert into stores (name, postcode) values (?, ?)', (name, postcode))
    # print("store=", store)

def stores_update_position(id, latitude, longitude):
    # def update_store(db, id, new_latitude, new_longitude):
    sql = 'update stores set latitude=?, longitude=? where id=?'
    args = (new_latitude, new_longitude, id)

    cursor = db.cursor()
    cursor.execute(sql, args)
    db.commit()