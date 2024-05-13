import statistics

a = int(input())
b = list(map(int, input().split()))

c = statistics.median(sorted(b))

print(c)