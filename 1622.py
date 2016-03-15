import sys
for line in sys.stdin.readlines():
    a=[int(x) for x in line.strip().split()[1::] ]
    ans1=0
    ans2=0
    for i,v in enumerate(a):
        if i%2!=v:
            ans1+=1
    for i,v in enumerate(a):
        if i%2==v:
            ans2+=1
    print min(ans1,ans2)