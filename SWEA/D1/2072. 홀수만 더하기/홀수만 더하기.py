a = int(input())

for i in range(1, a + 1):
    b = list(map(int, input().split()))
    sum = 0

    for j in range(10):
        if b[j] % 2 == 1:
            sum += b[j]
    
    print(f"#{i} {sum}")