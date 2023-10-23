#!/bin/sh
echo "Migrating..."
python manage.py migrate
exec "$@"