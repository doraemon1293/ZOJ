import sys
import math
sys.stdin=open("test.txt","r")
for i in sys.stdin.readlines()[1::]:
    i=int(i)
    print int(math.floor( math.log(i,2) )+1)