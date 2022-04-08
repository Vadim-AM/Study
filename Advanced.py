def pascal(n):
    string = []
    for i in range(n + 1):
        temp_string = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_string.append(1)
            else:
                temp_string.append(string[i - 1][j - 1] + string[i - 1][j])
        string.append(temp_string)
    return string


n = int(input())
for k in pascal(n - 1):
    print(*k)
