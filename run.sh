!#/bin/bash

echo "hello"

mkdir data
touch data/data.txt
echo : "hello" > data.txt
cat data.txt

Sum=01
word="word"
text1="word word"

echo $Sum
echo "hello from $Sum"
echo "hello from $Sum hey there"
echo "hello from $word hey there"
echo "hello from $text1 hey there"


echo "Today's date: $(date)"
echo $(pwd)
date