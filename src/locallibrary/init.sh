# A script that automates the reconstruction of the entire database.
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell < init.py
python3 manage.py runserver 0.0.0.0:8080
