


def longest_common_prefix(strs):





    

    result = []
    for letters in zip(*strs):
        for i in range(len(letters) -1):
            if letters[i] != letters[i +1]:
                break
        else:
            result.append(letters[0])
            continue
        break
        


    return ''.join(result)






if __name__ == "__main__":



    s = ['flower','flow','flight']


    longest_common_prefix(s)

