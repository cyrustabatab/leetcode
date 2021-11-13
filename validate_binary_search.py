


def validate_binary_search(root):


    def validate_helper(root,minValue=float('-inf'),maxValue=float('inf')):



        if not root:
            return True


        
        if not minValue < root.value < maxValue:
            return False




        return validate_binary_search(root.left,minValue=minValue,maxValue=root.value) and validate_binary_search(root.right,minValue=root.value,maxValue=maxValue)


    
    return validate_helper(root)





