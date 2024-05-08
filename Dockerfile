FROM python:3.11-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelarate
RUN pip uninstall -y transformers accelarate
RUN pip install transformers accelarate

CMD ["python3", "app.py"]
