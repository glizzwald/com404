print ("What type of cover does the book have")
book_type = input()
if (book_type == "soft"):
    print("Is the book perfect bound?")
    perfect_bound = input()
    if (perfect_bound == "yes"):
        print("Soft cover, perfect books are very popular")
    else:
        print("Soft covers with soild or stitches are great for short books")
if (book_type == "hard"):
    print("Books with hard covers can be more expensive!")
