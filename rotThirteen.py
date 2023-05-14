def rot13(text):
    
    result = ''

    for char in text:

        if char.isalpha():

            ordinance = ord(char) + 13
            if char.isupper() and ordinance > 90:   # 'Z'
                    ordinance -= 26
            
            if char.islower() and ordinance > 122:  # 'z'
                    ordinance -= 26
            
            result += chr(ordinance)
            
        else:
            result += char

    return result


assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'