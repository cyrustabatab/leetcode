import pdb



def oranges(grid):


    num_oranges = 0 
    rotten_oranges = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            value = grid[row][col]
            if value in (1,2):
                if value == 2:
                    rotten_oranges.add((row,col))
                num_oranges +=1 

    
    
    number_fresh = num_oranges- len(rotten_oranges)

    
    oranges_converted = 0
    
    minutes = 0
    added = True
    while added:
        added = False
        for row,col in rotten_oranges.copy():
            neighbors = ((row + 1,col),(row - 1,col),(row,col - 1),(row,col + 1))

            for nr,nc in neighbors:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    rotten_oranges.add((nr,nc))
                    grid[nr][nc] = 2
                    oranges_converted += 1
                    added = True



            rotten_oranges.remove((row,col))

    
        if added:
            minutes += 1
    
    if oranges_converted == number_fresh:
        return minutes
    else:
        return -1
    

if __name__ == "__main__":


    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print(oranges(grid))


