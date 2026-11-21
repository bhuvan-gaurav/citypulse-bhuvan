# # echo "enter input:"
# # read num

# # echo $num

# read -p "Enter a number: " num

# if [ $num -gt 0 ]; then
#   echo "$num is positive"
# elif [ $num -lt 0 ]; then
#   echo "$num is negative"
# else
#   echo "$num is zero"
# fi

# # read -p "enter number" sum

# # echo $sum


# read -p "Enter your name: " name
# read -p "Enter your roll number: " rollno
# read -p "Enter your college: " college

# echo ""
# echo "----- Student Details -----"
# echo "Name    : $name"
# echo "Roll No : $rollno"
# echo "College : $college"
# echo "Date    : $(date)"

# touch data.txt
# cat 

#!/bin/bash

read -p "Enter your age: " age

if [ $age -lt 0 ]; then
  echo "$age is not a valid age"
elif [ $age -le 12 ]; then
  echo "$age: Child"
elif [ $age -le 19 ]; then
  echo "$age: Teenager"
elif [ $age -le 59 ]; then
  echo "$age: Adult"
else
  echo "$age: Old"
fi