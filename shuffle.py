import random

def shuffle(values):

    for i in range (len(values)):
        swapIndex = random.randint(0, len(values)-1)
        values[i], values[swapIndex] = values[swapIndex], values[i]


# nums = [1, 2, 3, 4, 5]
# shuffle(nums)
# print(nums)

random.seed(42)
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    assert len(testData1) == 10
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]