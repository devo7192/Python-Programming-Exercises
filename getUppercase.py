def getUppercase(text):
    
    capitalizedText = ''
    for x in text:
        if 97 <= ord(x) <= 122:
            capitalizedText += chr(ord(x) - 32)
        else:
            capitalizedText += x

    return capitalizedText


assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''