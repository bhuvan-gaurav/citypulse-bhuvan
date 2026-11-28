# fruits = ["apple", "banana", "mango"]

# new_fruit = input("Enter a fruit to add: ")
# fruits.append(new_fruit)
# fruits.insert(1, "kiwi")
# print(fruits)

# remove_fruit = input("Enter a fruit to remove: ")
# if remove_fruit in fruits:
#     fruits.remove(remove_fruit)
# else:
#     print(f"{remove_fruit} is not in the list")

# fruits.sort()
# print("Sorted:", fruits)
# print("Total fruits:", len(fruits))
# print("First 2:", fruits[:2])

# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:3])    
# print(numbers[::2])    

# squares = [num ** 2 for num in range(1, 6)]
# print("Squares:", squares)



students = {
    "s1": {"name": "Bhuvan", "age": 19, "cgpa": 9.1},
    "s2": {"name": "Rohan", "age": 20, "cgpa": 8.4},
}


print(students["s1"]["name"])    
print(students["s2"]["cgpa"])  
 


students["s1"]["cgpa"] = 9.3


students["s2"]["city"] = "Bangalore"


students["s3"] = {"name": "Deeraj", "age": 18, "cgpa": 8.9}


print(students["s1"].get("email", "No email"))


for student_id, details in students.items():
    print(f"\nID: {student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")

del students["s2"]["city"]
del students["s3"]

