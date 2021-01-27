import time

import app.db as db
import app.remote.postcode_io as postcode_io

for store in db.stores_find_all():

    if store.latitude is None or store.longitude is None:
        print("lookup: id=%s, name='%s', postcode='%s'" % (store.id, store.name, store.postcode))

        res_latitude, res_longitude = postcode_io.lookup_postcode(store.postcode)
        if (res_latitude is not None) and (res_longitude is not None):
            db.stores_update_location(store, res_latitude, res_longitude)
        
        time.sleep(1)

