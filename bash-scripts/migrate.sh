#!/bin/bash
# Run Django migrations
set -e

echo "====== Running migrations... ======"

docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate

echo "====== Migrations Complete ======"
