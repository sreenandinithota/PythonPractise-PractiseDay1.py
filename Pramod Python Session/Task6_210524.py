
# Explain the difference between the = operator and the == operator in Python.
# = --> Assignment operator [doesn't return value, assign the value]
# a = 10
# b = 10
# == --> Comparison operator [return value in boolean]
# result = (a == b)
# print(result)

# -----------------------------------------------------------------
# What does the ** operator do in Python, and how is it used?
# ** --> Power operator
# a = 2**4
# b = 9**9
# print(a, b, sep='$', end='!')
# -----------------------------------------------------------------
# What does the ^ operator do in Python, and in what context is it commonly used?
# ^ --> Bitwise XOR operator
# x = False
# y = False
# print(x ^ y)
# -----------------------------------------------------------------
# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
# import math
# radius = float(input("Enter the radius"))
# print(math.pi)
# area = math.pi*pow(radius, 2)
# print(area)
# -----------------------------------------------------------------
# Develop a Python script that calculates the square and cube of a given number.
# import math
# user = float(input("Enter the number"))
# square = user**2
# square1 = math.pow(user, 2)
# print(square)
# print(square1)
# cube = user**3
# cube1 = math.pow(user, 3)
# print(cube)
# print(cube1)





# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
# pie = 3.14
# r = float(input("Enter radius if circle "))
# area_of_circle = pie*r*r
# print(area_of_circle)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

# x = int(input("Enter the first number"))
# y = int(input("Enter the second number"))
# print("x and y both are equal", x == y)
# print("x is greater than b", x > y)
# print("x is less than b", x < y)

# Develop a Python script that calculates the square and cube of a given number.

# user = int(input("Enter the number"))
# x_square = 2
# y_cube = 3
# print("Square of given number:", user ** x_square)
# print("Cube of given number:", user ** y_cube)
# ----------------------------------------------------


# print("Hello", "World", sep="-", end="!", file=file, flush=True)

# print("Hello", "World", "MKT", sep="8", end="@")
# my_string = "This is Pramod!"
# print(len(my_string))
# print(my_string[15:2:-2])
# print(my_string[0:7:3])