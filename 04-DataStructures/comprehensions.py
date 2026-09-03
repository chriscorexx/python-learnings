# ==========================================
# Python Comprehensions
# ==========================================


# ------------------------------------------
# 1. Basic List Comprehension
# ------------------------------------------

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)


# Same thing using a list comprehension

numbers = [number for number in range(1, 6)]

print(numbers)


# ------------------------------------------
# 2. Squaring Numbers
# ------------------------------------------

squares = [number ** 2 for number in range(1, 6)]

print(squares)


# ------------------------------------------
# 3. List Comprehension with Condition
# ------------------------------------------

even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)


# ------------------------------------------
# 4. Odd Numbers
# ------------------------------------------

odd_numbers = [
    number
    for number in range(1, 11)
    if number % 2 != 0
]

print(odd_numbers)


# ------------------------------------------
# 5. Filtering a List
# ------------------------------------------

numbers = [10, 15, 20, 25, 30, 35]

greater_than_20 = [
    number
    for number in numbers
    if number > 20
]

print(greater_than_20)


# ------------------------------------------
# 6. Changing List Items
# ------------------------------------------

names = ["chris", "alex", "john"]

uppercase_names = [
    name.upper()
    for name in names
]

print(uppercase_names)


# ------------------------------------------
# 7. String Comprehension
# ------------------------------------------

word = "Python"

letters = [letter for letter in word]

print(letters)


# ------------------------------------------
# 8. Nested Loop Comprehension
# ------------------------------------------

pairs = [
    (i, j)
    for i in range(3)
    for j in range(3)
]

print(pairs)


# ------------------------------------------
# 9. Set Comprehension
# ------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = {
    number
    for number in numbers
}

print(unique_numbers)


# ------------------------------------------
# 10. Dictionary Comprehension
# ------------------------------------------

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)


# ------------------------------------------
# 11. Dictionary Comprehension with Condition
# ------------------------------------------

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)
