FROM python:3.7-slim-buster

WORKDIR /opt/CTFd
RUN mkdir -p /var/log/CTFd /var/uploads

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libffi-dev \
        libssl-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY deployment/dev/frontend/build-image/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN adduser \
    --disabled-login \
    -u 1001 \
    --gecos "" \
    --shell /bin/bash \
    ctfd

USER 1001
EXPOSE 8000
