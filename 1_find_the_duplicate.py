# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

def find_the_duplicate(arr):
    arr_len = len(arr)
    if arr_len > 1:
        # Find the intersection point of the two runners.
        slow = arr[0]
        fast = arr[arr[0]]
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]

        return slow

    return -1

# Input: nums = [1,3,4,2,2]
# Output: 2
    
    
        
