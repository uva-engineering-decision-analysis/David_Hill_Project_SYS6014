#!/bin/bash
# init

function pause(){
   read -p "$*"
} 

cd src/
python dozerscraper.py
python cleandata.py
python datagen.py

pause 'Press [Enter] key to continue...'