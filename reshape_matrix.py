


def reshape_matrix(mat,r,c):


    if r * c != len(mat) * len(mat[0]):
        return mat


    
    new_matrix = []

    current_row = current_col =0
    for row in range(r):
        new_row = []
        for col in range(c):
            new_row.append(mat[current_row][current_col])
            if current_col == len(mat[0]) - 1:
                current_row += 1
                current_col = 0
            else:
                current_col += 1

        
        new_matrix.append(new_row)
    

    return new_matrix


if __name__ == "__main__":

    mat = [[1,2,3],[3,4,5]]

    print(mat)
    r,c = 3,2

    mat = reshape_matrix(mat,r,c)

    print(mat)


