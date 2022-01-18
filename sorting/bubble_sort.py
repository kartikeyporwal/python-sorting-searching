def bubble(alist):
    for passes in range(len(alist)-1, 0, -1):
        for i in range(passes):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

    return alist


print(bubble([12, 34, 24, 23, 2, 34, 1, 24, 56, 32, 45]))

# Bubble sort offers O(n^2) in worst case & average case. In best case it offers
# O(n) because no exchange is done.
