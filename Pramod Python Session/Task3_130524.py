name = 'batman'
print(len(name))  # len will start from 1

print(name[3])  # Index will start from 0

# print(name[6])   # IndexError: string index out of range
print(len(name)-1)
print(name[len(name)-1])

# string - immutability
# that can't be changed or modified
string = 'Hello'
string = 'Sree'
# string[0] = 'F'  # TypeError: 'str' object does not support item assignment
print(string)

print(string[-1])
print(string[-5])


val = None  # 'NoneType'
# Nothing
# None is not a default value
# None is not 0.
# None is not an empty string
# None is not the same as False

print(val)
print(type(val))
"""

# Sequence --> List
# []
# Collection of items
# It can be of different data types
my_shopping_list = ["kitchen items", "cooking items", "laundry items", "Pooja items"]
print(len(my_shopping_list))



# ESCAPE SEQ

# n - \n > new line
# t - \t > tab char
# a - \a > bell
# f - \f > form feed
"""