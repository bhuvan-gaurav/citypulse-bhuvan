
# def say_hello():
#     print("Hello, everyone!")

# say_hello()
# say_hello()



# def greet(name):
#     print("Hello,", name)

# greet("Priya")
# greet("Rahul")



# def add(num1, num2):
#     return num1 + num2

# answer = add(10, 20)
# print(answer)



# def double(number):
#     return number * 2

# user_number = int(input("Enter a number: "))
# print(double(user_number))



# def check_even_odd(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# check_even_odd(7)
# check_even_odd(10)

def add_numbers(a, b):
    sum = a + b
    print("Sum =", sum)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add_numbers(a, b)



def calculate_grade(name, marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 40:
        grade = "Pass"
    else:
        grade = "Fail"
    print(name, "scored", marks, "- Grade:", grade)

calculate_grade("Anjali", 88)
calculate_grade("Ravi", 45)
calculate_grade("Sneha", 95)



def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(add(num1, num2))
elif operation == "-":
    print(subtract(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
else:
    print("Invalid operation")