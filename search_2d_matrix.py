


def search_2d(matrix,target):



    row,column = 0,len(matrix[0]) - 1


    while row < len(matrix) and column >= 0:

        if matrix[row][column] == target:
            return True



        if target < matrix[row][column]:
            column -= 1
        else:
            row += 1
    
    return False

