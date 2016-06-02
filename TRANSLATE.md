Steps to add a new language translation
---------------------------------------

1. Install gettext (brew + link):
```brew install gettext```
2. Create the template to upload to Pootle. LANG == 2-digit laguage code
```django-admin.py makemessages -l LANG```
3. Create the template for the string in JS files
```django-admin.py makemessages -d djangojs -l LANG```
4. Add locale to settings_local.py
5. Create migration for the locale fields needed in the DB:
```./managepy schemamigration travels --auto```
6. Migrate the DB
```./managepy migrate travels```
7. Remind the translators to make a user and submit TRANSLATIONS, not SUGGESTIONS. They'll need permission for that
8. Extract the files from Pootle
9. Paste them in the existing locale folder
10. Compile translations. This compiles both .po
```./managepy compilemessages```
