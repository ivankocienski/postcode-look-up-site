from flask import render_template

import app.db as db

def respond_root():
    row_count = db.stores_count()
    rows = db.stores_find_all()

    return render_template(
        'root.html.jinja', 
        store_count=row_count, 
        store_list=rows
    )