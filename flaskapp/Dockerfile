FROM python:3

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

# Install apt dependencies
RUN apt update

# Install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# RUN flask init-db

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
