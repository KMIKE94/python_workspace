FROM python:3.6-alpine

COPY . /tmp/
COPY templates/ /tmp/templates/

RUN pip install flask
# Allows us to use the Swagger specification
# includes validation of inputs and outputs
RUN pip install connexion 
RUN pip install connexion[swagger-ui] 
RUN pip install Flask-SQLAlchemy==2.1 flask-marshmallow marshmallow-sqlalchemy marshmallow
RUN python /tmp/build_database.py

CMD ["python","/tmp/server.py"]