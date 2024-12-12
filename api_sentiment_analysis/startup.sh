#!/bin/bash
pip install --upgrade pip
pip install -r /home/site/wwwroot/requirements.txt

# Lancer l'application Flask
gunicorn --bind=0.0.0.0 --timeout 600 app:app