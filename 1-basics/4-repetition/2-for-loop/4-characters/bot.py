print("What strange markings do you see?")
markings = input()
print("Identifying...")
num = 0
for position in range (0, len(markings), 1):
    print("index" ,int(num),":",(markings[position]))

print("Done!")