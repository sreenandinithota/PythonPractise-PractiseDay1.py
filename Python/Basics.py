print("Welcome to python Learning")

a = 50
b = 70
add1 = (a+b)
print(add1)

add2 = (add1 + a + b)
print(add2)

print("Add sum of two values")
print("divide sum of two value")

userInput = input("Enter the withdraw amount")
cash = int(userInput)
accountBalance = 70000
checkBalance = accountBalance-cash

# Normal format
# print('Take your cash', cash,',balance in your account is', checkBalance)

# format() i.e, placeholder {}
print('Take your cash {}, balance in your account is {}'.format(cash, checkBalance))