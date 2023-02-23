
FROM python:3.7
RUN mkdir /usr/src/myapp -p
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN pip install -r requirements.txt
WORKDIR /usr/src/myapp
CMD python manage.py runserver 0:8000

