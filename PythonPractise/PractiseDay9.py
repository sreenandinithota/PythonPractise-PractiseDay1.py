# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(),input(), type(), format(), max, min, id(), sum(), avg()

# Strings
name = "Joseph"  # 0 to 5
# 0,1,2,3,4,5
# J,o,s,e,p,h
print(name)
print(type(name))
print(id(name))  # id -> memory address where it is stored 4309895152
print(len(name))
# length of string ( 1 )

name = name.upper()
print(name)
name = name.lower()
print(name)
a = name.count('A')
print(a)
#  print(name[4]) # string index out of range

# Python - Immutable - that can't be changed
name[0] = "P"  # 'str' object does not support item assignment
x = 'lime'
x[2] = 't'
print(x)
