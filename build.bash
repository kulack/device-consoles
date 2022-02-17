#!/usr/bin/env bash

IMAGE=fkulack/device-consoles
TAG=1.0.0

# Prereq:
#   docker buildx create --use

docker buildx build --push --platform linux/arm64,linux/amd64 --tag "$IMAGE:$TAG" .
