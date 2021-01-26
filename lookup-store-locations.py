import sqlite3
import time
import re
import requests

def lookup_postcode(postcode):
    clean_postcode = re.sub('\\s+', '', postcode)
    r = requests.get("https://postcodes.io/postcodes/%s" % clean_postcode)
    if r.status_code != 200: return (None, None)
    # print(r.status_code)
    # print(r.headers)

    data = r.json()
    #print(data)

    result = data['result']
    #print(result)

    return (result['longitude'], result['latitude'])
    #longitude = result['longitude']
    #latitude = result['latitude']

    #print("longitude=%s, latitude=%s" % (longitude, latitude))

def update_store(db, id, new_latitude, new_longitude):
    sql = 'update stores set latitude=?, longitude=? where id=?'
    args = (new_latitude, new_longitude, id)

    cursor = db.cursor()
    cursor.execute(sql, args)
    db.commit()



def find_and_update_stores(db):
    cursor = db.cursor()
    cursor.execute('select * from stores')

    for row in cursor.fetchall():
        id, name, postcode, latitude, longitude = row

        if (latitude is None) or (longitude is None):
            print("lookup: id=%s, name='%s', postcode='%s'" % (id, name, postcode))

            res_latitude, res_longitude = lookup_postcode(postcode)
            if (res_latitude is not None) and (res_longitude is not None):
                update_store(db, id, res_latitude, res_longitude)
            
            time.sleep(1)

            
            


#longitude, latitude = lookup_postcode('XXUU')

#print("longitude=%s, latitude=%s" % (longitude, latitude))


db = sqlite3.connect("db/database.sqlite")
find_and_update_stores(db)

# db.commit()