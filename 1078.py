import sys

def check(n,base):
    #print base
    number=[]
    while n!=0:
        number.append(n%base)
        n=n/base
    #print number
    if number==number[::-1]:
        return True
    else:
        return False
    

lines=sys.stdin.readlines()
for line in lines:
    num=int(line.strip())
    bases=[]
    if num==0: break
    else:
        for base in range(2,17):
            if check(num,base):
                bases.append(str(base))
        if bases!=[]:
            print "Number %d is palindrom in basis " %num +' '.join(bases)
        else:
            print "Number %d is not a palindrom"%num
        