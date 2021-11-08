



def two_sum(nums,target):


    seen = {}


    for i,num in enumerate(nums):
        value = target - num
        if value in seen:
            return [seen[value],i]

        seen[num] = i





