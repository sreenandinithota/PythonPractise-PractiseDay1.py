# Program to find the max in two numbers
print(max(23, 13))
print(max(45, -5))
print(max(87, 998, 962))
print(max(34, 897, -183, 76.1, -0))

# TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(65, 98, 222, 698, "Maximum"))

# IndentationError: unexpected indent
#    print("Hello World")
# --------------------------------------------------------------------------------
# ✅ Dynamically typed
# Dynamic Type - Type of Data that Python supports.
age = 65
# variableName = variableValue
# identifier = literal

# Types which are supported in the Python

# Integers - Positive and negative whole numbers.
# 1, -1,123, 999, 100000, 96543210

# Floating Points Numbers
# 3.14, 5.3333333 , 18.00, 0.000786  . -0.4, -1.6
pi = 3.14

# String
# "pramod", "A", "hello world", "Hi, I am good person, You are a liar", "12345"
name = "Pramod"

# Boolean
# True, False
# true, false ? boolean?
isMale = True

# How do I check the type of the variable?
print(type(age))
print(type(name))
print(type(isMale))
print(type(pi))

# Python - Complex NUMBER - i iota -
complex_number = 2 + 3j
# Real - 2
# Imaginary - 3
print(complex_number.real)
print(complex_number.imag)

# Complex Data types in Python
# List
# Tuple
# Dictionary
# Set

person_age = 65
person_name = 'python'
# Dynamically typed
# Here we declared some variables without mentioning their data types.
# The compiler determines them at run time!!
# This is what dynamically means!
# To verify the data types of variables at run-time!
# Examples: Python, Javascript, PHP, RUBY [Dynamically typed]
# Ex: Java, C, C++ [Statically typed]
print(person_age)
print(person_age)