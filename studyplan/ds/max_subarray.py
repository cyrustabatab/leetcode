


def max_subarray(nums):



    max_sum = float("-inf")

    current_sum = 0
    for num in nums:

        if num > current_sum + num:
            current_sum = num
        else:
            current_sum += num



        max_sum = max(max_sum,current_sum)

    
    return max_sum



