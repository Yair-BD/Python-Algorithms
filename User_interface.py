from numpy.random import randint

def get_k_array_from_user():
    while True:
        try:
            n = int(input("Hey user please enter the len of the array you would like to use "))
            k = int(input("And the number of smallest num to get from the array "))
        
            if "y" == input("Enter 'y' to fell the array or 'n' to get ready one: "):
                array = [None] * n
                for i in range(n):
                    array[i] = int(input().strip())
            else:
                array = list(randint(999, size=n))
        except :
            print("Plese enter ONLY Valid NUMBERS, no char or negative digits\n")
            
        else :        
            print(f"Your array is: {array}, and your k smallest numbers is: {k}\n")
            break
    
    return array, array.copy(), k
    
