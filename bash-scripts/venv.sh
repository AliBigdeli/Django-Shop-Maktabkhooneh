#!/bin/bash
set -e

echo "====== Setup Project ======"

# create virtualenvironment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# activate virtualenvirnment
PROJECT_DIR=$(dirname "$0")/..
source "$PROJECT_DIR/venv/bin/activate"

# update & install pip
pip install --upgrade pip

# install requirements
pip install -r "$PROJECT_DIR/requirements.txt"

echo "====== Setup Complete ======"
