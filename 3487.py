import sys
sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines()[1::]:
    s=line.strip()
   
    if len(s)!=1 and s[-2]=="1":
        print s+"th"
    else:
        
        
        if s[-1]=="1":
            print s+"st"
        elif s[-1]=="2":
            print s+"nd"
        elif s[-1]=="3":
            print s+"rd"
        
        else:
            print s+"th"
    