




def search(nums,target):



    low,high = 0,len(nums) - 1


    while low <= high:
        mid = (low + high)//2


        if a[mid] == target:
            return mid


        if target < a[mid]:
            high = mid - 1
        else:
            low = mid + 1


    return -1
