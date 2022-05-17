from User_interface import *
from Heap_funcs import *
from Quick_func import *


def main():
    array_quick, arrayֹ_heap, k = get_k_array_from_user()
    
    key = k_smallest(array_quick, 0, len(array_quick) - 1, k)
    array_k = array_quick[0: key]
    quick_sort(array_k, 0, len(array_k)-1)
    
    
    build_min_heap(arrayֹ_heap)
    
    
    print(f"The amazing k smallest numbers after quick sort:{array_k} \nThe number of comparisons is: {Settings.quick_comparisons}\n\n\n")
    
    
    print(f"The amazing k smallest numbers from the heap:{get_k_smallest(k,arrayֹ_heap)} \nThe number of comparisons is: {Settings.heap_comparisons}")

if __name__ == '__main__': 
    Settings.globals()# Instead passing and return from the number of comparisons, the variable is global.
    main()
        
    
    
