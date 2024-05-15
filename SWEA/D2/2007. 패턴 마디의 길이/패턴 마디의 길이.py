a = int(input())

for i in range(1, a + 1):
    b = input()
    
    for j in range(1, 11):
        if b[0 : j] == b[j : 2 * j]:
            print(f"#{i} {j}")
            break