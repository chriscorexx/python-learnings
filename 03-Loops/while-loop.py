# Python While Loops


# 1. Basic While Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# 2. Countdown

number = 5

while number > 0:
    print(number)
    number -= 1

print("Done!")


# 3. While Loop with User Input

age = int(input("Enter your age: "))

while age < 18:
    print("You are under 18.")
    age = int(input("Enter your age again: "))

print("You are 18 or older.")


# 4. Sum Using a While Loop

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Sum:", total)


# 5. Multiplication Table

number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1


# 6. Infinite Loop Example

# Be careful with infinite loops.
# The condition will always remain True.

# while True:
#     print("This will run forever")


# 7. Simple Password Loop

password = ""

while password != "python":
    password = input("Enter the password: ")

print("Correct password!")
