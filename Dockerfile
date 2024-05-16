FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip isntall -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$POST app:app