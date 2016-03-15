import sys
for line in sys.stdin.readlines()[:-1:]:
    line=line.strip()
    n=int( line.split(' ')[0] )
    q=line.split(' ')[1]
    s=[]
    w=[]
    leave=0
    for c in q:
        if c in s:
            s.remove(c)
        elif len(s)>=n:
            if c in w:
                w.remove(c)
                leave+=1
            else:
                w.append(c)
        else:
            s.append(c)
    if leave:
        print "%d customer(s) walked away." %leave
    else:
        print "All customers tanned successfully."

                