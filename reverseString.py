def reverseString(text):
    
    text = list(text) # "Can't manipulate string" workaround 
    
    for i in range(len(text)//2): # Iterate through to midway point
        mirrorIndex = len(text)-1-i
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i] # Swaps simultaneously - no temp!

    return ''.join(text)
    

assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'

