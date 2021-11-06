


def rotate(nums,k):


    

    
    new_array = nums[::]


    for i in range(len(nums)):
        nums[i] = new_array[(i - k) % len(nums)]
    



def reverse(a,low,high):


    while low < high:
        a[low],a[high] = a[high],a[low]
        low += 1
        high -= 1
    
def rotate_2(a,k):



    a.reverse()



    reverse(a,0,k -1)
    reverse(a,k,len(a) - 1)






#[7,6,5,4,3,2,1]


if __name__ == "__main__":


    nums = [1,2,3,4,5,6,7]
    k = 3

    print(nums)
    rotate_2(nums,k)
    print(nums)
