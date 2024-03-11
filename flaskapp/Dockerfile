FROM python:3

WORKDIR /app

# Install apt dependencies
RUN apt update

# Install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
