from User_interface import *
from Heap_funcs import *
from Quick_func import *


def main():
    arrayֹ_heap, k = get_k_array_from_user()
    array_quick = arrayֹ_heap.copy()
    key = k_smallest(array_quick, 0, len(array_quick) - 1, k)
    print(array_quick)
    array_b = array_quick[0: key]
    print(array_b)
    quick_sort(array_b, 0, len(array_b)-1)
    print(array_b)
    # build_min_heap(arrayֹ_heap)
    # print(f"The amazing k smallest numbers:{get_k_smallest(k,arrayֹ_heap)} \nThe number of comparisons is: {Settings.comparisons}")

if __name__ == '__main__': 
    Settings.globals()# Instead passing and return from the number of comparisons, the variable is global.
    main()
        
    
    
