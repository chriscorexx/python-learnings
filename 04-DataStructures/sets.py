# ==========================================
# Python Sets
# ==========================================


# ------------------------------------------
# 1. Creating a Set
# ------------------------------------------

fruits = {"Apple", "Banana", "Mango"}

print(fruits)


# ------------------------------------------
# 2. Duplicate Values
# ------------------------------------------

numbers = {1, 2, 3, 2, 4, 1}

print(numbers)


# ------------------------------------------
# 3. Adding Items
# ------------------------------------------

fruits.add("Grapes")

print(fruits)


# ------------------------------------------
# 4. Adding Multiple Items
# ------------------------------------------

fruits.update(["Orange", "Pineapple"])

print(fruits)


# ------------------------------------------
# 5. Removing an Item
# ------------------------------------------

fruits.remove("Banana")

print(fruits)


# ------------------------------------------
# 6. discard()
# ------------------------------------------

fruits.discard("Apple")

print(fruits)


# ------------------------------------------
# 7. Checking if an Item Exists
# ------------------------------------------

if "Mango" in fruits:
    print("Mango is in the set")


# ------------------------------------------
# 8. Looping Through a Set
# ------------------------------------------

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 9. Set Length
# ------------------------------------------

print("Length:", len(fruits))


# ------------------------------------------
# 10. Union
# ------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1.union(set2)

print(combined)


# ------------------------------------------
# 11. Intersection
# ------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

common = set1.intersection(set2)

print(common)


# ------------------------------------------
# 12. Difference
# ------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference = set1.difference(set2)

print(difference)


# ------------------------------------------
# 13. Symmetric Difference
# ------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference = set1.symmetric_difference(set2)

print(difference)


# ------------------------------------------
# 14. Converting a List to a Set
# ------------------------------------------

numbers_list = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = set(numbers_list)

print(unique_numbers)


# ------------------------------------------
# 15. Empty Set
# ------------------------------------------

empty_set = set()

print(empty_set)
