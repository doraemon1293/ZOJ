import sys
import math
#sys.stdin=open('test.txt','r')
for line in sys.stdin.readlines():
	n=int(line)
	frac=math.modf(n*math.log10(n))[0]
	ans=int(10**frac)
	while ans==0:
		ans*=10
	print ans