FROM python:3.7.3

WORKDIR /sub
RUN mkdir csv

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run.py .

ENTRYPOINT ["python", "/sub/run.py"]