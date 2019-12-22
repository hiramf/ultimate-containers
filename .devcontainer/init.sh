#!bin/bash
set -e

echo "Installing python requirements..."
pip install -r ./.devcontainer/requirements.txt

echo "Installing git..."
apt update
apt install git -y

exec "$@"