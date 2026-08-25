#Python for loops

#Basic for loops

for i in range (5):
    print(i)

#for loop in a string

name = "Chris"

for character in name:
    print(character)

#for loop with a list

languages = ["Java","C++", "Python", "Ruby"]
for language in languages:
    print(languages)


#using range function
for i in range (1, 6):
    print(i)


#Doing calculations in a loop
for i in range (1, 6):
    print(i*2)



#Multiplication table

number = int(input("Enter a number"))
for i in range(1, 11):
    print(number, "x", i, "=", number*i)



#Print even number

for i in range(2, 21, 2):
    print(i)


#calulated sum  

total = 0

for i in range(1, 101):
    total = total + i

print("Sum:", total)
