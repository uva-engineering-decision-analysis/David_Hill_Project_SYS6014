#!/bin/bash
# init

function pause(){
   read -p "$*"
} 

cd src/
python decisiontool.py

pause 'Press [Enter] key to continue...'