FROM python:3.5


ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt --no-cache-dir
