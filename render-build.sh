#!/usr/bin/env bash

# Exit on first error
set -e

# Install the aria2c command-line tool using apt
apt-get update
apt-get install -y aria2

# Install Python dependencies from requirements.txt
pip install -r requirements.txt
