# ✅ Right Triangle Star Pattern
# n = 5
# *
# **
# ***
# ****
# *****

# triangle_input = int(input("Enter the number"))
#
# for i in range(0, triangle_input+1):
#     print('*'*i)
#     i = i+1

# --------------------------------------------------------------------------------------

# ✅ Palindrome of String
# i/p = naman , nitin, level
# o/p = true
# i/p = pramod
# o/p = false

# get_input_name = (input("Enter the name"))
# default_name = "nitin"
#
# if get_input_name == default_name:
#     print(True)
# else:
#     print(False)

# ---------------------------------------------------------------------------------------

# ✅ String Reverse
# 3-4 ways to do this in Python

# *Way1*

# string_input = (input("Enter the name"))
# x = string_input[::-1]
# print(x)

# *Way2*

#
# def reverse_string(string):
#     new_string = ""
#     for i in range(len(string)-1,-1,-1):
#         new_string += string[i]
#     return new_string()
#
#
# reverse_string("Member")

# def reverse_string_reversed(s):
#     return ''.join(reversed(s))
#
#
# print(reverse_string_reversed("saurabh"))  # Output: "hbaruas"

# *Way3*

#
# string = input("Enter name: ")
# new_list = ""
# for x in string:
#     new_list = x+new_list
# print(new_list)

# ✅ Count vowels and consonants in a String

string = "program!"
vowels = "aeiouAEIOU"

for i in vowels:
    count = sum(string.count(i))
    # count = sum(string.count(vowel) for vowel in vowels)
    print(count)