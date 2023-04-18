def getSmallest(numbers):

    if numbers == []:
        return None
    
    currentMin = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < currentMin:
            currentMin = numbers[i]
    
    return currentMin

def getBiggest(numbers):

    if numbers == []:
        return None
    
    currentMax = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > currentMax:
            currentMax = numbers[i]
    
    return currentMax 

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None