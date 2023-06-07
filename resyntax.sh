#!/bin/bash

# purpose:
# - convert image names retrieved by a Basler camera into Dr. Niklas Manz's (PI)
# prefered format

# use:
# in a command line interface run the following two commands
# chmod +x /path/to/resyntax.sh 
# /path/to/resyntax.sh YYYY-MM-DD_HH-MM (see preconditions below)

# preconditions: 
# - ran in a folder containing only .tiff files starting with "Basler_"
# - image files can be numerically sorted in accordance with order taken
# - script is passed a start datetime in the format "YYYY-MM-DD_HH-MM"

# postconditions:
# - a sibling folder named "YYYY-MM-DD_HH-MM" containing images
# - images are named in accordance with format "YYYY-MM-DD_HH-MM_XXXX" 
# where XXXX is an incrementing number starting at 1000
# - original directory and every recursive child in it is deleted

export DIRECTORY=$(pwd)
export DATETIME=$1
export NUMBER_OF_FRAMES=$(cd $DIRECTORY ; ls -1 | wc -l)
export index=1000

mkdir ../$DATETIME
find . -type f -name 'Basler_*' | sort -n | while read FILE ;
do
    filename=${FILE} ;
    newfilename="${DATETIME}_${index}.tiff" ;
    mv "$filename" "../${DATETIME}/${newfilename}" ;
    ((index++));
done

cd .. ;
rm -r $DIRECTORY ;