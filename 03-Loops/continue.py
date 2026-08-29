# ==========================================
# Python continue Statement
# ==========================================


# ------------------------------------------
# 1. Basic continue
# ------------------------------------------

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


# ------------------------------------------
# 2. Skip Even Numbers
# ------------------------------------------

for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)


# ------------------------------------------
# 3. Skip Odd Numbers
# ------------------------------------------

for i in range(1, 11):
    if i % 2 != 0:
        continue

    print(i)


# ------------------------------------------
# 4. Skip a Specific Number
# ------------------------------------------

for i in range(1, 11):
    if i == 7:
        continue

    print(i)


# ------------------------------------------
# 5. Continue with a List
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        continue

    print(number)


# ------------------------------------------
# 6. Skip Negative Numbers
# ------------------------------------------

numbers = [10, -5, 20, -10, 30, -15]

for number in numbers:
    if number < 0:
        continue

    print(number)


# ------------------------------------------
# 7. Continue with User Input
# ------------------------------------------

while True:
    value = input("Enter a number or 'quit': ")

    if value == "quit":
        break

    if not value.isdigit():
        print("Please enter a valid number.")
        continue

    print("You entered:", value)
