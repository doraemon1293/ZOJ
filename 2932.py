import sys
#sys.stdin=open("test.txt","r")
d={' ':'%20','!':'%21','$':'%24','(':'%28',')':'%29','*':'%2a'}

for line in sys.stdin.readlines()[:-1:]:
    line=line.strip()
    line=line.replace('%','%25')
    #print line
    for key in d:
        line=line.replace(key,d[key])
    print line
    
        
        