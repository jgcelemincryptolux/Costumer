# Costumer


# Create virtual env
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# configurar la conexion a base de datos
en database.py
en alambic.ini


# cd app
alembic upgrade head

# run 
uvicorn main:app --reload
