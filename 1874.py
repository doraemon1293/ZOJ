import sys
lines=[x.strip() for x in sys.stdin.readlines()[:-1:]]
for line in lines:
    a=[int(x) for x in line.split()[0][::-1]]
    b=[int(x) for x in line.split()[1][::-1]]
    l=max(len(a),len(b))
    add=0
    ans=0
    for i in range(l):
        if i >= len(a):
            aa=0
        else:
            aa=a[i]
        if i >= len(b):
            bb=0
        else:
            bb=b[i]
        if aa+bb+add>=10:
            add=1
            ans+=1
        else:
            add=0
    if ans==1:
        print "%d carry operation." %ans
    elif ans>1:
        print "%d carry operations." %ans
    else:
        print "No carry operation."
            
            
            
        