a = int(input())

for i in range(1, a + 1):
    b = list(map(int, input().split()))
    max_num = 0
    
    for j in range(10):
        if b[j] > max_num:
            max_num = b[j]
    
    print(f"#{i} {max_num}")