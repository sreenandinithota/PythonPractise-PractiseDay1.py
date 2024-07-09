# Format string

x = 10
print(x)

num = 8
print(f"The number is {num * 2}")
print(f"The number is {num * 3}")
print(f"The number is {num * 4}")
print(f"The number is {num * 5.453}")

num = 5
print(f"{num}*1 = {num}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")
print(f"{num}*9 = {num*9}")

b = 1
print(f"{b}x1={b}")
print("2x{}={},{}".format(b, b * 2, 3))
print("9 x {} = {}*{}".format(b, b*9))
# This is just use to showcase the output.