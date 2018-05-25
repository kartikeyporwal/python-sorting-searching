#Defining a function for linear search which take a list of items and a item to be searched as an input

#importing shuffle from random module to shuffle list elements

from random import shuffle

def linear_search(alist, item):
    
    position = 0
    found = False
    while position < len(alist) and found == False:
        if alist[position] == item:
            found = True
        else:
            position += 1
            
    return found

a = [i for i in range(200)]
shuffle(a)

print(linear_search(a, 599))
