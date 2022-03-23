import cantor
import integerList
import random

def decode_instruction(i):
    if(i%3 == 0):
        tmp = int(i/3)
        return "R_"+str(tmp)+" = R_"+str(tmp)+" + 1"
    elif(i%3 == 1):
        tmp = int(i/3)
        return "R_"+str(tmp)+" = R_"+str(tmp)+" - 1"
    else:
        s = cantor.sx(int((i+1)/3))
        d = cantor.dx(int((i+1)/3))
        return "If R_"+str(s)+"== 0 then goto"+str(d)
    
def decode(P):
    instructions = integerList.decode(P)
    print(instructions)
    return list(map(lambda x: decode_instruction(x),instructions))

def random_program():
    return decode(random.randint(0, 1999999191919191919))