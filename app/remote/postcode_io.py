import requests
import re

def lookup_postcode(postcode):
    clean_postcode = re.sub('\\s+', '', postcode)
    r = requests.get("https://postcodes.io/postcodes/%s" % clean_postcode)
    if r.status_code != 200: return (None, None)

    data = r.json()
    result = data['result']
    return (result['latitude'], result['longitude'])