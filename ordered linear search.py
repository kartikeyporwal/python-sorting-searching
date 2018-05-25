#Defining a function for linear search which take an ordered list of items and a item to be searched as an input

def ordered_linear_search(alist, item):

    found = False
    position = 0
    stop = False

    while position < len(alist) and found == False and stop == False:
        if alist[position] == item:
            found = True
        else:

            #since the list is ordered, we will check the item till the point it's less than the list's item
            # [1,3,5,7,9], to search 4, we'll check till 5 and then stop, it'll reduce the best case & average case complexity from n to 1 & n/2 respectively!
            if alist[position] > item:
                stop = True
            else:
                position += 1
    return found

li = ordered_linear_search([i for i in range(200) if i%2 != 0], 96)
print(li)
        
