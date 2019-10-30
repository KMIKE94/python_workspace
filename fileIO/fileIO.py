import sys

REVERSED_TEXT = "_reverse.txt"
FILE_NOT_FOUND_EXCEPTION = "File not found"
FILE_WRITE_EXCEPTION = "Unable to write to file"
FILE_READ_OPERATION = "r"
FILE_WRITE_OPERATION = "w"

def getFileContents(fileName):
    print("Reading contents from file ", fileName)
    try:
        with open(fileName, FILE_READ_OPERATION) as file:
            lineList = []
            for line in file.readlines():
                formattedLine = line.replace("\n", "")
                lineList.append(formattedLine)
            return lineList    
    except FileNotFoundError:
        print(FILE_NOT_FOUND_EXCEPTION)

def printList(inputList):
    counter = 1
    for line in inputList:
       print("Item(" + str(counter) + "): " + line, end=' ')
       counter += 1

def writeReversedFileContents(reversedList, file_name):
    newFileName = file_name + REVERSED_TEXT
    print("Writing contents of file " + newFileName + " in reverse order")
    try:
        with open(newFileName, FILE_WRITE_OPERATION) as file:
            for line in reversedList:
                file.write(line + "\n")
            return True
    except IOError:
        print(FILE_WRITE_EXCEPTION, newFileName)


if __name__ == "__main__":
    fileName = str(sys.argv[1])
    fileNameWithSuffix = fileName + ".txt"
    
    inputList = getFileContents(fileNameWithSuffix)
    inputList.reverse()
    if writeReversedFileContents(inputList, fileName):
        print("Completed operation successfully")
