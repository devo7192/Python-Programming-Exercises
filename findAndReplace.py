def findAndReplace(text, oldText, newText):

    replacedText = ''
    i = 0
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replacedText += text[i]
            i += 1
        
    return replacedText

# These assert functions stop the program if their condition is False
assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox', 'fox', 'dog') == 'The Fox and dog' # Note: case-sensitive