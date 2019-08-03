#!/bin/bash
CONTAINER=django-history
mkdir -p tmp
#
# https://docs.docker.com/engine/reference/commandline/image_build/
docker image build -t $CONTAINER -f - . << EOS
FROM python:3
WORKDIR /code
ADD . /code
RUN pip install -r /code/requirements/pypi.txt
RUN pip install -e /code/packages/django-mylinks
EOS
#
docker container run -v $PWD/tmp:/result $CONTAINER  /code/bin/docker-test-run.bash