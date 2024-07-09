pi = 3.14
print(pi)
print(type(pi))

i1 = 10
i2 = 87
i3 = i2/i1
print(i3)  # Python is very smart, it knows that 12/10 is a float
print(type(i3))

# -------------------------------------------------------------------

# strings
# it's a bunch of characters '', "", """  """

x = 'python'
print(x)

x = "pythonProgramming"
print(x)

z = """python is an 
interpreted programming language.
It's a simple english language which 
every one can understand."""
print(z)
print(type(z))

# Raw String
raw_str = r'C:\pythonexam\ex'
print(raw_str)
print(type(raw_str))

# Format of the String

first_name = "Python"
last_name = "Programming"
print(first_name + " " + last_name)
print(first_name, last_name)

# f -> formatting - it will replace the values of the variables
# {} -> placeholders

print(f"My name is {first_name} {last_name}")
print(f"I'll be responsible for maintaining the {first_name} {last_name}")

