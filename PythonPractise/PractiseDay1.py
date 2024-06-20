print("Hello World!")

print(2+2)
print(2-2)
print(2/2)
print(2*2)


# print()
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# self - Concept in OOps which points to itself - ignore.
# *args - Unlimited number of arguments * - string, int, float, boolean...
# sep=' ' - How you want to separate the arguments
# end='\n' - in the end what you want to do
# file=None - File IO

# ESCAPE SEQ
# n - \n > new line
# t - \t > tab char
# a - \a > bell
# f - \f > form feed

print("Hello","This is PythonProgram", True, 20.0, 1995)
print("Hi, My name is Python", "Program", sep=" **** ")
print("Watch the class", "with full concentration", sep=" ")
print("Have a good day!\nEnjoy your day")

# text = "hello\nworld"
# print(text)
#
# lines = text.split('\n')
# print(lines)
#
# print('\n'.join(lines))

# print(sep="-", "Hi", "Python") --> positional argument follows keyword argument

print("I am Good Person", "@Python", sep='........', end=' ~ ')
print("I am Bad Person", "@Java", sep=',,,,,,,,,,,,,', end=" ` ")
print("No one is perfect")
# Python is case sensitive
# Print("Hi") -->  NameError: name 'Print' is not defined. Did you mean: 'print'?