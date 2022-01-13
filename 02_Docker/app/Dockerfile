FROM python:3.10

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

CMD ["/usr/local/bin/python", "manage.py", "migrate"]
CMD ["/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
