# Given an array nums with n objects colored red, white, or blue, sort them in-place so
#  that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

def sort_colors(colors):
    low,mid,high = 0,0,len(colors)-1
    while(mid < high):
        if colors[mid] == 0:
            colors[low],colors[mid] = colors[mid],colors[low]
            low +=1
            mid +=1
        elif colors[mid] == 1:
            mid +=1
        else:
            colors[high],colors[mid] = colors[mid],colors[high]
            high -=1
    return colors

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
