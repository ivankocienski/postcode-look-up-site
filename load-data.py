
import sqlite3
import json

db = sqlite3.connect("db/database.sqlite")
cursor = db.cursor()
cursor.execute('select count(*) from stores')
row = cursor.fetchone()
print("row=", row)


data = json.load(open("fixtures/stores.json"))
for store in data:
    name = store['name']
    postcode = store['postcode']

    cursor.execute('insert into stores (name, postcode) values (?, ?)', (name, postcode))
    # print("store=", store)

db.commit()