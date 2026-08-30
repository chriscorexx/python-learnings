# ==========================================
# Python Lists
# ==========================================


# ------------------------------------------
# 1. Creating a List
# ------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# ------------------------------------------
# 2. Accessing List Items
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
# 4. Changing List Items
# ------------------------------------------

fruits[0] = "Orange"

print(fruits)


# ------------------------------------------
# 5. Adding Items - append()
# ------------------------------------------

fruits.append("Grapes")

print(fruits)


# ------------------------------------------
# 6. Adding Items - insert()
# ------------------------------------------

fruits.insert(1, "Apple")

print(fruits)


# ------------------------------------------
# 7. Removing Items - remove()
# ------------------------------------------

fruits.remove("Banana")

print(fruits)


# ------------------------------------------
# 8. Removing Items - pop()
# ------------------------------------------

removed_fruit = fruits.pop()

print("Removed:", removed_fruit)
print(fruits)


# ------------------------------------------
# 9. List Length
# ------------------------------------------

print("Length:", len(fruits))


# ------------------------------------------
# 10. Checking if an Item Exists
# ------------------------------------------

if "Mango" in fruits:
    print("Mango is in the list")


# ------------------------------------------
# 11. Looping Through a List
# ------------------------------------------

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 12. List Indexes with range()
# ------------------------------------------

for i in range(len(fruits)):
    print(i, fruits[i])


# ------------------------------------------
# 13. List Slicing
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[2:5])
print(numbers[:3])
print(numbers[2:])


# ------------------------------------------
# 14. Sorting a List
# ------------------------------------------

numbers.sort()

print(numbers)


# ------------------------------------------
# 15. Reversing a List
# ------------------------------------------

numbers.reverse()

print(numbers)


# ------------------------------------------
# 16. Copying a List
# ------------------------------------------

original = [1, 2, 3]

copy = original.copy()

print(original)
print(copy)


# ------------------------------------------
# 17. Clearing a List
# ------------------------------------------

temporary = [1, 2, 3]

temporary.clear()

print(temporary)


# ------------------------------------------
# 18. Lists Can Store Different Data Types
# ------------------------------------------

data = ["Chris", 18, 5.5, True]

print(data)


# ------------------------------------------
# 19. Nested Lists
# ------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[0])
print(matrix[0][0])
print(matrix[1][2])


# ------------------------------------------
# 20. Looping Through a Nested List
# ------------------------------------------

for row in matrix:
    for number in row:
        print(number, end=" ")

    print()
