print("What phrase do you see?")
user_input = str(input())

print("Reversing...")
for position in range (len(user_input)-1,0,1):
    print(user_input[position])
