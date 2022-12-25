from random import *

def exponentiation(base, exponent):
    result = base
    if exponent > 0:
        for x in range(exponent -1):
            result = result * base
    elif exponent < 0:
        for x in range(exponent, -1):
            result = result * base
        result = 1 / result
    else:
        result = 1
    return(result)

def root(radicand, index, decimalDigits):
    if index == 0:
        return("Error: not a valid index")
    elif radicand < 0:
        return("Error: does not handle complex numbers")
    if index < 0:
            return("Error: does not compute negative exponents yet")
    border1 = 0
    border2 = radicand
    counter = 0
    while True:
        counter = counter + 1
        if border1 - border2 < -1:
            guess = randint(border1, border2)
        else:
            guess = uniform(border1, border2)
        guess_p = exponentiation(guess, index)
        if guess_p == radicand:
            print(f"I have guessed {counter} times")
            return(guess)
        elif border2 - border1 <= exponentiation(0.1, decimalDigits + 1):
            print(f"I have guessed {counter} times")
            return(round(guess, decimalDigits))
        elif guess_p > radicand:
            border2 = guess
        elif guess_p < radicand:
            border1 = guess
        else:
            return("Error")

# Test Values

#basis = randint(0, 10)
#exponent = randint(-5, 5)

radicand = 4 #randint(0, 100)
index = 2 #randint(1,5)
decimalDigits = 1 #randint(1, 10)
    
print(radicand, index, decimalDigits)
print(root(radicand, index, decimalDigits))
