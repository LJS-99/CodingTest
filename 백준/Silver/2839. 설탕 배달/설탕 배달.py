a = int(input())

if a % 5 == 0:
    print(a // 5)

else:
    p = 0
    while a > 0:
        a -= 3
        p += 1
        if a % 5 == 0:
            p += a // 5
            print(p)
            break
        elif a == 1 or a == 2:
            print(-1)
            break
        elif a == 0:
            print(p)
            break