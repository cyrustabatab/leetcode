



def rotate_matrix(matrix):



    start_row = start_col = 0
    end_row = end_col = len(matrix) - 1


    

    n = len(matrix) - 1
    while start_row <= end_row:
        for i in range(n):
            matrix[start_row][start_col + i],matrix[start_row + i][end_col],matrix[end_row][end_col- i],matrix[end_row - i][start_col] = matrix[end_row -i][start_col],matrix[start_row][start_col + i],matrix[start_row + i][end_col],matrix[end_row][end_col -i]

        

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1


        n -= 2


def display_matrix(matrix):


    for row in matrix:
        for col in row:
            print(f"{col:<3}",end='')

        print()



matrix = [[j for j in range(i,i+5)] for i in range(1,26,5)]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

display_matrix(matrix)

rotate_matrix(matrix)
print()
display_matrix(matrix)
