import re

num = int(input())
li = []
for i in range(1, num + 1):
    if re.search(r'\w*a\w*n\w*t\w*o\w*n\w*', input()):
        print(i, end=' ')
