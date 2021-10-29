



def count_complete_tree_nodes(root):

    start  = 1


    current = root


    while current:

        if current.right:
            current = current.right
            n = n * 2 + 1
        else:
            n *= 2



    
