# QUIT - only accept this
# EQ - i number of values equating to the value of equation
# POLY - returns the polynomial
# EQUALS - The 'X' value
# ADD 1 1 - first value is the coefficient
#           second is added to the coefficient
# DIFF 1 1 - same as above
import sys
import polynomialeq

if __name__ == "__main__":
    print("Enter one of the following: QUIT, EQ, POLY, EQUALS, ADD, DIFF\n" +
          "\n\'QUIT\' will end the application." +
          "\n\'EQUAT\' will allow you to define the polynomial from 0 -> i, a polynomial structure follows => x^0.....x^i" +
          "\n\'POLY\' will return the current polynomial." +
          "\n\'EVAL 0\' fills in for x in the polynomial." +
          "\n\'ADD 1 2\' adds the second value to the coefficient at the first value." +
          "\n\'DIFF 1 2\' subtracts the second value from the coefficient at the first value", end='\n')
    
    userInput = str(input())
    if userInput != "QUIT":
        shouldTerminate = False
        firstCall = True
        while not shouldTerminate:
            poly = polynomialeq.Polynomial(userInput)
            poly.performFunction()
            userInput = str(input())
            if userInput == "QUIT":
                shouldTerminate = True
            
    else:
        print("QUITING", end="\n")