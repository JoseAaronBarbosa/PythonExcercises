import time
import random 
import numpy as np

def insertion_sort(unsorted_array):

    for i in range(0,len(unsorted_array)):

        key = unsorted_array[i] 
        j = i-1
        while j>=0 and A[j] > key:
            unsorted_array[j+1] = unsorted_array[j]
            j = j-1
        unsorted_array[j+1] = key

    return unsorted_array

def binary_search(array, element):
    min = 0
    max = len(array)
    Searches = 1
    while True:
        index = ((min+max)//2)
        a_element = array[index]
        if a_element == element:
            print(f"Element found in index {index}")
            break
        elif a_element < element:
            min = index+1
        else:
            max = index-1
        Searches += 1
    return Searches


A = np.arange(start=1,stop=10001)

Searches = binary_search(A,2)   


print(f'Done in {Searches} searches')