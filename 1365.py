import sys
lines=[s.strip() for s in sys.stdin.readlines()]
d=0
for s in lines[:-1:]:
    
    if s=="0":
        print d
        d=0
    else:
        add= int(s.split(' ')[2])
        code= s.split(' ')[3]
        if code=='F':
            add*=2
        elif code=='B':
            add=int( round(add*1.5,0) )
        elif code=='Y':
            if add<500:
                add=500
        d+=add
                
        
            