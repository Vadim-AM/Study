for i in range(int(input())):
    s, virus, x = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
            if x == 5:
                print(i + 1, end=' ')
                break
