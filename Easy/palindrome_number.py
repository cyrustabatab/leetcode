

def palindrome_2(x):



    if x < 0:
        return False
        
    original = x
    digits = math.floor(math.log(x))

    
    new_number = 0

    while x:
        d = x % 10


        new_number += d * 10**digits

        digits -= 1

        x //= 10


    return x == original




def palindrome(x):

    x = str(x)
    return x[::-1] == x
