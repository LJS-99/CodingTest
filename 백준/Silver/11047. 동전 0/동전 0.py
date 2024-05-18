a, b = map(int, input().split())

coins = []

for i in range(a):
    coins.append(int(input()))
    
coins.sort(reverse = True)

answer = 0

for coin in coins:
    if b >= 0:
        answer += b //coin
        b %= coin
        if b <= 0:
            break
        
print(answer)