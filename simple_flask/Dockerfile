FROM python:3

COPY people.py /tmp/
COPY server.py /tmp/
COPY swagger.yml /tmp/

RUN mkdir /tmp/templates/
COPY /templates/home.html /tmp/templates/

RUN pip install flask
# Allows us to use the Swagger specification
# includes validation of inputs and outputs
RUN pip install connexion 
RUN pip install connexion[swagger-ui] 
RUN pip install Flask-SQLAlchemy==2.1 flask-marshmallow marshmallow-sqlalchemy marshmallow

CMD ["python","/tmp/server.py"]