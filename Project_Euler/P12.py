def trg_div_n(n):
    d=1
    even_m=min(n+1,n,key=lambda x: x%2)/2
    odd_m=max(n+1,n,key=lambda x: x%2)
    p=2
    cd=1
    while even_m>1  or odd_m>1:
        cd=1
        if even_m<p**2 and even_m>1:
            
            while not odd_m % even_m:
                odd_m/=even_m
                cd+=1
            

            cd+=1
            even_m=1
            d*=cd
            p+=1
            continue          
        if odd_m<p**2 and odd_m>1:
            
            while not even_m % odd_m:
                even_m/=odd_m
                cd+=1
            
            cd+=1
            odd_m=1
            d*=cd
            p+=1
            continue
        while not even_m % p:
            even_m/=p
            cd+=1
            
        while not odd_m % p:
            odd_m/=p
            cd+=1
            
        d*=cd    
        p+=1
    return(d)
 
i=1
while True:
    if trg_div_n(i)>500:
        print(i*(i+1)/2, i)
        break
    i+=1
