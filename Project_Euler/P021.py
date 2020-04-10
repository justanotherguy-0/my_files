def divisors (opfd):
    '''takes a list of a number's prime descomposition. Its entries
    are list in the format [_prime number_,_power_]'''
    if sum([x[0]==0 or x[0]==1 for x in opfd]): return [0]
    
    import functools
    pfd= [list(x) for x in opfd]
    ml=[]
    while True:
        for i in range(opfd[-1][1],-1,-1):
            pfd[-1][1]=i
            ml.append(functools.reduce(lambda x,y: x*y, [a[0]**a[1] for a in pfd]))  
        if sum([x[1] for x in pfd])==0: break
        for ii in range(len(pfd)-2,-1,-1):
            if pfd[ii][1]==0:
                pfd[ii][1]=opfd[ii][1]
                continue
            else:
                pfd[ii][1]-=1
                break
    return ml
def prime_descomposition(n):
    if n==1: return [[1,1]]
    if n==0: return [[0,1]]
    pdl=[]    
    if not n%2:
        cd=0
        while not n%2:
            n//=2
            cd+=1
        pdl.append([2,cd])
    for i in range(3,n+1):
        if not n%i:
            cd=0
            while not n%i:
                n//=i
                cd+=1
            pdl.append([i,cd])
    return pdl
s=0

for i in range(2,10000):
    #Substracting i for b to be sum of proper division
    b=sum(divisors(prime_descomposition(i)))- i
    if i!= b:
        if i == sum(divisors(prime_descomposition(b))) - b: s+=i
print(s)
