FROM python

LABEL maintainer="matin20001313@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /user/src/app

COPY ./requirements.txt .

RUN pip install --upgrade && pip install -r requirements.txt

COPY ./core .