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
    border1 = 0
    border2 = radikand
    guess = randint(border1, border2)
    guess_p = potenz(guess, wurzelexponent)
    counter = 0
    if wurzelexponent == 0:
        return("Error: not a valid exponent")
    elif radikand < 0:
        return("Error: does not handle complex numbers")
    while True:
        if wurzelexponent < 0:
            break
        counter = counter +1
        if guess_p == radikand:
            print(f"I have guessed {counter} times")
            return(guess)
        elif guess_p > radikand:
            border2 = guess
        elif guess_p < radikand:
            border1 = guess
        guess = randint(border1, border2)
        guess_p = potenz(guess, wurzelexponent)
    while True:
        counter = counter +1
        if guess_p == radikand:
            print(f"I have guessed {counter} times")
            return(guess)
        elif guess_p > radikand:
            border1 = guess
        elif guess_p < radikand:
            border2 = guess
        guess = round(uniform(border1, border2),10)
        guess = 1 / guess
        guess_p = potenz(guess, wurzelexponent)
    
    
    """ guess = round(uniform(border1, border2),10)
    guess = 1 / guess
    guess_p = potenz(guess, wurzelexponent)
    if border1 - border2 == 0.0000000001:
        guess = round(guess, 0.0000000001)
        print(f"I have guessed {counter} times")
        return(guess) """
      
#i need to do some shit with the numbers when they are negative because being bigger is the wrong thing to check


# Test Values

#basis = randint(0, 10)
#exponent = randint(-5, 5)

radikand = 9 #randint(0, 100)
wurzelexponent = -2 #randint(0,5)

    
print(radikand, wurzelexponent)
print(wurzel(radikand, wurzelexponent))