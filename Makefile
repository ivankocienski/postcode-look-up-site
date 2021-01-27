
env:
	#virtualenv venv
	. ./venv/bin/activate && pip install --upgrade pip && pip install flask requests sqlalchemy pytest geopy

db:
	sqlite3 db/database.sqlite < db/schema.sql

clean_pycache:
	find . -iname '__pycache__' | xargs rm -r