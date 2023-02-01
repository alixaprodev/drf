# build_files.sh
python -m pip install virtualenv
python -m venv env
./env/Bin/activate
python -m pip install -r requirements.txt
python manage.py collectstatic