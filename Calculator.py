from random import *

#mostly the same function as before
def potenz(basis, exponent):
    result = basis
    if exponent > 0:
        for x in range(exponent - 1):
            result = result * basis
    elif exponent < 0:
        for x in range(exponent, -1):
            result = result * basis
        if exponent < 0:
            result = 1 / result
    else:
        result = 1
    return(result)

# Improved version by j

def wurzel(radikand, wurzelexponent):
    if wurzelexponent == 0:
        print("Error: not a valid exponent")
        return
    elif radikand < 0:
        print("Error: does not handle complex numbers")
        return
    border1 = 0
    border2 = 100
    guess = randint(border1, border2)
    guess_p = potenz(guess, wurzelexponent)
    while True:
        if guess_p == radikand:
            result = guess
            return(result)
            break
        elif guess_p > radikand:
            border2 = guess
        elif guess_p < radikand:
            border1 = guess
        else:
            print("Error")
            break
        guess = randint(border1, border2)
        guess_p = potenz(guess, wurzelexponent)
        if border1 - border2 == -1:
            print("Error: not int")
            break

# Test Values

#basis = randint(0, 10)
#exponent = randint(-5, 5)

radikand = 9 #randint(0, 100)
wurzelexponent = 2 #randint(0,5)

    
print(radikand, wurzelexponent)
print(wurzel(radikand, wurzelexponent))