class Polynomial:
    _quit = "QUIT"
    _equat = "EQUAT"
    _poly = "POLY"
    _eval = "EVAL"
    _add = "ADD"
    _diff = "DIFF"

    def __init__(self, userInput):
        self.userInput = userInput
        self.polynomial = []

    def defineEquation(self, equation):
        inputList = equation.split(" ")
        coefficient = 0
        self.polynomial.clear()
        for input in inputList[1:]:
            self.polynomial.append(str(input) + "x^" + str(coefficient))
            coefficient += 1
        self.printPolynomial()

    def evaluateEquation(self, userInput):
        if self.polynomial:
            # Evaluate the equation
            xVal = list(userInput.split(" "))[-1]
            value = 0
            for x in self.polynomial:
                wordList = list(x)
                numericalVal = int(wordList[0])
                # already have the x value in xVal above
                coeff = int(wordList[-1]) # last value of equation
                value += (numericalVal * int(xVal) ** coeff)
            print(value)
        else:
            print("Polynomial empty, please define an equation(EQUAT X....)",end=("\n"))

    def addCoefficient(self, userInput):
        inputList = userInput.split(" ")
        coeff = int(inputList[1])
        additive = int(inputList[2])

        # saved in polynomial as i-1 where i is the coeff value
        # find the coefficient
        if len(self.polynomial) >= (coeff+1):
            poly = self.polynomial[coeff]
            strList = list(poly)
            numericalVal = strList[0]
            powerVal = int(strList[-1])
            powerVal = powerVal + additive
            self.polynomial[coeff] = numericalVal + "*x^" + str(powerVal) 
            self.printPolynomial()
        else:
            print("Polynomial is not that large",end="\n")

    def subtractCoefficient(self, userInput):
        inputList = userInput.split(" ")
        coeff = int(inputList[1])
        diff = int(inputList[2])

        # saved in polynomial as i-1 where i is the coeff value
        # find the coefficient
        if len(self.polynomial) >= (coeff+1):
            poly = self.polynomial[coeff]
            strList = list(poly)
            numericalVal = strList[0]
            powerVal = int(strList[-1])
            powerVal = powerVal - diff
            self.polynomial[coeff] = numericalVal + "*x^" + str(powerVal) 
            self.printPolynomial()
        else:
            print("Polynomial is not that large",end="\n")


    def performFunction(self):
        userInput = self.userInput
        # We require the user to enter some values into the EQUAT part
        if userInput.startswith(Polynomial._equat) and userInput != Polynomial._equat:
            self.defineEquation(userInput)
        elif userInput == Polynomial._poly:
            self.printPolynomial()
        elif userInput.startswith(Polynomial._eval) and len(userInput.split(" ")) == 2:
            self.evaluateEquation(userInput)
        elif userInput.startswith(Polynomial._add) and len(userInput.split(" ")) == 3:
            # checking for 3 individual inputs means that
            # we define which coefficient we want to add a value to
            # and the value we add with
            self.addCoefficient(userInput)
        elif userInput.startswith(Polynomial._diff) and len(userInput.split(" ")) == 3:
            self.subtractCoefficient(userInput)
        else:
            print("Bad Input", end="\n")

    def printPolynomial(self):
        for poly in self.polynomial:
            print(poly, end=' ')
        print(end="\n")