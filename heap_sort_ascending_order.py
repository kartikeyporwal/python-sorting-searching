import heapq

array_to_sort = [54, 14, 549, 365, 74, 4, 25, 34]

# initialise an empty array that will contain the sorted data in ascending order
sorted_array = []

# heapify the array
heapq.heapify(array_to_sort)

# process until there is no element left in the array to be sorted
while array_to_sort:
    smallest_element = heapq.heappop(array_to_sort)
    sorted_array.append(smallest_element)

# print the sorted array
# Output [4, 14, 25, 34, 54, 74, 365, 549]
print(sorted_array)

