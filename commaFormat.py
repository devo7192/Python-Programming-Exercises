def commaFormat(number):

    stringNum = str(number)

    decimalValue = ''
    decimalIndex = stringNum.find('.')
    if decimalIndex != -1:
        decimalValue = stringNum[decimalIndex:]
        stringNum = stringNum[:decimalIndex]

    count = 0
    formattedNum = []
    for i in range(len(stringNum)-1, -1, -1):   
        
        if count == 3:
            formattedNum.insert(0, ',')
            count = 1
        else:
            count += 1

        formattedNum.insert(0, stringNum[i])

    return ''.join(formattedNum) + decimalValue


assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
