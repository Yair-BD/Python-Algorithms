import Settings
from Settings import swap

def build_min_heap(array: list):
    for i in range(len(array)//2, -1, -1):
        min_heap(i, array)
    
    
def min_heap(father: int, array: list):
    min = father
    left = left_child(father)
    right = right_child(father)
    
    # Check the true father = who the smallest in the tree family
    # We in the array borders and the child is smaller then his father
    if left <= len(array)-1 :
        Settings.heap_comparisons += 1
        if array[left] < array[father]: 
            min = left
    
    if right <= len(array)-1: 
        Settings.heap_comparisons += 1    
        if array[right] < array[min]:
            min = right
    
    #If the min != the father we have to contiue the func 
    if father != min:
        swap(array, father, min)
        min_heap(min, array)


def heap_axtract_min(array: list):
    if len(array) > 0: # In case the user asked more k smallest number than we have and we dont want to get an index error.
        swap(array, 0, -1)

        min = array.pop() # Using pop to get and remove the first object, the min, from the list.
        min_heap(0, array)
        return min
    
def get_k_smallest(k: int, array: list):
    if len(array) < k: # In case the user asked more k smallest number than we have.
        print("The number of smallest numbers that you asked is bigger from the original size of the array\nSo there is the array :)")
        return array
    else:
        list = [None] * k #Make a list in the size of k smallest numbers
        for i in range(k):
            list[i] = heap_axtract_min(array)
        return list

# Relationships functions
def left_child(i: int):
    return 2*i + 1

def right_child(i: int):
    return 2*i + 2

