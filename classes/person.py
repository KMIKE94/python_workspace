class Person:
    firstName = ""
    lastName = ""
    employeeNum = -1

    def __init__(self, firstname, lastName, employeeNum):  
        self.firstName = firstname
        self.lastName = lastName
        self.employeeNum = employeeNum

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getEmployeeNum(self):
        return self.employeeNum
    
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastName(self, lastName):
        self.lastName = lastName