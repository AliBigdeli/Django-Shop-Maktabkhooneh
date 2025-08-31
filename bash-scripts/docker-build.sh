#!/bin/bash
set -e

echo "====== Docker Images Built & Starting Docker Containers ======"

PROJECT_DIR=$(dirname "$0")/..
cd "$PROJECT_DIR"

docker-compose build 

echo "====== Docker Images Built ======"