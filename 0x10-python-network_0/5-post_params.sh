#!/bin/bash
# Script that make a POST request, display response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
