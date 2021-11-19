



def move_zeros(nums):



    low = -1
    high = 0


    while True:

        if nums[high] != 0:
            if low > -1:
                nums[low],nums[high] = nums[high],nums[low]
                low = -1
















