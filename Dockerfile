FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip config set global.trusted-host "pypi.org files.pythonhosted.org"
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["pytest"]
