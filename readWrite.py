def writeToFile(fileName, textToWrite):
    with open(fileName, 'w') as f:
        f.write(textToWrite)

def appendToFile(fileName, textToWrite):
    with open(fileName, 'a') as f:
        f.write(textToWrite)

def readFromFile(fileName):
    with open(fileName, 'r') as f:
        return f.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'