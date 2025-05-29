#!/bin/bash
pip install -r /home/site/wwwroot/tasktracker/requirements.txt
gunicorn --bind=0.0.0.0 --chdir /home/site/wwwroot/tasktracker tasktracker.app:app