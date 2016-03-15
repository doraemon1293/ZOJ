import sys
import string
sys.stdin=open("test.txt","r")
n=int( sys.stdin.readline() )
for i in range(n):
    s=sys.stdin.readline().strip()
    print s.translate(None,string.digits)
