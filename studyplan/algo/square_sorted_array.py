



def square_sorted_array(nums):




    low,high = 0,len(nums) - 1

    
    result = [None] * len(nums)

    end = len(result) - 1
    while low <= high:
        if nums[low]**2 >= nums[high]**2:
            result[end] = nums[low]**2
            low += 1
        else:
            result[end] = nums[high]**2
            high -= 1

        end -= 1


    return result



if __name__ == "__main__":

    a = [-7,-3,2,3,11]

    print(square_sorted_array(a))




