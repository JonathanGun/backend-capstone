# Tour Travel Admin System

Admin page for tour & travel website

![Admin Page](.github/admin-page.png)

![Admin Edit Travel](.github/admin-edit-travel.png)

## Installing Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Migrating db

```bash
python3 manage.py makemigrations api
python3 manage.py migrate
```

## Develop

```bash
python3 manage.py runserver
```
