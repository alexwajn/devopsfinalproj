FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python3 -m flask --app flaskcalcapp run --host=0.0.0.0
