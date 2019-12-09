import os, sys
from person import Person

def createPerson(firstName, lastName, employeeNum):
    person = Person(firstName, lastName, employeeNum)
    print(person.getFirstName())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error::::Provide 3 arguments - firstName, lastName, employeeNum")
    else:
        createPerson(sys.argv[1], sys.argv[2], sys.argv[3])