FROM python:3.12-slim

WORKDIR /app

COPY ComputerIDEProject/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ComputerIDEProject/ .

RUN SECRET_KEY=build-placeholder python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "IDESite.wsgi"]
