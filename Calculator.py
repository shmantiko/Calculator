from random import *

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

def wurzel(radikand, wurzelexponent, decimal_digits):
    if wurzelexponent == 0:
        return("Error: not a valid exponent")
    elif radikand < 0:
        return("Error: does not handle complex numbers")
    if wurzelexponent < 0:
            return("Error: does not compute negative exponents yet")
    border1 = 0
    border2 = radikand
    counter = 0
    while True:
        counter = counter + 1
        if border1 - border2 < -1:
            guess = randint(border1, border2)
        else:
            guess = uniform(border1, border2)
        guess_p = potenz(guess, wurzelexponent)
        if guess_p == radikand:
            print(f"I have guessed {counter} times")
            return(guess)
        elif border2 - border1 <= potenz(0.1, decimal_digits + 1):
            print(f"I have guessed {counter} times")
            return(round(guess, decimal_digits))
        elif guess_p > radikand:
            border2 = guess
        elif guess_p < radikand:
            border1 = guess
        else:
            return("Error")

# Test Values

#basis = randint(0, 10)
#exponent = randint(-5, 5)

radikand = 2 #randint(0, 100)
wurzelexponent = 1 #randint(1,5)
decimal_digits =  -1 #randint(1, 10)
    
print(radikand, wurzelexponent, decimal_digits)
print(wurzel(radikand, wurzelexponent, decimal_digits))

# things that break the function
# - wurzelexponent cant be with a comma
# - negative exponents
# - comma numbers in decimal digits
# - negative number in decimal digits sometimes outputs 0.0 sometimes 2
