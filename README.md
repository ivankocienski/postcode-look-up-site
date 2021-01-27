# Postcode Search App

This is an application for presenting information about Locations and their postcodes. It uses a JSON API to look up a postcode and get its coordinates. This information can then be accessed by a url [http://localhost:5000].

Unfortunately the postcode lookup is lacking.


requirements

- python (built on 3.8)
- virtualenv
- sqlite
- make

- flask
- sqlalchemy
- geopy
- requests
- pytest

How to set up

In project directory run `make env` the run `make db` to create environment and database.

Then run `python load-data.py` to import the stores data into database.

Then run `python lookup-store-locations.py` to populate the location data in the database.

Then run `python run-server.py` to run the web server.

Also the tests can be run with `pytest`.

