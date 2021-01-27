import json

import app.config
import app.db as db

data = json.load(open("fixtures/stores.json"))
for store in data:
    name = store['name']
    postcode = store['postcode']

    db.stores_insert(name, postcode)
    