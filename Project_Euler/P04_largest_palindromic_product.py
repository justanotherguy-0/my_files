n=999999
nn=999
def max_poldr(n):
    while n>10000:
        if n==int(str(n)[::-1]):
            nn=999
            while nn>100:
                if n/nn <=999 and n/nn>=101 and n/nn==int(n/nn):
                    print('tugfa')
                    return(nn,' times ', n//nn,' is ', n )
                    n=10000
                    break
                    
                nn-=1    
            n-=10**(int((len(str(n))-0.1)/2)+1)
            n=int(str(n)[:int((len(str(n))-0.1)/2)+1] + '9'*(len(str(n))//2))
            continue    
        n-=1              
print (max_poldr(999999))        