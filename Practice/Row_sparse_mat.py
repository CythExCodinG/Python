# Function to get row-wise representation of sparse matrix
def sparse_matrix_representation(matrix):
    sparse_representation = []
    rows = len(matrix)
    columns = len(matrix[0])


    # Traverse the matrix row by row
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != 0:  # Only store non-zero elements
                sparse_representation.append((i, j, matrix[i][j]))

    return sparse_representation

# Sample 3x3 matrix with mostly zero values

matrix = [
    [0, 0, 3],
    [0, 5, 0],
    [6, 0, 0]
]


# Get the sparse matrix representation
sparse_rep = sparse_matrix_representation(matrix)

# Print the sparse matrix representation
print("Row-wise Sparse Matrix Representation (row, column, value):")
for element in sparse_rep:
    print(element)
