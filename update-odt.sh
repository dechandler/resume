#!/bin/bash

./template.py
zip -u resume.odt *.xml
soffice --headless --convert-to pdf resume.odt
