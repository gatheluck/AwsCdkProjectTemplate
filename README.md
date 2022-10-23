# AWS CDK Project Template

[![MIT License](https://img.shields.io/github/license/cvpaperchallenge/Ascender?color=green)](LICENSE)

## What is this repository?

This repository is intended to be used as a template for development with AWS CDK. 

**NOTE**: Since we are still in the process of trial and error to find the best configuration, there may be major configuration changes in the future.

## Project Organization

```
    ├── .github/                   <- Settings for GitHub.
    │
    ├── environments/              <- Provision depends on environments.
    │
    ├── src/                       <- Source code. This sould be Python module.
    :   :
    │   ├── sample_minimal_lambda  <- Sample lambda code.
    │   │
    │   └── stacks                 <- Python code to define stacks.
    │
    ├── tests/                     <- Test codes.
    │
    ├── .flake8                    <- Setting file for Flake8.
    ├── .dockerignore
    ├── .gitignore
    ├── app.py                     <- Define application from stack.
    ├── cdk.json                   <- Setting file for AWS CDK.
    ├── LICENSE
    ├── Makefile                   <- Makefile used as task runner. 
    ├── poetry.lock                <- Lock file. DON'T edit this file manually.
    ├── poetry.toml                <- Setting file for Poetry.
    ├── pyproject.toml             <- Setting file for Project.
    └── README.md                  <- The top-level README for developers.

```

## Prerequisites

- [Docker](https://www.docker.com/) 
- [Docker Compose](https://github.com/docker/compose)
- (Optional) [NVIDIA Container Toolkit (nvidia-docker2)](https://github.com/NVIDIA/nvidia-docker)
- [AWS Cloud Development Kit (AWS CDK)](https://github.com/aws/aws-cdk)
- [AWS Cloud Development Kit Library](https://pypi.org/project/aws-cdk-lib/)
- (Optional) [AWS Serverless Application Model (SAM)](https://github.com/aws/serverless-application-model)

**NOTE**: Example codes in the README.md are written for `Docker Compose v2`. However, Ascender also should work under `Docker Compose v1`. If you are using `Docker Compose v1`, just replace `docker compose` in the example code by `docker-compose`.

## Prerequisites installation

Here, we show example prerequisites installation codes for Ubuntu. If prerequisites  are already installed your environment, please skip this section. If you want to install in another environment, please follow the officail documentations.

- Docker and Docker Compose: [Install Docker Engine](https://docs.docker.com/engine/install/)
- NVIDIA Container Toolkit (nvidia-docker2): [Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)


### Install Docker and Docker Compose

```bash
# Set up the repository
$ sudo apt update
$ sudo apt install ca-certificates curl gnupg lsb-release
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker and Docker Compose
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

If `sudo docker run hello-world` works, installation succeeded.

### (Optional) NVIDIA Container Toolkit

If you want to use GPU in Ascender, please install NVIDIA Container Toolkit (nvidia-docker2) too. NVIDIA Container Toolkit also requires some prerequisites to install. So please check thier [official documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#pre-requisites) first.

```bash
$ distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

$ sudo apt update
$ sudo apt install -y nvidia-docker2
$ sudo systemctl restart docker
```

If `sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi` works, installation succeeded.

### AWS Cloud Development Kit (AWS CDK) and AWS Cloud Development Kit Library

```bash
# Install AWS CDK
$ npm i -g aws-cdk

# Install AWS Cloud Development Kit Library
$ pip3 install aws-cdk-lib
```

You can check installed AWS CDK version by `cdk --version`.

### (Optional) AWS Serverless Application Model (SAM)

In this template, we use AWS Serverless Application Model (SAM) to execute test locally.

```bash
$ pip install aws-sam-cli
```

You can check installed version by `sam --version`.

## Quick start

### Start development

```bash
# Build Docker image and run container
$ cd environments/cpu
$ sudo docker compose up -d

# Run bash inside of container (jump into contaienr)
$ sudo docker compose exec core bash

# Create virtual environment and install dependent packages by Poetry
% poetry install
```

### Local test

Here we explain how to run local test. To run test locally, we use AWS Serverless Application Model (SAM).

```bash
# Please run followings from out side of the container
# Synthesizes CloudFormation template. This command creates some files under `cdk.out`
$ cdk synth

# Build and start API locally
$ sam build -t cdk.out/sample-minimal.template.json
$ sam local start-api
```

Now you can test API at `http://127.0.0.1:3000/sample` by default. You can try and test API by using `curl` as follows:

```bash
# Send GET request from different terminal
$ curl -X GET http://127.0.0.1:3000/sample

{"torch_version": "1.12.1+cu102"}
```

### Deployment

```bash
# Please run followings from out side of the container
# Synthesizes CloudFormation template. This command creates some files under `cdk.out`
$ cdk synth

# Build bootstrapping and deploy
$ sam build -t cdk.out/sample-minimal.template.json
$ cdk bootstrap
$ cdk deploy

# If it succeeded, AWS resources are created

# Tear down all created AWS resources
$ cdk destroy
```

### Stop development

```bash
$ cd environments/cpu
$ sudo docker compose stop
# If you want remove containers, please use `down` instead of `stop`
```
