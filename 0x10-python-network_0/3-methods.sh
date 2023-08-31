#!/bin/bash
# Script that sends a request to display HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
