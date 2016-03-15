
cube=[x**3 if x >1 else 0 for x in range(202)]



for a in range(6,201):
    #sum=a**3
    for b in range(2,a):
        for c in range(b,a):
            t=cube[a]-cube[b]-cube[c]
            if t<cube[c+1]: break
            if t in cube[c+1::]:
                print "Cube = %d, Triple = (%d,%d,%d)" %(a,b,c,cube.index(t))
                    
                    
