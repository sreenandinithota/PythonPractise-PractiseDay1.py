# Find age of the person by asking birth year
from datetime import date

# print(date.today().year)

userInput = int(input("Enter your birth year"))

currentYear = date.today().year

print("Your current age as per 2024:", currentYear - userInput)
