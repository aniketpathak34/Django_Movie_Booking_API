#!/bn/bash

echo " BUILD START"
python3.9 -m pip install -r requirements.txt


echo "Make Migrations..."
python3.9 manage.py makemigrations.py --noinput
python3.9 manage.py migrate --noinput

echo "collect static.."
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD COMPLETED"