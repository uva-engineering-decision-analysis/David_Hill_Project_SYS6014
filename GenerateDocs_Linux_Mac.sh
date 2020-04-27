#!/bin/bash
# init

function pause(){
   read -p "$*"
} 

pandoc  -s ./Final_Paper.md -o ./docs/Final_Paper.pdf
pandoc  -s ./project_proposal_FINAL.ipynb -o ./docs/project_proposal_FINAL.pdf
pandoc -t beamer -s proposal_presentation.md -V theme:CambridgeUS -o ./docs/proposal_presentation.pdf

pause 'Press [Enter] key to continue...'