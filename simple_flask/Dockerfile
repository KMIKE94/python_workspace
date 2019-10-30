FROM python:3

ADD ./* /tmp/

RUN pip install flask
# Allows us to use the Swagger specification
# includes validation of inputs and outputs
RUN pip install connexion
RUN pip install connexion[swagger-ui]

CMD ["python","/tmp/server.py"]