Installation
============

Dependencies
------------

These instructions will help you install the various dependencies that you need
to make Locast run.

 * Python 2.5 or greater
 * Django 1.3
 * ffmpeg

1. install base system
----------------------

First, there are some common tools that need to be installed:

Debian:

    apt-get install ffmpeg

Then we need to install the geospatial database. We use Postgres + PostGIS, but
any geospatial database should work:

Debian:

    apt-get install postgresql-8.4-postgis

Redhat:

    yum install postgresql84-server postgis psycopg2 gdal

2. Set up virtualenv
--------------------

We recommend running Locast within a python virtual environment.

Debian:

    apt-get install python-virtualenv

Create the directory that will host the site:

    mkdir -p /prod
    cd /prod

Initialize a virtual environment. This will contain all our libraries and code:

    virtualenv locast

If you need a specific version of Python, you can specify it using '-p' to virtualenv

    cd locast
    source bin/activate

Place the git project directory inside the virtual environment

3. install Locast Core
----------------------
You can install the Locast core using pip:

    pip install https://github.com/mitmel/Locast-Web-Core/zipball/master
    
4. Install Locast 
-------------------------
Install support packages to support installation of all the python modules.

 * PIL is needed for all the thumbnailing.

On Debian, you can do:

    apt-get install python-imaging 

Activate the virtual environment:

    source bin/activate

Go into the project directory, and from there, install all of the dependencies:

    pip install -r requirements.txt

5. setup database
-----------------

Start Postgres administration (as root):

    su - postgres

Or as a user with sudo privileges:

    sudo -u postgres -s

Create Postgres user:

    createuser -W locast

You should not give this user any special privileges, so answer no to all. You
should create a random password.

Create database:

    createdb -O locast locast
    
Set up postgis on db:

    createlang plpgsql locast
    psql -d locast -f /usr/share/postgresql/8.4/contrib/postgis-1.5/postgis.sql
    psql -d locast -f /usr/share/postgresql/8.4/contrib/postgis-1.5/spatial_ref_sys.sql

Set ownership:

    psql locast

Enter these SQL commands:

    alter table geometry_columns owner to locast;
    alter table spatial_ref_sys owner to locast;

Exit psql by pressing Ctrl-D.

6. Configure Locast 
---------------------------

Create a folder to place the local configuration files into:

    mkdir ../etc

Next, copy the `example settings_local.py` file to your virtualenv's etc
directory:

    cp settings_local.py.example ../etc/settings_local.py

Modify this file to your environment.

Link the local settings file into the Python path. `readlink` will place the
absolute path to `../etc/` in the `locast.pth` file:

    readlink -f ../etc/ > ../lib/python2.6/site-packages/locast.pth


7. Create admin user
--------------------

TODO
