from random import *

#naming is now consistently in english
#fixed code for negative exponents
def exponentiation(base, exponent):
    result = base
    if exponent > 0:
        for x in range(1,exponent):
            result = result * base
    elif exponent < 0:
        for x in range(exponent,-1):
            result = result * result
        result = 1 / result
    else:
        result = 1
    return(result)


#works with negative indexes now
def root(radicand, index, decimalDigits):
    negIndex = False
    if index == 0:
        print("Error: not a valid exponent")
        return
    elif index < 0: 
        index *= -1
        negIndex = True
    elif radicand < 0:
        print("Error: does not handle complex numbers")
        return
    border1 = 1
    border2 = radicand
    guess = 1
    if radicand >= 1:
        while True:
            if border2 - border1 <= 1:
                guess = uniform(border1, border2)
            else:
                guess = randint(border1, border2)
            guess_p = exponentiation(guess, index)
            if guess_p == radicand:
                result = guess
                break 
            elif border2 - border1 <= exponentiation(0.1, decimalDigits) * 0.1:
                result = round(guess, decimalDigits)
                break
            elif guess_p > radicand:
                border2 = guess
            elif guess_p < radicand:
                border1 = guess
            else:
                print("Error")
                break
    elif radicand < 1:
        while True:
            if border1 - border2 <= 1:
                guess = uniform(border2, border1)
            else:
                guess = randint(border2, border1)
            guess_p = exponentiation(guess, index)
            if guess_p == radicand:
                result = guess
                break
            elif border1 - border2 <= exponentiation(0.1, decimalDigits) * 0.1:
                result = round(guess, decimalDigits)
                break
            elif guess_p > radicand:
                border1 = guess
            elif guess_p < radicand:
                border2 = guess
            else:
                print("Error")
                break

    if negIndex == True:
        result = 1 / result
    return(round(result, decimalDigits))

# Test Values

#base = randint(0, 10)
#exponent = randint(-5, 5)

radicand = randint(0, 100)
index = randint(-5,5)
decimalDigits = 11
    
print(radicand, index)
print(root(radicand, index, decimalDigits))
#added the variable instead of the number