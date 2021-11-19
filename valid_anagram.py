


def valid_anagram(s,t):


    counts_s = Counter(s)


    for character in t:
        if character not in counts_s:
            return False

        counts_s[character] -= 1
        if counts_s[character] == 0:
            del counts_s[character]

    return True




