#!/bin/bash


# Lancer l'application Flask
gunicorn --bind=0.0.0.0 --timeout 600 app:app