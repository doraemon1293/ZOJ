import sys

def f(lines):
    for a in lines:
        for b in lines:
            if a!=b and (a.startswith(b) or b.startswith(a) ):
                #print a,b
                return False
    return True
            
        
set=0
line=sys.stdin.readline()
lines=[]
while line:
    line=line.strip()
    if line=='9':
        #print lines
        set+=1
        if f(lines):
            print "Set %d is immediately decodable" %set
        else:
            print "Set %d is not immediately decodable" %set
        lines=[]
    else:
        lines.append(line)
    line=sys.stdin.readline()

    

        