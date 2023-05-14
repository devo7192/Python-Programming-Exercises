def convertStrToInt(stringNum):

    isPositive = True
    if stringNum[0] == '-':
        isPositive = False
        stringNum = stringNum[1:]

    StrToInt = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    intValue = 0
    placeValue = 1
    for i in range(len(stringNum)-1, -1, -1):
        intValue += StrToInt.get(stringNum[i]) * placeValue
        placeValue *= 10 

    return intValue if isPositive else intValue * -1


for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
