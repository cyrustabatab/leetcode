



def num_valid_words(words,puzzles):

    
    first_letters = set(puzzle[0] for puzzle in puzzles)

    words = [word for word in words if word[0] in first_letters]
    

    valid_words = []
    for puzzle in puzzles:
        letters = set(puzzle)
        num_words = 0
        for word in words:
            for i in range(1,len(word)):
                letter = word[i]
                if letter not in letters:
                    break
            else:
                num_words += 1
        valid_words.append(num_words) 


    return valid_words
