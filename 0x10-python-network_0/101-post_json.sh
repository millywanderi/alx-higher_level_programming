#!/bin/bash
# Script that send json POST request and displays the body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
