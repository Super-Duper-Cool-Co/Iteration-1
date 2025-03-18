FROM python:latest

RUN apt-get update && apt-get install -y sudo python3-pandas && pip install pandas

COPY Files/SDCC_Database.csv /Files/SDCC_Database.csv
COPY backend.py /

CMD [ "python", "./backend.py" ]