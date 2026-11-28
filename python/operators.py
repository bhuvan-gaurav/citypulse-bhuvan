
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


marks = int(input("Enter your marks: "))
is_passed = marks >= 40
has_good_score = marks >= 75

print("Passed:", is_passed)
print("Good score:", has_good_score)
print("Both:", is_passed and has_good_score)
print("Either:", is_passed or has_good_score)
print("Not passed:", not is_passed)


bonus = 5
marks += bonus
print(f"Marks after bonus: {marks}")


number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


