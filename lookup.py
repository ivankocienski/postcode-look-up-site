import sys
import re

import app.config as config
import app.db as db
import app.lib.postcode as postcode
import app.lib.geo as geo

def bad_end(msg):
    print("error: %s" % msg)
    sys.exit(-1)

def read_command_line_args():
    if(len(sys.argv) < 2):
        bad_end("Missing postcode value")

    postcode_input = sys.argv[1]
    print(postcode_input)

    max_distance = 100000
    try:
        max_distance = int(sys.argv[2])
        if max_distance < 1:
            bad_end("Range value must be greater than 1")

    except ValueError:
        bad_end("Range value is not an integer")

    except IndexError:
        pass

    return (postcode_input, max_distance)

def make_postcode_pattern(postcode_input):
    postcode_re = postcode.parse_regex(postcode_input)
    if postcode_re is None:
        bad_end("Bad postcode provided")
    
    return postcode_re

def find_origin_store(postcode_pattern):
    return db.stores_find_like_postcode(postcode_pattern)

def show_ambiguous_matches(found_stores):
    print("More than one match for given postcode")
    for store in found_stores:
        print(
            "id=%s, name=%s, postcode=%s, latitude=%s, longitude=%s" % 
            (store.id, store.name, store.postcode, store.latitude, store.longitude))

def show_distance_to_origin(origin, max_distance):
    found_stores = db.stores_find_all_with_location(origin.id)

    found_stores = geo.compute_distance_to_origin(origin, found_stores)

    found_stores = geo.filter_by_distance(found_stores, max_distance)

    found_stores = geo.sort_by_longitude(found_stores)

    for result in found_stores:        
        print(
            "      id=%s, name=%s, postcode=%s, longitude=%s, distance=%s" % 
            (result.store.id, result.store.name, result.store.postcode, 
            result.store.longitude, result.distance))

def main():
    postcode_input, max_distance = read_command_line_args()

    postcode_pattern = make_postcode_pattern(postcode_input)

    origin_stores = find_origin_store(postcode_pattern)

    if len(origin_stores) == 0:
        print("Could not find any stores matching that postcod")
        return

    if len(origin_stores) > 1:
        show_ambiguous_matches(origin_stores)
        return

    origin = origin_stores[0]
    print("Found [%s] '%s' (%s)" % (origin.id, origin.name, origin.postcode))
    print("    Using centre: latitude=%.2f, longitude=%.2f" % (origin.latitude, origin.longitude))

    show_distance_to_origin(origin, max_distance)

main()
