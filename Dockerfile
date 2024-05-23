FROM python:3.10

ENV SPRING_HOST_NAME='127.0.0.1'
ENV SPRING_HOST_PORT='8080'

COPY . app/
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

RUN echo $SPRING_HOST_NAME
RUN echo $SPRING_HOST_PORT

EXPOSE 5000
CMD [ "flask","run","--host=0.0.0.0" ]