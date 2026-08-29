
#Basic nested loop

for i in range(3):
    for j in range(3):
        print(i,j)


#Rows and columns

for rows in range(4):
    for cols in range(3):
        print("*", end =" ")


#Number Pattern

for i in range(1,5):
    for j in range(i):
        print(i, end = " ")
print()


#Multiplication Tables

for i in range(1, 6):
    for j in range(1, 11):
        print(i*j , end = " ")
print()


#Nested loops with list

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for number in row:
        print(number, end=" ")
print()

#Nested loops using strings

words = ["Python", "Code"]

for word in words:  #prints only the words
    for character in word:    #prints all the chatraters(letters)
        print(character, end = " ")
print()


#Co-ordinate system using nested loops

for x in range(3):
    for y in range(3):
        print("Co-ordinates:", x, y)


#Using break in nested loops

for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(i, j)


# 9. Continue in a Nested Loop

for i in range(3):
    for j in range(5):
        if j == 2:
            continue

        print(i, j)


#Multiplication table grid


for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")

    print()
