def rec_pos_sum(a,b):
	'''takes the input and returns the corresponding summation'''
	
	return a*b*(a+1)*(b+1)/4
def closest_rec_pos_sum(n):
    #returns the tuple whith the rectangle dimmensions whose summation is the closest to the input
	i=1 
	ii=1
	d=n   
	while i*(i+1)/2 <=n:
		ii=1
		while ii<=i:
			da=rec_pos_sum(i,ii) - n
        	if abs(da) < abs(d):
        	    d=da
                a=i
                b=ii
        	if da>0:
        	    break
        	ii+=1
        i+=1
	return (int(n+d),a,b)    
print(closest_rec_pos_sum(2000000))
