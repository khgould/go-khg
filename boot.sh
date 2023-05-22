#!/bin/bash
# this script is used to boot a Docker container
source venv/bin/activate
exec gunicorn -b :8080 --access-logfile - --error-logfile - go-khg:app