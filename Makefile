
DIST_NAME=ik-tails-dot-com-stores-app

env:
	#virtualenv venv
	. ./venv/bin/activate && pip install --upgrade pip && pip install flask requests sqlalchemy pytest geopy

db:
	sqlite3 db/database.sqlite < db/schema.sql

clean_pycache:
	find . -iname '__pycache__' | xargs rm -r

dist:
	mkdir -p dist/${DIST_NAME}
	cp -R Makefile README.md app db fixtures *.py public tests dist/${DIST_NAME}
	cd dist && tar -cjf ${DIST_NAME}.tar.bz2 ${DIST_NAME}
	find dist/${DIST_NAME} -iname '__pycache__' | xargs rm -r
	rm -f dist/${DIST_NAME}/db/database.sqlite

dist_clean:
	rm -rf dist/*