#!/bin/bash

cd /home/site/wwwroot/tasktracker
gunicorn --bind=0.0.0.0 --timeout 600 app:app