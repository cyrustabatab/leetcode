from collections import Counter


def valid_anagrams(s,t):


    letter_counts = Counter(s)


    for character in t:
        letter_counts[character] -= 1
        if letter_counts[character] < 0:
            return False



    return all(value == 0 for value in letter_counts.values())


