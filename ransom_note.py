from collections import Counter


def ransom_note(ransomNote,magazine):



    magazine_counts = Counter(magazine)



    for character in ransomNote:
        if character not in magazine_counts:
            return False

        magazine_counts[character] -= 1
        if magazine_counts[character] == 0:
            del magazine_counts[character]


    return True



