



def merge_sorted_array(nums1,m,nums2,n):






    first = second = 0 






    while first != m + n:

        if nums1[first] > nums2[second]:
            nums1[first],nums2[second] = nums2[second],nums1[first]

        first += 1






if __name__ == "__main__":    

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]


    print(nums1)
    merge_sorted_array(nums1,6,nums2,3)
    print(nums1)
