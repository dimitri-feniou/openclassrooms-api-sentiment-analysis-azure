#!/bin/bash
pip install --upgrade pip
pip install -r /home/site/wwwroot/requirements.txt

# Lancer l'application Flask
gunicorn -w 4 -b 0.0.0.0:8000 run:app