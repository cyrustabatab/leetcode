



def valid_parentheses():


    stack = []
    

    opening = {'(': ')','{': '}','[': ']'}

    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if not stack:
                return False

            before = stack.pop()

            if not opening[before] == c:
                return False



    return not stack



