import sys
import re

import geopy.distance as distance

import app.config as config
import app.db as db
import app.util as util


if(len(sys.argv) < 2):
    print("Missing postcode value")
    sys.exit(-1)

postcode = sys.argv[1]
print(postcode)

postcode_re = util.parse_regex(postcode)
print(postcode_re)

#stores = db.stores_find_all()
#for store in stores:
#    if util.postcode_match(postcode_re, store.postcode):
#        print(store.id, store.name, store.postcode)

#found_stores = [store for store in stores if util.postcode_match(postcode_re, store.postcode)]

# print(found_stores)
#for store in found_stores:
#    print(store.id, store.name, store.postcode)

def distance_between(centre, other):

    coords_1 = (centre.longitude, centre.latitude)
    coords_2 = (other.longitude, other.latitude)

    return distance.distance(coords_1, coords_2).km

found_stores = db.stores_find_like_postcode(postcode_re)
print("found_stores.len=", len(found_stores))

if len(found_stores) > 1:
    print("More than one match for given postcode")
    for store in found_stores:
        print(
            "id=%s, name=%s, postcode=%s, latitude=%s, longitude=%s" % 
            (store.id, store.name, store.postcode, store.latitude, store.longitude))
else:
    centre = found_stores[0]
    print("Found [%s] '%s' (%s)" % (centre.id, centre.name, centre.postcode))
    print("    Using centre: latitude=%.2f, longitude=%.2f" % (centre.latitude, centre.longitude))

    look_stores = db.stores_find_all()

    look_stores = list(map(
        lambda store: (distance_between(centre, store), store),
        look_stores
    ))

    look_stores.sort(key=lambda a: a[0])
    look_stores = look_stores[1:11]

    for result in look_stores:
        distance, store = result
        
        print(
            "      id=%s, name=%s, postcode=%s, distance=%s" % 
            (store.id, store.name, store.postcode, distance))

    #print(look_stores)



