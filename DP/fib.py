



def fib(n):

    
    if n <= 1:
        return n
    first,second = 0,1


    for _ in range(n -2 + 1):
        first,second = second,first + second


    return second



