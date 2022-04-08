def pascal(n):
    string = []
    if n == 0:
        string.append(1)
        return string
    elif n == 1:
        string.append(1)
        string.append(1)
        return string
    elif n >= 2:
        for num in range(2, n + 2):
            num = ((num * (num - 1)) // 2)
            string.append(num)
        return string


print(pascal(5))
