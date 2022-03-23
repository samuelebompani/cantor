import cantor
import integerList

def decode_instruction(i):
    if(i%3 == 0):
        tmp = int(i/3)
        print("R_"+str(tmp)," = R_"+str(tmp)," + 1\n")
    elif(i%3 == 1):
        tmp = int(i/3)
        print("R_"+str(tmp)," = R_"+str(tmp)," - 1\n")
    else:
        s = cantor.sx(int((i+1)/3))
        d = cantor.dx(int((i+1)/3))
        print("If R_"+str(s),"== 0 then goto",d)
    
def decode(P):
    instructions = integerList.decode(P)
    print(instructions)
    return list(map(lambda x: decode_instruction(x),instructions))

decode(1756262107)