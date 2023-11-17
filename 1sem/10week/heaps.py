# heaps для бинарных куч (заданы массивом)
# 1
def list_is_min_heap(array: list) -> int:
    if array[0] != min(array):
        return 0
    for i in range((len(array) - 1) // 2):
        if array[i] > array[2 * i + 1] or array[i] > array[2 * i + 2]:
            return 0
    return 1


lst = list(map(int, '3 5 3 6 6 4 3 7 8 8 8 5 6'.split()))
print(list_is_min_heap(lst))


# 6
def minify(max_heap, i):
    n = len(max_heap)
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and max_heap[i] > max_heap[l]:
        smallest = l

    if r < n and max_heap[smallest] > max_heap[r]:
        smallest = r

    if smallest != i:
        max_heap[i], max_heap[smallest] = max_heap[smallest], max_heap[i]
        minify(max_heap, smallest)


def makemin(max_heap):
    n = len(max_heap) // 2 - 1
    for i in range(n, -1, -1):
        minify(max_heap, i)


heap = [3, 9, 2, 1, 4, 5]
makemin(heap)
print(heap)
