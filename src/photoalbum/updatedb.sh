#!/bin/sh
rm -f db.sql
python manage.py syncdb --noinput
echo "Loading test data... "
cat testdata.txt | sqlite3 group013
echo "DONE."
