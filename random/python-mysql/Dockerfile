FROM python:3.6-alpine

COPY . /app/
RUN pip install -r /app/requirements.txt

CMD [ "python", "/app/server.py" ]