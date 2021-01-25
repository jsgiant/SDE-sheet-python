# Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and 
# one number occurs twice in the array. Find these two numbers.

def getTwoElements( arr, size):
    for i in range(size):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            repeating_element = abs(arr[i])
             
    for i in range(size):
        if arr[i]>0:
            missing_element =  i + 1

    return (repeating_element,missing_element)
 
