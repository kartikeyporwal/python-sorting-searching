# In bubble sort lots of unnecessary exchange is done, this can be avoided if
# we could modify the bubble sort to stop early if it finds that the list is sorted
# This approach is called short bubble

def short_bubble_sort(alist):
    passes = len(alist)-1
    exchange = True
    while passes > 0 and exchange:
        exchange = False
        for i in range(passes):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        passes -= 1

    return alist

print(short_bubble_sort([12,1,3,45,89,54,3,24,67,32,67,23]))
