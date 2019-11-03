health = int(100)
print("Your health is", health,".  Escape is in progress...")

max_loop = int(5)
control_loop = int(0)
while (control_loop<max_loop):
    print("...Oh dear, who is that?")
    person = input()
    control_loop = control_loop + 1

    if(person == "Smiler's Bot"):
        print("Time to jam out of here.")
        health = health - 20

    elif(person == "Hacker"):
        health = health + 20
        print("Yay! Better follow this one!")

    else:
        print("Phew, just another emoji!")


print("Escaped! Health is", health)
