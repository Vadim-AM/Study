n, m = [int(i) for i in input().split()]
result_matrix = [[0] * m for _ in range(n)]
matrix_one = [[int(_) for _ in input().split()] for _ in range(n)]
input()
matrix_two = [[int(_) for _ in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        result_matrix[i][j] = matrix_one[i][j] + matrix_two[j][i]

for i in result_matrix:
    print(*i)