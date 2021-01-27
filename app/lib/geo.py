import geopy.distance as distance

def _distance_between(centre, other):
    coords_1 = (centre.longitude, centre.latitude)
    coords_2 = (other.longitude, other.latitude)

    return distance.distance(coords_1, coords_2).km

class DistanceStore:
    def __init__(self, store, origin_store):
        self.store = store
        self.distance = _distance_between(store, origin_store)

def compute_distance_to_origin(centre, other_stores):
    return list(map(
        lambda store: DistanceStore(store, centre), 
        other_stores))

def filter_by_distance(found_stores, max_distance):
    # keep the stores within range
    return list(filter(
        lambda result: result.distance < max_distance,
        found_stores))

def sort_by_longitude(found):
    # sort from north to south
    found.sort(key=lambda result: result.store.longitude)
    return found