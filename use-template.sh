#!/bin/bash

# Determining whether to get date automatically or through args
if test "$#" -eq 0; then
    echo "Determining date automatically"
    year=$(date +%Y)
    day=$(date +%d)

elif test "$#" -eq 2; then
    echo "Determining date through args"    
    year=$1
    day=$2
    
else
    echo "Invalid Number of Arguments. Use './use-template.sh' for automatic date determination. Use './use-template.sh <year> <day>' to set date."
    exit 1
fi

# Make new directory with boiler plate code
year_dir=$year
day_dir=day$day
new_dir=$year/$day_dir
filename=$day_dir.py

if [ ! -d "$year_dir" ]; then
    echo "Year Directory '$year' does not exist. Creating it."
    mkdir $year
fi
mkdir $new_dir
cp ./template/boilerplate.py $new_dir/$filename

# Get the input data
session=$(cat .env)
curl --cookie "session=$session" https://adventofcode.com/$year/day/$day/input > $new_dir/data.txt