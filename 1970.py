import sys
#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines():
    s1,s2=line.split()
    j=0
    ans="No"
    for i in s2:
        if i==s1[j]:
            j+=1
            if j==len(s1):
                ans="Yes"
                break
    print ans
        
        