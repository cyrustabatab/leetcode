



def dissapeared_numbers(nums):

    for num in nums:

        num = abs(num)

        if nums[len(nums) - num] > 0:
            nums[len(nums) - num] *= -1 


    
    result = []
    for i,num in enumerate(nums):

        if num > 0:
            result.append(len(nums) - i)

    return result












