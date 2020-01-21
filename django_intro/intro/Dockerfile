FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
