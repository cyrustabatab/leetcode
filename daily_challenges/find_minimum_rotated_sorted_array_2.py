



def find_minimum_rotated_sorted_array(nums):





    low,high = 0,len(nums) - 1


    while low <= high:
        mid = (low + high)//2

        if a[mid] > a[mid -1] and a[mid]:

