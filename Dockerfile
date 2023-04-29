FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/

CMD python init.py pre && alembic upgrade head && python init.py init_db && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
