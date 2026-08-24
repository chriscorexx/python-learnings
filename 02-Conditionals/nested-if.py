age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("You need an ID")
else:
    print("You must be 18 or older")
