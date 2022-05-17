def globals():
    global heap_comparisons, quick_comparisons
    heap_comparisons = quick_comparisons = 0
    
def swap(array: list, i: int, j: int):
    array[i], array[j] = array[j], array[i]
