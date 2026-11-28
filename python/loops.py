
for number in range(1, 6):
    print(number)


start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))
for number in range(start_number, end_number + 1):
    print(number)


languages = ["Python", "Java", "C"]
for language in languages:
    print(language)


word = input("Enter a word: ")
for letter in word:
    print(letter)


count = 1
while count <= 5:
    print(count)
    count += 1


for number in range(1, 11):
    if number == 6:
        break
    print(number)


for number in range(1, 11):
    if number == 5:
        continue
    if number == 9:
        break
    print(number)


limit = int(input("Enter n: "))
total = 0

for i in range(1, limit + 1):
    total += i

print(f"Sum from 1 to {limit} is: {total}")


for number in range(1, 21):
    if number % 2 == 0:
        print(number)


table_of = int(input("Enter a number for its table: "))
for multiplier in range(1, 11):
    print(f"{table_of} x {multiplier} = {table_of * multiplier}")