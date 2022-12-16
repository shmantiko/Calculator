import random
#basis = float(input("Basis: "))
#exponent = int(input("Exponent: "))

def potenz(basis, exponent):
    ergebnis = basis
    if exponent > 0:
        for x in range(1,exponent):
            ergebnis = ergebnis * basis
    elif exponent < 0:
        for x in range(exponent,-1):
            ergebnis = ergebnis * ergebnis
        ergebnis = 1 / ergebnis
    else:
        ergebnis = 1
    return(ergebnis)


radikand = float(input("Radikand: "))  
wurzelexponent = int(input("WurzelExponent: "))

def wurzel(radikand, wurzelexponent):
    if radikand > 0:
        grenze1 = 1
        grenze2 = radikand
        i = 1
        if radikand >= 1:
            while i == 1:
                rndmNum = random.randint(grenze1,grenze2)
                match = potenz(rndmNum, wurzelexponent)
                if match == radikand:
                    i = 2
                elif match < radikand:
                    grenze1 = rndmNum
                else:
                    grenze2 = rndmNum
        else:
            while i == 1:
                rndmNum = random.randint(grenze2,grenze1)
                match = potenz(rndmNum,wurzelexponent)
                if match == radikand:
                    i = 2
                elif match < radikand:
                    grenze2 = rndmNum
                else:
                    grenze1 = rndmNum
    elif radikand < 0:
        print("Dieses Programm kann keine Wurzel aus ne")
    else:
        match = 0
    ergebnis = rndmNum
    print(ergebnis)

wurzel(radikand, wurzelexponent)

    




#potenz(basis,exponent)