import sys
sys.stdin=open("test.txt","r")
a=[0]
b=set([0])
for line in sys.stdin.readlines()[:-1:]:
    n=int(line)
    if n > len(a)-1:
        for i in xrange(len(a),n+1):
            ai=a[i-1]-i
            if ai >0 and ai not in b:
                b.add(ai)
                a.append(ai)
            else:
                temp=a[i-1]+i
                b.add(temp)
                a.append(temp)
        print a[n]
            
    else:
        print a[n]
#print a