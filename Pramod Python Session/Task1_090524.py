# Task1: Take user input(name, age, roll_number, mobile_number) and print the user details
# Task2: Print the table of 2 by using the command print()

# Task1
user_name = input('Enter your name')
user_age = input('Enter your age')
user_rollNo = input('Enter your rollNo')
user_mobileNo = input('Enter your mobileNo')
print(f"UserDetails- Name: {user_name}, age: {user_age}, rollNo: {user_rollNo}, mobileNo: {user_mobileNo}")

# Task2

table = int(input('Enter Math table number'))
for i in range(1, 11):
    print(table, '*',  i, '=', table * i)




