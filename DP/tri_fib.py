


def tri_fib(n):

    
    if n<= 1:
        return n

    if n == 2:
        return n

    first,second,third = 0,1,1




    for _ in range(n -3 + 1):
        first,second,third = second,third,first + second + third

    
    return third

