# ==========================================
# Python Dictionaries
# ==========================================


# ------------------------------------------
# 1. Creating a Dictionary
# ------------------------------------------

person = {
    "name": "Chris",
    "age": 18,
    "country": "India"
}

print(person)


# ------------------------------------------
# 2. Accessing Dictionary Values
# ------------------------------------------

print(person["name"])
print(person["age"])


# ------------------------------------------
# 3. Using get()
# ------------------------------------------

print(person.get("country"))


# ------------------------------------------
# 4. Adding a New Key-Value Pair
# ------------------------------------------

person["city"] = "Pune"

print(person)


# ------------------------------------------
# 5. Changing a Value
# ------------------------------------------

person["age"] = 19

print(person)


# ------------------------------------------
# 6. Removing an Item
# ------------------------------------------

person.pop("city")

print(person)


# ------------------------------------------
# 7. Dictionary Length
# ------------------------------------------

print("Length:", len(person))


# ------------------------------------------
# 8. Checking if a Key Exists
# ------------------------------------------

if "name" in person:
    print("Name exists")


# ------------------------------------------
# 9. Looping Through Keys
# ------------------------------------------

for key in person:
    print(key)


# ------------------------------------------
# 10. Looping Through Values
# ------------------------------------------

for value in person.values():
    print(value)


# ------------------------------------------
# 11. Looping Through Keys and Values
# ------------------------------------------

for key, value in person.items():
    print(key, ":", value)


# ------------------------------------------
# 12. Dictionary Keys
# ------------------------------------------

print(person.keys())


# ------------------------------------------
# 13. Dictionary Values
# ------------------------------------------

print(person.values())


# ------------------------------------------
# 14. Copying a Dictionary
# ------------------------------------------

person_copy = person.copy()

print(person_copy)


# ------------------------------------------
# 15. Nested Dictionary
# ------------------------------------------

students = {
    "student1": {
        "name": "Chris",
        "age": 18
    },
    "student2": {
        "name": "Alex",
        "age": 20
    }
}

print(students)


# ------------------------------------------
# 16. Accessing Nested Dictionary Values
# ------------------------------------------

print(students["student1"]["name"])
print(students["student2"]["age"])


# ------------------------------------------
# 17. Dictionary with Different Data Types
# ------------------------------------------

data = {
    "name": "Chris",
    "age": 18,
    "height": 5.5,
    "student": True
}

print(data)


# ------------------------------------------
# 18. Clearing a Dictionary
# ------------------------------------------

temporary = {
    "a": 1,
    "b": 2
}

temporary.clear()

print(temporary)
