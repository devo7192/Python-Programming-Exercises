def convertIntToStr(integerNum):
    
    if integerNum == 0:
        return '0'
    
    isPositive = True
    if integerNum < 0:
        isPositive = False
        integerNum *= -1

    digits = []
    intToStr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    
    while integerNum:
        peel = integerNum % 10
        integerNum //= 10
        digits.insert(0, intToStr.get(peel))
    
    return ''.join(digits) if isPositive else '-' + ''.join(digits)


for i in range (-10000, 10000):
    assert convertIntToStr(i) == str(i)
