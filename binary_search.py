def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    
    while first <= last and not found:
        mid = (first + last)//2
        if alist[mid] == item:
            found = True
        elif item < alist[mid]:
            last = mid -1
        elif item > alist[mid]:
            first = mid + 1
    return found

print(binary_search([i for i in range(500)], 25))


#Worst case complexity of binary search is O(log n) which is far better than that of
# linear search where it was O(n). Searching can furthe rbe improved if we use Hashing
# which provid O(1).
# Binary search is optimum for large ordered list.
