from collections import Counter


def intersection_two_arrays(nums1,nums2):


    counts_1 = Counter(nums1)


    result = []
    for number in nums2:
        if number in counts_1:
            counts_1[number] -= 1
            result.append(number)
            

    

    return result
