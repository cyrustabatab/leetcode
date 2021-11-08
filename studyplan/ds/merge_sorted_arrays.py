



def merge_sorted_array(nums1,m,nums2,n):







    placement_index = m + n - 1
    print(placement_index)


    first,second = m - 1,n - 1




    

    
    while placement_index >= 0:
        print(first,second)
        if second < 0 or ( first >=0 and nums1[first] >= nums2[second]):

            nums1[placement_index] = nums1[first]
            first -= 1
        else:
            nums1[placement_index] = nums2[second]
            second -= 1

        placement_index -= 1







if __name__ == "__main__":    

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]


    print(nums1)
    merge_sorted_array(nums1,3,nums2,3)
    print(nums1)
