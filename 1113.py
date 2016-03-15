def fac(n):
    ans=1
    for i in range(n+1):
        if i!=0:ans*=i
    return ans

print "n e"
print "- -----------"
for n in range(10):
    e=0
    for i in range(n+1):  
        e+=1.0/fac(i)
    

    if n==0 or n==1:
        print n,"%.0f" %e
    elif n==2:
        print n,"%.1f" %e
    else:
        print n,"%.9f" %e