import cantor
import integerList as il

#cantor(x,y)
assert(cantor.cantor(0,0)==1)
assert(cantor.cantor(0,3)==10)
assert(cantor.cantor(4,0)==11)
assert(cantor.cantor(3,2)==18)
print("Ok cantor")

#gamma(n)
assert(cantor.gamma(486)==30)
assert(cantor.gamma(12)==4)
assert(cantor.gamma(1)==0)
assert(cantor.gamma(9)==3)
print("Ok gamma")

#sx(n)
assert(cantor.sx(9)==1)
assert(cantor.sx(13)==2)
assert(cantor.sx(18)==3)
assert(cantor.sx(1)==0)
print("Ok sx")

#dx(n)
assert(cantor.dx(12)==1)
assert(cantor.dx(19)==3)
assert(cantor.dx(22)==0)
assert(cantor.dx(1)==0)
print("Ok dx")

#reverse(n)
assert(cantor.reverse(10)==(0,3))
assert(cantor.reverse(13)==(2,2))
assert(cantor.reverse(8)==(2,1))
assert(cantor.reverse(23)==(5,1))
print("ok reverse")

#cantorZero
assert(cantor.cantorZero(0,0)==0)
assert(cantor.cantorZero(0,3)==9)
assert(cantor.cantorZero(4,0)==10)
assert(cantor.cantorZero(3,2)==17)
print("Ok cantor zero")

#reverse(n)
assert(cantor.reverseZero(9)==(0,3))
assert(cantor.reverseZero(12)==(2,2))
assert(cantor.reverseZero(7)==(2,1))
assert(cantor.reverseZero(22)==(5,1))
print("ok reverse zero")

#integer list
assert(il.encode([1,2,5])==18144)
assert(il.encode([0,1])==6)
assert(il.decode(18144)==[1,2,5])
assert(il.decode(100)==[5,2,0])
assert(il.projection(3,18144)==5)
assert(il.projection(2,100)==2)
print("Ok integer list encoding")