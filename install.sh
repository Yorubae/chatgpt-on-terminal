#!/bin/bash

echo "Please enter your API key:"
read api_key

while [[ -z "${api_key}" ]]
do
    echo "API key cannot be empty. Please enter again:"
    read api_key
done

echo "apiID=${api_key}" > .env
echo "API key has been saved as apiID in .env file."
echo "Installing required dependecies!"
pip install -r requirements.txt
echo "You're good to go!"
