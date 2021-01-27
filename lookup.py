import sys
import re

import app.config as config
import app.db as db
import app.lib.postcode as postcode
import app.lib.geo as geo

if(len(sys.argv) < 2):
    print("Missing postcode value")
    sys.exit(-1)

postcode_input = sys.argv[1]
print(postcode_input)

max_distance = 100000
try:
    max_distance = sys.argv[2]

except IndexError:
    pass

print("max_distance=", max_distance)

postcode_re = postcode.parse_regex(postcode_input)
print(postcode_re)

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

    # find stores with locations that are not the centre
    look_stores = db.stores_find_all_with_location(centre.id)

    # compute distances
    look_stores = list(map(
        lambda store: (geo.distance_between(centre, store), store),
        look_stores))

    # keep the stores within range
    look_stores = list(filter(
        lambda result: result[0] < max_distance,
        look_stores))

    print(len(look_stores))
    for result in look_stores:
        distance, store = result
        
        print(
            "      id=%s, name=%s, postcode=%s, distance=%s" % 
            (store.id, store.name, store.postcode, distance))
    
    def store_key(a):
        print(a, "l=", a[1].longitude) 
        return a[1].longitude

    # sort from north to south
    look_stores.sort(key=store_key)
    # look_stores = look_stores[1:]

    for result in look_stores:
        distance, store = result
        
        print(
            "      id=%s, name=%s, postcode=%s, distance=%s" % 
            (store.id, store.name, store.postcode, distance))

    #print(look_stores)



