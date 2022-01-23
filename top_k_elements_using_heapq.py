"Retrieve the top-k elements from an array using heapq data structure"

import heapq

element_array = [45, 22, 97, 74, 34, 12, 79, 384, 12, 3, 94]
# element_array = [45, 25, 14, 65]

heap_array = []
k = 3

for element in element_array:
    if len(heap_array) < k:
        heapq.heappush(heap_array, element)
    else:
        if element > heap_array[0]:
            heapq.heapreplace(heap_array, element)

print(heap_array)