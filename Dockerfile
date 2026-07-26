FROM python:3.13
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/
WORKDIR /code
RUN pip -V
RUN python --version
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "simoes_tecnologia.wsgi:application", "--bind", "0.0.0.0:8000"]
