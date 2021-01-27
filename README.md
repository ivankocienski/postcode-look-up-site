# Postcode Search App

This is an application for presenting information about Locations and their postcodes. It uses a JSON API to look up a postcode and get its coordinates. This information can then be accessed by a url [http://localhost:5000].

Unfortunately the postcode lookup is lacking.

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
    > make env

    # build database
    > make db

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

## Thoughts

This was an attempt to complete 'backend role' specification.


With more time I would improve the layout of the code. There are a few scripts for poking data into the database or querying the database and the functionality could be streamlined so code duplication would be reduced. It is not tidy code in those scripts. I would also make the code more pythonic using a proper project scaffold.

The hardests were the test and the location lookup.

