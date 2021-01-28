from flask import render_template, request

import app.db as db
import app.lib.postcode as postcode
import app.lib.geo as geo

def respond_root():
    row_count = db.stores_count()
    rows = db.stores_find_all()

    return render_template(
        'root.html.jinja',
        distance=100,
        store_count=row_count, 
        store_list=rows
    )

def respond_search():
    try:
        distance_arg = int(request.args.get('distance'))

    except ValueError:
        distance_arg = 100
    
    if distance_arg < 10: distance_arg = 10
    if distance_arg > 10000: distance_arg = 10000

    postcode_arg = (request.args.get('postcode') or '').strip()
    if len(postcode_arg) == 0:
        # missing postcode
        return render_template(
            'search.html.jinja',
            distance=distance_arg)


    postcode_pattern = postcode.parse_regex(postcode_arg)
    if postcode_pattern is None:
        # bad postcode
        return render_template(
            'search.html.jinja',
            postcode=postcode_arg,
            distance=distance_arg,
            problem='Postcode is invalid')
    
    origin_stores = db.stores_find_like_postcode(postcode_pattern)
    if len(origin_stores) == 0:
        # not found
        return render_template(
            'search.html.jinja',
            postcode=postcode_arg,
            distance=distance_arg,
            problem='Location with that postcode could not be found')
    
    if len(origin_stores) > 1:
        # ambiguous origin
        return render_template(
            'search.html.jinja',
            postcode=postcode_arg,
            distance=distance_arg,
            other_origins=origin_stores,
            problem='Abiguous postcode match')

    origin = origin_stores[0]

    found_stores = db.stores_find_all_with_location(origin.id)

    found_stores = geo.compute_distance_to_origin(origin, found_stores)

    found_stores = geo.filter_by_distance(found_stores, distance_arg)

    found_stores = geo.sort_by_longitude(found_stores)

    return render_template(
        'search.html.jinja',
        postcode=postcode_arg,
        distance=distance_arg,
        origin=origin,
        found_stores=found_stores)