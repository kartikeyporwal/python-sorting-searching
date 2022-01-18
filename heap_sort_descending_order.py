"Heap Sort in Descending Order implementation using max-heap"

import heapq

array_to_sort = [54, 14, 549, 365, 74, 4, 25, 34]

# initialise an empty array that will contain the sorted data in descending order
sorted_array = []

# create an array with negated elements to be used to convert min-heap to max-heap
array_to_sort = [-el for el in array_to_sort]

# heapify the array, this is min-heap but will act as the max heap becaused of the negation
heapq.heapify(array_to_sort)

# process until there is no element left in the array to be sorted
while array_to_sort:
    largest_element = -1 * heapq.heappop(array_to_sort)
    sorted_array.append(largest_element)

# print the sorted array
# Output [549, 365, 74, 54, 34, 25, 14, 4]
print(sorted_array)
