# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

def findTheDuplicate(nums):
    nums_len = len(nums)
    if nums_len > 1:
        # Find the intersection point of the two runners.
        slow = nums[0]
        fast = nums[nums[0]]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    return -1

# Input: nums = [1,3,4,2,2]
# Output: 2
    
    
        
