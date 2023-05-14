def drawBox(size):
    
    if size < 1:
        return
    
    print(' ' * (size + 1), end='')
    print('+' + ('-' * (size*2)) + '+')
    
    for i in range(size):
        print(' ' * (size - i) + '/' + (' ' * (size*2)) + '/' + (' ' * i) + '|')

    print('+' + ('-' * (size*2)) + '+' + (' ' * size) + '+')

    for i in range(size):
        print('|' + (' ' * size * 2) + '|' + (' ' * (size-(i+1))) + '/')
    
    print('+' + ('-' * (size*2)) + '+')


drawBox(2)

