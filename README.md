# Costumer
alembic init alembic
alembic revision --autogenerate -m "migrate tables"
alembic upgrade head