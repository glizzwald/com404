print("Enter a word")
word = input()
print("Enter a method: 1, 2, 3 or 4 ")
method = input()

def under():
    print(word)
    print("*****")

def over():
    print("*****")
    print(word)

def both():
    print("*****")
    print(word)
    print("*****")

def grid():
    print("*****")
    print(word)
    print("*****")

if(method == "1"):
    under()
elif(method == "2"):
    over()
elif(method == "3"):
    both()
elif(method == "4"):
    print("What is the size of the grid")
    gridsize = int(input())
    while(gridsize>0):
        grid()
        gridsize = gridsize - 1


