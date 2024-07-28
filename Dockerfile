FROM python:3

WORKDIR api

COPY requirements.txt /api

RUN pip install -r requirements.txt

COPY . /api

CMD  ["uvicorn","--host", "0.0.0.0", "--port", "8000", "main:app", "--reload", "--env-file",".env"]


