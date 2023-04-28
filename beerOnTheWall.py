# Program that displays the lyrics to "99 Bottles of Beer"

def lyrics(x):
    
    if x > 1:
        print(x, 'bottles of beer on the wall,')
        print(x, 'bottles of beer,')
        print('Take one down,')
        print('Pass it around,')
        if x-1 > 1: 
            print(x-1, 'bottles of beer on the wall,')
        else:
            print(x-1, 'bottle of beer on the wall,')

    elif x == 1:
        print(x, 'bottle of beer on the wall,')
        print(x, 'bottle of beer,')
        print('Take one down,')
        print('Pass it around,')
        print('No more bottles of beer on the wall!')       


i = 99
while i > 0:
    lyrics(i)
    i -= 1