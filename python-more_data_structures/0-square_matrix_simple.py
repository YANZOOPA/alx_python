def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values
        squared_row = []
        
        # Iterate through each element in the row, square it, and append to the new row
        for element in row:
            squared_row.append(element ** 2)
        
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
