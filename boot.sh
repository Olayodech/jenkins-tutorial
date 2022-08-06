#!/bin/bash

source venv/bin/activate
flask db upgrade
exec python3 application/app.py