#!/bin/bash

# Define the URL of the zip file
MODEL_ZIP_URL="https://drive.usercontent.google.com/download?id=1P7Igx_aPNn-EX0N_wYwkMewYDArWCyeV&export=download&authuser=0&confirm=t&uuid=da35fd8c-19aa-47e4-a34c-deb0fa46c7de&at=APZUnTW4C9P0qozpoYhbR7_uMcyM:1700692950690"

# Create a directory named 'model' if it doesn't exist
mkdir -p model

# Download the zip file
wget "$MODEL_ZIP_URL" -O models.zip

# Extract the zip file into the 'model' directory
unzip models.zip -d model

# Cleanup: Remove the downloaded zip file
rm models.zip

echo "Models downloaded and extracted into the 'model' directory."
