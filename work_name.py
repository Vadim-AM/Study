n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
k = 1
one, two = 0, max(n, m) - 1
squares = int((min(n, m) + 1) / 2)
for i in range(squares):
    for j in range(one, two + 1):
        matrix[i][j] = k
        k += 1
    for j in range(one + 1, two):
        matrix[j][two] = k
        k += 1
    for j in range(two - 1, one - 1, -1):
        matrix[two - 1][j] = k
        k += 1
    for j in range(two - 1, one, -1):
        matrix[j][one] = k
        k += 1
    one += 1
    two -= 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
