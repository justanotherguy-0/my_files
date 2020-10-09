import math as mh
import random as rdm
# ingresamos los puntos via teclado
lsp=list() #lista de puntos
'''
n=int(input("Cuantos puntos va a ingresar?: "))

for i in range(n):
    nwp=['',''] #newpoint
    
    nwp[0]=float(input("coordenada en x del punto" + str(i+1) + ': '))
    nwp[1]=float(input("coordenada en y del punto" + str(i+1) + ': '))
    lsp.append(nwp)
    print("\n")
'''    

def angl(dt1,dt2):
    #devuelve el angle entre dt1 y dt2 usando la ley del coseno
    a=(dt1[0]**2 + dt1[1]**2)**0.5
    b=(dt2[0]**2 + dt2[1]**2)**0.5
    c2=(dt1[0]-dt2[0])**2 + (dt1[1]-dt2[1])**2
    cosc= -(c2 - a**2-b**2)/(2*a*b)
    return mh.acos(cosc)
    
def minang(plist):
    #Take a list of coordinates as input and returns the pair of points with the smallest angle separating them
    minp=[plist[0],plist[1],angl(plist[0],plist[1])]
    for i in range(len(plist)):
        for ii in range(i+1,len(plist)):
            if angl(plist[i],plist[ii])< minp[2] : minp=[plist[i],plist[ii],angl(plist[i],plist[ii])]
    return(minp)    

#inciso c
for i in range(4):
    lsp.append([rdm.randint(-9,9),rdm.randint(-9,9)])
        
print(lsp,minang(lsp),sep='\n')
