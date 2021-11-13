


def remove_duplicates_sorted_array(a):


    
    end = len(a)


    i = 0

    

    while i < end:
        number = a[i]

        j = i + 1


        while j < end and a[j] == number:
            a[end -1],a[j] = a[j],a[end -1]
            end -= 1












