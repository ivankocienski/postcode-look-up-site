import geopy.distance as distance

def distance_between(centre, other):

    coords_1 = (centre.longitude, centre.latitude)
    coords_2 = (other.longitude, other.latitude)

    return distance.distance(coords_1, coords_2).km