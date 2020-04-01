import math
def rec_pos_sum(a,b):
    '''takes the input and returns the corresponding summation'''
    return a*b*(a+1)*(b+1)/4
def closest_rec_pos_sum(n):
    #returns the tuple whith the rectangle dimmensions whose summation is the closest to the input
    i=0 
    d=n
    a=1
    b=1
    while i*(i+1)/2 <n and d:
        i+=1
        #applying the quadratic formula
        n1= math.floor((( (i**2 + i)**2 + (i**2 + i)*16*n)**(1/2) - i**2 -i )/(2*(i**2 + i)))
        da=min(((rec_pos_sum(i,n1)-n,n1),(rec_pos_sum(i,n1+1)-n,n1+1)), key= lambda x:abs(x[0]))
        if abs(da[0]) < abs(d):
            d= da[0]
            a=da[1]
            b= i
            
    return (int(n+d),a,b)    
print(closest_rec_pos_sum(2000000))
