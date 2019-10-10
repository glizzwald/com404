print("Calculating the sum of the first 100 numbers...")
number = 0
previousnumber = 0
while (number < 100):
    number = number + 1
    previousnumber = number + previousnumber
    number + previousnumber

print(previousnumber)