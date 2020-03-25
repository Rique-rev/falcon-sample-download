FROM frolvlad/alpine-python3

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r /app/src/requirements.txt

WORKDIR /app

WORKDIR /app/src

EXPOSE 8080

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "main:api"]
