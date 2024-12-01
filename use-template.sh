#!/bin/bash

# Determining whether to get date automatically or through args
if test "$#" -eq 0; then
    echo "Determining date automatically"
    year=$(date +%Y)
    day=$(date +%-d)

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
filename1=$day_dir\_part1.py
filename2=$day_dir\_part2.py

if [ ! -d "$year_dir" ]; then
    echo "Year Directory '$year' does not exist. Creating it."
    mkdir $year
fi
mkdir $new_dir
cp ./template/boilerplate.py $new_dir/$filename1
cp ./template/boilerplate.py $new_dir/$filename2

# Set the data directory in the python files to be run from the root of this repo
sed -i "s|./|./$year/$day_dir/|g" $new_dir/$filename1
sed -i "s|./|./$year/$day_dir/|g" $new_dir/$filename2

# Get the public test case, extract it from the HTML, remove extra newline
curl https://adventofcode.com/$year/day/$day > $new_dir/testcase.txt
sed -zi 's|.*<pre><code>||' $new_dir/testcase.txt
sed -zi 's|</code>.*||' $new_dir/testcase.txt
head -c -1 $new_dir/testcase.txt > tmp; mv tmp $new_dir/testcase.txt

# Get the session-based input data
session=$(cat .env)
curl --cookie "session=$session" https://adventofcode.com/$year/day/$day/input > $new_dir/data.txt