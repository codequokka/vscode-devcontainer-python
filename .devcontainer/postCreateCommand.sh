#!/bin/sh
# postCreateCommand.sh

echo "Starting setup..."

sudo chown -R vscode:vscode .

# Poetry
# poetry config virtualenvs.in-project true
# poetry install

# Pip
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt

echo "Finished setup"
