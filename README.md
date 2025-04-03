# Bangkit Capstone 0434

## Installing Virtual Environment
```bash
python3 -m virtualenv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Migrating db
```bash
python3 manage.py makemigrations api
python3 manage.py migrate
```
