



def contains_duplicate(self,nums):


    seen = set()


    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
