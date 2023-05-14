
def bubbleSort(numbers):

    swapsMade, swapsRecorded = 0, 0

    while True:
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                swapsMade += 1

        if swapsMade == swapsRecorded:
            break
        
        swapsRecorded = swapsMade

    # print(numbers)


bubbleSort([2, 0, 4, 1, 3, 6, 5, 7, 8, 9, 13, 12, 11, 10, -1, 33, -6])
