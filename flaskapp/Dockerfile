# Refactor to use multi-stage build with builder & release stages
FROM python:3

WORKDIR /app

RUN apt update

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
