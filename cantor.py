import math

def cantor(x,y):
    if (x < 0 or y < 0):
        return -1
    return round((x + y) * (x + y + 1) / 2 + y + 1)

def gamma(n):
    if n < 0:
        return -1
    return math.floor((-1 + math.sqrt(8 * n - 7)) / 2)

def dx(n):
    if(n >= 0):
        return n - cantor(gamma(n),0)

def sx(n):
    if(n < 0):
        return -1
    return gamma(n) - dx(n)

def reverse(n):
    if(n < 0):
        return -1
    g = gamma(n)
    d = (n - cantor(g, 0))
    return (g - d, d)

def cantorZero(x,y):
    return cantor(x,y)-1

def reverseZero(n):
    return reverse(n+1)