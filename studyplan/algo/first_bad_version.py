



def first_bad_version(self,n):



    low,high = 1,n


    while low <= high:

        mid = (low + high)//2


        if isBadVersion(mid):
            if not isBadVersion(mid -1):
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1















    
