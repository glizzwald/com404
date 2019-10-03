print("Where shold I look?")
location = input()
if (location == "in the bedroom"):
    bedroom = input("Where in the bedroom should I look? ")
    if (bedroom == "under the bed"):
        print("Found some shoes but no battery.")
    else:
        print("found some mess but no battery.")
if (location == "in the bathroom"):
    print("where in the bathroom should I look?")
    bathroom = input()
    if (bathroom == "in the bathtub"):
         print("found a rubber duck but no battery")
     
    else:
         print("It is wet but I found no battery.")
if (location == "in the lab"):
    print("where in the lab should I look")
    lab = input()
    if (lab == "on the table"):
        print("Yes! I found my battery")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking.")
