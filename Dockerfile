FROM python:3.7.3

WORKDIR ~/sub

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run.py
ADD config.ini

ENTRYPOINT ["python", "~/sub/run.py"]