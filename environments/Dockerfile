# https://hub.docker.com/r/nikolaik/python-nodejs
# https://github.com/nikolaik/docker-python-nodejs
ARG BASE_IMAGE=nikolaik/python-nodejs:python3.8-nodejs16-slim
FROM ${BASE_IMAGE}

ARG PROJECT_NAME=AwsCdkTemplate
ARG USER_NAME=pn
ARG APPLICATION_DIRECTORY=/home/${USER_NAME}/${PROJECT_NAME}

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    PYTHONPATH=${APPLICATION_DIRECTORY}

RUN apt update && apt install --no-install-recommends -y make

WORKDIR ${APPLICATION_DIRECTORY}
RUN npm install --global npm-check-updates aws-cdk
