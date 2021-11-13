



def sudoku_helper(board,empty_spots,empty_spots_index):



    if empty_spots_index == len(empty_spots):
        return True


    row,col = empty_spots
    for number in range(1,10):
        board[row][col] = number
        sudoku_helper(board,empty_spots,empty_spots_index + 1)
        board[row][col] = '.'


    return False





def verify_sudoku(board):



    

    for i in range(9):
        seen = set()
        for value in board[i]:
            if value != '.':
                if value in seen:
                    return False
                seen.add(value)
        seen = set()
        for col in range(9):
            if board[col][i] != '.':
                if board[col][i] in seen:
                    return False
                
                seen.add(board[col][i])



    

    for box_row in range(0,9,3):
        for box_col in range(0,9,3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    value = board[i][j]
                    if value != '.':
                        if value in seen:
                            return False
                        seen.add(value)



    return True

    


    

        





