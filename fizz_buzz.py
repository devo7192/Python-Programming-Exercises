def fizzBuzz(upTo):
    # Loop from 1 up to (and including) the upTo parameter:
    for i in range(1, upTo+1):
        # If the loop number is divisible by 3 and 5, print 'FizzBuzz':
        if (i % 15 == 0):
            print("FizzBuzz", end = " ")
        elif (i % 3 == 0):
        # Otherwise the loop number is divisible by only 3, print 'Fizz':
            print("Fizz", end = " ")
        elif (i % 5 == 0):
        # Otherwise the loop number is divisible by only 5, print 'Buzz':
            print("Buzz", end = " ")
        else:
        # Otherwise, print the loop number:
            print(i, end = " ")        

fizzBuzz(35)