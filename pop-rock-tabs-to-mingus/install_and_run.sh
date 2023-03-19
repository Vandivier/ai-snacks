#!/bin/bash

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Initialize the Poetry environment and install dependencies
echo "Initializing Poetry environment and installing dependencies..."
poetry install

# Run the main Python script
echo "Running the main Python script..."
poetry run python main.py
