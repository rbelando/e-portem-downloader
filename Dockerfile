FROM python:3.9-alpine3.13
LABEL maintainer="rbelando"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./e-portem-downloader /e-portem-downloader
WORKDIR /e-portem-downloader

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"
