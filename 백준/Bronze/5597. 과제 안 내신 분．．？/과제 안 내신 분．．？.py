temp = []

for i in range(1, 31):
    temp.append(i)

for i in range(1, 29):
    a = int(input())
    temp.remove(a)

print(min(temp))
print(max(temp))
