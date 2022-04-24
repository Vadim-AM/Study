n, m = [int(_) for _ in input().split()]
matrix_one = [[int(_) for _ in input().split()] for _ in range(n)]
input()
p, d = [int(_) for _ in input().split()]
matrix_two = [[int(_) for _ in input().split()] for _ in range(p)]
result_matrix = [[0] * len(matrix_two[0]) for _ in range(n)]

for i in range(len(matrix_one)):
    for j in range(len(matrix_two[0])):
        for k in range(len(matrix_two)):
            result_matrix[i][j] += matrix_one[i][k] * matrix_two[k][j]

for i in result_matrix:
    print(*i)