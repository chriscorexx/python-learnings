# ==========================================
# Python break Statement
# ==========================================


# ------------------------------------------
# 1. Basic break
# ------------------------------------------

for i in range(1, 11):
    if i == 5:
        break

    print(i)


# ------------------------------------------
# 2. Stop a While Loop
# ------------------------------------------

count = 1

while count <= 10:
    if count == 6:
        break

    print(count)
    count += 1


# ------------------------------------------
# 3. Find a Number
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Found:", number)
        break


# ------------------------------------------
# 4. Search for a Name
# ------------------------------------------

names = ["Alex", "John", "Chris", "Sam"]

for name in names:
    if name == "Chris":
        print("Chris found!")
        break


# ------------------------------------------
# 5. User Input with break
# ------------------------------------------

while True:
    command = input("Enter a command (quit to exit): ")

    if command == "quit":
        print("Exiting...")
        break

    print("You entered:", command)


# ------------------------------------------
# 6. Password Example
# ------------------------------------------

correct_password = "python"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted!")
        break

    print("Wrong password. Try again.")
