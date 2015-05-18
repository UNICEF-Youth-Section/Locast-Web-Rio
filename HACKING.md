This are the steps needed for setting up a new development environment.

The project has some extra dependencies that have to be installed using the OS's package manager.

This have to be run from the cloned repo's root:

```
pip install virtualenv
virtualenv .
. bin/activate
pip install https://github.com/UNICEF-Youth-Section/Locast-Web-Core-Rio/zipball/master
pip install -r requirements.txt
pip install psycopg2 Pillow
createuser -a locast
createdb locast
psql -d locast -f `find /usr/local/Cellar -name postgis.sql`
psql -d locast2 -f `find /usr/local/Cellar -name spatial_ref_sys.sql`

vi settings_local.py # edit SECRET_KEY, add APP_NAME
./manage.py syncdb
./manage.py migrate travels

./manage.py runserver
```

[Locast's documentation](http://locast.mit.edu/documentation/) can contain extra details.
