print("How many numbers should I sum up?")
amount_of_numbers = int(input())
numbers = 0
previous_number = 0

while (amount_of_numbers>numbers):
    numbers = numbers + 1
    print("Please enter a number", numbers, "of", amount_of_numbers)
    user_number = int(input())
    previous_number = user_number + previous_number
    
print(previous_number)

