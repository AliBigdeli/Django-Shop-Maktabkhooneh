#!/bin/bash
# Run Django tests
set -e

echo "====== Running tests... ======"
docker compose exec backend python manage.py test

echo "====== Tests Complete ======"