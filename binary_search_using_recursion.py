def binary_search_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binary_search_recursion(alist[:mid], item)
            else:
                return binary_search_recursion(alist[mid+1:], item)
    

print(binary_search_recursion([1,2,3,4,5,6,7,8,9], 25))


# Usually binary search provide the worst case ccomplexity in logarithmic
# but slicing ooperation have its own complexity of O(k), so its complexity
# is not purely logarithmic in nature.
