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

# Improved version with 9 decimal digits by f

def wurzel(radikand, wurzelexponent):
    decimalDigits = 9
    if wurzelexponent == 0:
        print("Error: not a valid exponent")
        return
    elif radikand < 0:
        print("Error: does not handle complex numbers")
        return
    border1 = 1
    border2 = radikand
    guess = 1
    if radikand >= 1:
        while True:
            if border1 - border2 <= 1:
                guess = uniform(border1, border2)
            else:
                guess = randint(border1, border2)
            guess_p = potenz(guess, wurzelexponent)
            if guess_p == radikand:
                result = guess
                return(result)
                break
            elif border2 - border1 <= 0.00000000001:
                result = round(guess, 9)
                return(result)
                break
            elif guess_p > radikand:
                border2 = guess
            elif guess_p < radikand:
                border1 = guess
            else:
                print("Error")
                break
    elif radikand < 1:
        while True:
            if border2 - border1 <= 1:
                guess = uniform(border2, border1)
            else:
                guess = randint(border2, border1)
            guess_p = potenz(guess, wurzelexponent)
            if guess_p == radikand:
                result = guess
                return(result)
                break
            elif border1 - border2 <= 0.0000000001:
                result = round(guess, 9)
                return(result)
                break
            elif guess_p > radikand:
                border1 = guess
            elif guess_p < radikand:
                border2 = guess
            else:
                print("Error")
                break

# Test Values

#basis = randint(0, 10)
#exponent = randint(-5, 5)

radikand = 999999 #randint(0, 100)
wurzelexponent = 4 #randint(0,5)

    
print(radikand, wurzelexponent)
print(wurzel(radikand, wurzelexponent))