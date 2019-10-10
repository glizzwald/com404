print("What phrase do you see?")
phrase = str(input())
reverse = ""
print("Reversing...")
for position in range (len(phrase)-1,-1,-1):
    letter = phrase[position]
    reverse = reverse + letter

print(reverse)

