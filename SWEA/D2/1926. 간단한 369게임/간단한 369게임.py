a = int(input())

for i in range(1, a + 1):
    b = str(i)
    
    c = b.count('3') + b.count('6') + b.count('9')
    
    if c > 0:
        print('-' * c, end = ' ')
    else:
        print(i, end = ' ')