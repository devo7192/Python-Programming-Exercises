def mode(numbers):
    # returns the most frequent appearing number
    if numbers == []:
        return None
    
    numCount = {}
    for x in numbers:
        numCount[x] = numCount[x] + 1 if x in numCount else 1


    return max(numCount, key = numCount.get)


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4