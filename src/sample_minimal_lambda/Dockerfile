ARG BASE_IMAGE=python:3.9.13-slim-bullseye
FROM --platform=amd64 ${BASE_IMAGE} as base

ARG PROJECT_NAME=sample
ARG APPLICATION_DIRECTORY=/${PROJECT_NAME}

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    PYTHONPATH=${APPLICATION_DIRECTORY}

WORKDIR ${APPLICATION_DIRECTORY}

# Install requirements
COPY requirements.txt .
RUN pip3 install -U pip \
    && pip3 install -r requirements.txt --target ${APPLICATION_DIRECTORY}

FROM base as lambda

# Copy application code
COPY handlers.py sample.py ./

# Set up entrypoint
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY lambda-entrypoint.sh /
RUN chmod 755 /usr/bin/aws-lambda-rie /lambda-entrypoint.sh
ENTRYPOINT [ "/lambda-entrypoint.sh" ]