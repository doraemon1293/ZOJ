import sys

#sys.stdin=open("test.txt","r")
n=int( sys.stdin.readline() )
words=set()
for i in range(n):
    words.add( sys.stdin.readline().strip() )
k=int( sys.stdin.readline() )
for i in range(k):
    s=sys.stdin.readline().strip().split()
    ans=0
    for x in s[1::]:
        if x in words:
            ans+=1
    print ans
