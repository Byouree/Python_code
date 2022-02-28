from cmath import *
def polysum(n,s):    
    area = (0.25*n*s**2)/tan(pi/n)    
    perimeter = n*s    
    sum = area + (perimeter**2)    
    sum = round(sum.real,4) + round(sum.imag, 4)        
    return sum    
