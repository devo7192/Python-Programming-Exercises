def calculateSum(numbers):
    
    sumTotal = 0
    for x in numbers:
        sumTotal += x    

    return sumTotal

def calculateProduct(numbers):

    product = 1
    for x in numbers:
        product *= x

    return product


assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840