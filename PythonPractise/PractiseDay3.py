# variable names should start with A-Z, a-z
name = "Amrith"
print(name)
print(type(name))

# variable name shouldn't star with integers
# 123 = "Numeric" --> SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

# variable name should not be any keyword
# keyword ? // Reserved word
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' [2]
# and = 123

# variable name should not be any special character except underscore(_)
# @ = 123
# $ = 344
_ = 123
_name = "Program"
print(_name)
# $program = "Python"  --> SyntaxError: invalid syntax
# greeting$ = "Hello"

# variable name should not be any space
# first name = "Pramod" --> SyntaxError: invalid syntax
first_name = "Shukla"
print(first_name)
# Python love the snake case
variable_name = "Pychas"
long_var_name_is_created_here = "Hello"