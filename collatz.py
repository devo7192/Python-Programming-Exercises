def collatz(startingNumber):

    sequence = []
    if startingNumber < 1:
        return sequence
    
    num = startingNumber
    sequence.append(startingNumber)
    while num != 1:
        num = (num // 2) if (num % 2 == 0) else (3 * num + 1)
        sequence.append(num)


    return sequence


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum
    assert seq[-1] == 1
