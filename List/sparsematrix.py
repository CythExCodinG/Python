def sparse_full(sparse_matrix, rows, col):
    full_matrix = [[0] * col for _ in range(rows)]
    
    for r, c, v in sparse_matrix:
        full_matrix[r][c] = v
    
    return full_matrix

spar_mat = [(0, 2, 99),(2, 1, 66),(1, 2, 12)]

rows, col = 3, 3

result = sparse_full(spar_mat, rows, col)

for values in result:
    print(values)
