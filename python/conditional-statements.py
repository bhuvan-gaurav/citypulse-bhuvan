
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Pass")
else:
    print("Try again")


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is larger")
elif b > a:
    print(f"{b} is larger")
else:
    print("Both are equal")



first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print(f"{first_number} is larger")
elif second_number > first_number:
    print(f"{second_number} is larger")
else:
    print("Both are equal")
    