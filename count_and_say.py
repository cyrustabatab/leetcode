



def count_and_say(n):


    if n == 1:
        return "1"

    

    s = count_and_say(n -1)


    i = 0

    c = s[0]

    count = 1

    string = []
    while i < len(s):
        count = 1
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1
        
        
        string.append(f"{count}{s[i]}")
        i =j

    return ''.join(string)



print(count_and_say(4))



