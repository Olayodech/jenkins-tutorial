#!/bin/bash

source venv/bin/activate
flask db upgrade
exec flask run