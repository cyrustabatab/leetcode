



def climbing_steps(n):



    first,second = 1,1

    if n <= 1:
        return n


    for _ in range(n -1):
        first,second = second,first +second


    return second






