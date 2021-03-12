import math

def cantor(x,y):
    return (x+y)*(x+y+1)/2+y+1

def gamma(n):
    return math.floor((-1 + math.sqrt(8*n-7))/2)

def dx(n):
    return n - cantor(gamma(n),0)

def sx(n):
    return gamma(n) - dx(n)

def reverse(n):
    g = gamma(n)
    d = math.floor(n - cantor(g, 0))
    return (g - d, d)