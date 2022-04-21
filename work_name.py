from copy import deepcopy

n = int(input())
matrix_one = [[int(_) for _ in input().split()] for _ in range(n)]
matrix_two = deepcopy(matrix_one)
m = int(input())
for _ in range(1, m):
    result_matrix = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix_two[i][k] * matrix_one[k][j]
    matrix_two = deepcopy(result_matrix)
for i in matrix_two:
    print(*i)