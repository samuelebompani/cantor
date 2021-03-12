import math

def cantor(x,y):
    if (x >= 0 and y >= 0):
        return round((x+y)*(x+y+1)/2+y+1)
    return -1

def gamma(n):
    if n>=0:
        return math.floor((-1 + math.sqrt(8*n-7))/2)
    return -1

def dx(n):
    if(n >= 0):
        return n - cantor(gamma(n),0)

def sx(n):
    if(n >= 0):
        return gamma(n) - dx(n)
    return -1

def reverse(n):
    if(n < 0):
        return -1
    g = gamma(n)
    d = math.floor(n - cantor(g, 0))
    return (g - d, d)

def cantorZero(x,y):
    return cantor(x,y)-1

def reverseZero(n):
    return reverse(n+1)