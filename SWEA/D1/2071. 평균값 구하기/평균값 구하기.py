a = int(input())

for i in range(1, a + 1):
    b = list(map(int, input().split()))
    sum = 0
    avg = 0
    
    for j in range(10):
        sum += b[j]
    
    avg = round((sum / 10))
    print(f"#{i} {avg}")