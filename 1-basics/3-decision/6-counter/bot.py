print("Please enter the first whole number.")
num1 = int(input())

print("Please enter the second whole number.")
num2 = int(input())

print("Please enter the third whole number.")
num3 = int(input())

evens = 0
odds = 0

if(num1 % 2 == 0):
    evens = evens + 1
else:
    odds = odds + 1

if(num2 % 2 == 0):
    evens = evens + 1
else:
    odds = odds + 1

if(num3 % 2 == 0):
    evens = evens + 1
else:
    odds = odds + 1

print("There were", evens, "even and", odds, "odd numbers.")


