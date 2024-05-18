a = int(input())
b = list(map(int, input().split()))

b.sort()
p = 0

for i in range(1, a + 1):
    p += sum(b[0:i])
print(p)