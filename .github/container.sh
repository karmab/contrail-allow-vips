#!/bin/bash

set -ex

TAG=$(git rev-parse --short HEAD)
docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD docker.io
docker build -t quay.io/karmab/contrail-allow-vips:latest -f Dockerfile .
docker tag quay.io/karmab/contrail-allow-vips:latest quay.io/karmab/contrail-allow-vips:$TAG

docker login -u $QUAY_USERNAME -p $QUAY_PASSWORD quay.io
docker push quay.io/karmab/contrail-allow-vips:latest
docker push quay.io/karmab/contrail-allow-vips:$TAG
