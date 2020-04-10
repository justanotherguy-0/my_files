def sumpymd(pyramid):
    pyramid=pyramid.splitlines()
    a=[[int (y) for y in x.split()]  for x in pyramid]
    v=[a[0][0] + a[1][0],a[0][0] + a[1][1]]
    for rank in range(2,len(a)):
        d=[]
        for e in range(len(a[rank])):
            if not e:
                d.append(a[rank][e] + v[0])
            elif e== len(a[rank]) -1:
                d.append(a[rank][e] + v[-1])
            else:
                d.append(a[rank][e] + max(v[e],v[e-1]))
        v=list(d)
    return max(v)
