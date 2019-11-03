def item_from_suitcase(item):
    if (item==("toothbrush")):
        print("A toothbrush! Well, got to have clean teeth.")
    elif(item==("spidey suit")):
        print("My Spidey suit! I won't be needing this. I am on holiday.")
    else:
        print("An unexpected item! It could be useful.")

print("I wonder what is in my suitcase...")
item = input()

item_from_suitcase(item)
