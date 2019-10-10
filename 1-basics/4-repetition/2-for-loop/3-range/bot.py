brightness_level = int(input("What level of brightness is required"))
print("Adjusting brightness...")

for count in range(2,brightness_level+2,2):
    print("Beep's brightness level:", "*"*count)
    print("Bop's brightness level:", "*"*count)

