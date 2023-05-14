def getTitleCase(text):
    # returns the title case form of the string: every word begins with an uppdercase
    
    title = ''
    newWord = True
    for x in text:
        
        if x.isalpha() == False:
            title += x
            newWord = True
        
        else:   # found a letter
            if newWord:
                title += x.upper()
                newWord = False
            else:
                title += x.lower()

    return title
        

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()