#!/bin/bash
# Collect static files
set -e

echo "====== Collecting static files... ======"

docker compose exec backend python manage.py collectstatic --noinput

echo "====== Static Files Collected ======"
