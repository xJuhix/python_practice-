from random import random

#creates a function and ha n as positional argument
def flipCoin(n):
    #create and empty list where the results will be stored
    flip = []

    #loop throgh the amount of flips that is taken as the argument and append it to the empty fliplist
    for i in range(0,n):
        flip.append("Heads" if random() > 0.5 else "Tails")
    
    return(flip)

#invoke the fuction with the argument
print(flipCoin(25))