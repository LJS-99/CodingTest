a, b = map(int, input().split())

baskets = list(range(1, a + 1))

for i in range(b):
    c, d = map(int, input().split())
    
    baskets[c - 1 : d] = reversed(baskets[c - 1 : d])

for i in range(a):
    print(f"{baskets[i]}", end = ' ')