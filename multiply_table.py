a, b, c, d = int(input()), int(input()), int(input()), int(input())
for _ in range(c, d + 1):
    print('\t', '\t', _, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for k in range(c, d + 1):
        print('\t', k * i, end='\t')
    print()