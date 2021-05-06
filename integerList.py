import cantor as c

def encode(l):
    k=0
    l.reverse()
    for i in l:
        k = c.cantor(i, k)
    return k

def decode(n):
    k=list()
    while(n!=0):
        s, d = c.reverse(n)
        k.append(s)
        n=d
    return k

def length(n):
    if n==0:
        return 0
    return 1+length(c.dx(n))

def projection(t, n):
    if(t == 0 or t > length(n)):
        return -1
    for _ in range(t):
        u, n = c.reverse(n)
    return u

def increase(t, n):
    if(t == 0 or t > length(n)):
        return -1
    k=list()
    for _ in range(t-1):
        s, n = c.reverse(n)
        k.append(s)
    s, n = c.reverse(n)
    k.append(s+1)
    k.reverse()
    for i in k:
        n = c.cantor(i,n)
    return n

def decrease(t, n):
    if(t == 0 or t > length(n)):
        return -1
    k=list()
    for _ in range(t-1):
        s, n = c.reverse(n)
        k.append(s)
    s, n = c.reverse(n)
    k.append(s-1)
    k.reverse()
    for i in k:
        n = c.cantor(i,n)
    return n
