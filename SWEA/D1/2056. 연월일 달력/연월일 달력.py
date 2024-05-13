a = int(input())

for i in range(1, a + 1):
    b = input()
    
    year = b[0:4]
    month = b[4:6]
    day = b[6:]
    
    days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    fail = -1
    
    if 0 < int(month) < 13 and int(day) <= days[int(month)]:
        print(f"#{i} {year}/{month}/{day}")
    else:
        print(f"#{i} {fail}")