FROM python:3.5
RUN apt-get update
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

