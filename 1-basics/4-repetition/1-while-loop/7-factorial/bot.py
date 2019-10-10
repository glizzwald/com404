print("Please enter a number")
user_number = int(input())
factorial = 1

while (user_number > 0):
    factorial = factorial * user_number
    user_number = user_number - 1

print (factorial)
