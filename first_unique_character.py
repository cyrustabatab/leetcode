from collections import Counter


def first_unique_character(s):

    
    
    counts = Counter()


    for character in s:
        counts[character] += 1


    for i,character in enumerate(s):
        if counts[character] == 1:
            return character 


    return -1




