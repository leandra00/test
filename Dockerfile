FROM python:3.6

ENV PYTHONUNBUFFERED 1
ADD . /my-django-app

WORKDIR /my-django-app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD [ "runserver", "0.0.0.0:8000" ]
