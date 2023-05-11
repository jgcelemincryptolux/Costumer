# Costumer


# Create virtual env
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```



# cd app
alembic init alembic

# configurar la conexion a base de datos costumer
en database.py
en alambic.ini


alembic revision --autogenerate -m "migrate tables"
alembic upgrade head




# run
uvicorn main:app --reload
