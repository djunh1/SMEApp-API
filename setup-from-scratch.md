# Getting all set up from scratch. 

1. Set up virtual environment 

Create the venv
```
python3 -m venv SME-API
```

Activate Venv
```
cd API-VENV/bin && source activate
```

2. Install Django into the VENV if you haven't already

```
pip3 install django
```

3. Create the project (assuming you didn't clone this one!)

```
django-admin startproject api
```

4. Don't forget to install the dependencies

```
pip install -r requirements.txt
```

5. If desired, install fixtures

```
python3 API/manage.py loaddata testseed.json
```