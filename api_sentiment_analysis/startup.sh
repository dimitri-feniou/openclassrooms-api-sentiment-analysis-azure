#!/bin/bash

# Activer l'environnement virtuel
source antenv/bin/activate

# Lancer l'application Flask
gunicorn --bind=0.0.0.0 --timeout 600 app:app