def selection_sort(alist):
    for last_pos in range(len(alist)-1, 0, -1):
        pos_max = 0
        for i in range(1, last_pos+1):
            if alist[i] > alist[pos_max]:
                pos_max = i

        alist[last_pos], alist[pos_max] = alist[pos_max], alist[last_pos]

    return alist


print(selection_sort([54, 24, 26, 17, 34, 6, 78, 98, 23, 12, 53]))


# Selection sort offers O(n^2) complexity for all best, average & worst case.
# Though it is better in benchmark studies as it does far less exchange than that of bubble sort
