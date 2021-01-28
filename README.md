# Postcode Search App

This is an application for presenting information about Locations and their postcodes. It uses a JSON API to look up a postcode and get its coordinates. This information can then be accessed by a url [http://localhost:5000].

## requirements

- python (built on 3.8)
- virtualenv
- sqlite
- make

- flask
- sqlalchemy
- geopy
- requests
- pytest

## How to set up and run

    # create environment and install dependencies
    > make -B env

    # build database
    > make -B db

    > . ./venv/bin/activate
    # (you may need to update pip)

    # import the stores data into database
    > python load-data.py

    # populate the location data in the database
    > python lookup-store-locations.py

    # to run web server
    > python run-server.py

    # to run tests
    > pytest

## Structure

The web application follows a MVC pattern.

    app/config
    The configuration of the application for pulling parameters
    out of the process environment.

    app/server
    Flask set up and runner.

    app/routes
    Dispatch table connecting flask routes to controller functions

    app/controllers
    Methods that pull data from database and send it to the views

    app/db
    The database layer.

    app/views
    HTML templates.

    app/remote
    External API access wrappers

    app/lib
    Various support functions for scripts or controllers.

## Scripts

`load-data.py` loads JSON data into database.

`populate-store-locations.py` use postcode.io to look up latitude and logitude of store.

`run-server.py` Runs web server

`lookup.py` Given an argument it will look for a string match to the postcode. If a partial postcode is provided will still work. Postcodes can have spaces in them but must be provided in "quotes". If more than one location is found, will print out a list of locations and stop. If only one location is found, will do a geo-distance search and print out all postcodes sorted by longitude (from north to south). A second parameter can be provided to give a maximum radius. All distancs in kilometers.

## Thoughts

This was an attempt to complete 'backend role' specification.

With more time I would clean up the lookup script as it has a lot of logic that could be re-factored to make its internal processes cleaner. I would also like to put the lookup functionality on a web interface. Whilst the code in the application is separated out and not too complex I feel that some of the functions may be unclear, but this would have to be done by consulting with another developer.

The hardests part was the location lookup as it has a lot of logic to sanitize the input

This test was challenging but fair. 