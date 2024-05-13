a = int(input())

for i in range(1, a + 1):
    b = list(map(int, input().split()))
    c = 0 
    d = 0
    
    for j in range(2):
        c = b[0]
        d = b[1]
        
    if c > d:
        e = ('>')
    elif c < d:
        e = ('<')
    else:
        e = ('=')
    
    print(f"#{i} {e}")