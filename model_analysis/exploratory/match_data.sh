#!/bin/bash

# using a find command to match the data in "./data" to what's referenced in notebooks
find \
	-L \
	data/ \
	-type f \
	-exec bash -c 'grep `basename {}` notebooks/ -R >> /dev/null' \; \
	-exec bash -c 'mkdir -p datastash/`dirname {}`' \; \
	-exec mv {} datastash/{} \;
