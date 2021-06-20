#!/bin/sh
inputFile=${1}
outfiletxt=${2}
outfileimg=${3}

python /input/script.py --inputFile ${inputFile} --outputFolderTxt ${outfiletxt} --outputFolderImg ${outfileimg}