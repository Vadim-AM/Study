def my_matrix(string_num, width):
    zhnec = []
    for _ in range(string_num):
        zhnec.append([])
        for _ in range(width):
            zhnec[-1].append(input())
    return  zhnec

def right_matrix(this_shit, length, width):
    for i in range(length):
        for j in range(width):
            print(this_shit[i][j], end=' ')
        print()

def left_matrix(this_shit, length, width):
    for i in range(width):
        for j in range(length):
            print(this_shit[j][i], end=' ')
        print()


n = int(input())
m = int(input())
matrix = my_matrix(n, m)
right_matrix(matrix, n, m)
print()
left_matrix(matrix, n, m)