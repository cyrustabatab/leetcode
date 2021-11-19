


def search(row,col,m,n):


    if row == m and col == n:
        return 0


    
    ways = 0


    for n_row,n_col in ((row,col + 1),(row + 1,col)):
        if n_row < m and col < n:
            ways += search(n_row,n_col,m,n)


    return ways




def unique_paths(m,n):



    row = col = 0



    return search(row,col,m,n)











