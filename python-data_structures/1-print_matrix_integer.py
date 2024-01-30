def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                # Print the last number in the row with a new line
                print("{:d}".format(num))
            else:
                # Print the number followed by a space
                print("{:d}".format(num), end=" ")
        if not row:
            # Print a new line for an empty row
            print()
