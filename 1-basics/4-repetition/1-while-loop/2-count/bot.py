cables = 0
print("How many live cables should I avoid?")

max_cables = int(input())

while (cables < max_cables):
    cables = cables + 1
    print("Avoiding...Done!", cables, "live cables avoided.")

print("All live cables have been avoided.")