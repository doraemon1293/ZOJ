import sys
lines=[int(x.strip()) for x in sys.stdin.readlines()]
for n in lines[1::]:
    round=0
    arr=[True]*(n+1)
    while round<n:
        round+=1
        arr=[arr[i] if i%round else arr[i]!=True for i in range(n+1)]
    print arr[1::].count(False)
    