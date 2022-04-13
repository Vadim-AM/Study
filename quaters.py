matrix = [[int(_) for _ in input().split()] for _ in range(int(input()))]
output_text = ['Верхняя', 'Правая', 'Нижняя', 'Левая', 'четверть:']
sum_list = [0, 0, 0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i < j and i < (len(matrix) - 1 - j):
            sum_list[0] += matrix[i][j]
        elif j > i > (len(matrix) - 1 - j):
            sum_list[1] += matrix[i][j]
        elif i > j and i > (len(matrix) - 1 - j):
            sum_list[2] += matrix[i][j]
        elif j < i < (len(matrix) - 1 - j):
            sum_list[3] += matrix[i][j]
for i in range(4):
    print(f'{output_text[i]} {output_text[4]} {sum_list[i]}')
