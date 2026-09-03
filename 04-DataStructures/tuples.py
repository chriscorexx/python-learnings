# ==========================================
# Python Tuples
# ==========================================


# ------------------------------------------
# 1. Creating a Tuple
# ------------------------------------------

fruits = ("Apple", "Banana", "Mango")

print(fruits)


# ------------------------------------------
# 2. Accessing Tuple Items
# ------------------------------------------

print(fruits[0])
print(fruits[1])
print(fruits[2])


# ------------------------------------------
# 3. Negative Indexing
# ------------------------------------------

print(fruits[-1])
print(fruits[-2])


# ------------------------------------------
# 4. Tuple Length
# ------------------------------------------

print("Length:", len(fruits))


# ------------------------------------------
# 5. Looping Through a Tuple
# ------------------------------------------

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 6. Checking if an Item Exists
# ------------------------------------------

if "Mango" in fruits:
    print("Mango is in the tuple")


# ------------------------------------------
# 7. Different Data Types
# ------------------------------------------

data = ("Chris", 18, 5.5, True)

print(data)


# ------------------------------------------
# 8. Single Item Tuple
# ------------------------------------------

number = (10,)

print(number)


# ------------------------------------------
# 9. Tuple Without the Comma
# ------------------------------------------

not_a_tuple = (10)

print(not_a_tuple)
print(type(not_a_tuple))


# ------------------------------------------
# 10. Tuple Unpacking
# ------------------------------------------

person = ("Chris", 18, "India")

name, age, country = person

print(name)
print(age)
print(country)


# ------------------------------------------
# 11. Converting Tuple to List
# ------------------------------------------

numbers = (1, 2, 3, 4, 5)

numbers_list = list(numbers)

print(numbers_list)


# ------------------------------------------
# 12. Modifying Through a List
# ------------------------------------------

numbers_list.append(6)

numbers = tuple(numbers_list)

print(numbers)


# ------------------------------------------
# 13. Tuple Slicing
# ------------------------------------------

numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])
print(numbers[2:])
print(numbers[:3])


# ------------------------------------------
# 14. Nested Tuples
# ------------------------------------------

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix)
print(matrix[0])
print(matrix[1][2])


# ------------------------------------------
# 15. Tuple Methods
# ------------------------------------------

numbers = (1, 2, 2, 3, 2, 4)

print(numbers.count(2))
print(numbers.index(3))
