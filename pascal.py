


def pascal(numRows):

    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1,1]]


    all_rows = [] 

    previous_row = [1,1]

    all_rows = [previous_row]


    for _ in range(numRows):
        current_row = [1]

        for i in range(1,len(previous_row)):
            s = previous_row[i-1] + previous_row[i]
            current_row.append(s)

        current_row.append(1)

        all_rows.append(current_row)
        previous_row = current_row


    return current_row






