import random
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
COMBINATION = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def generatePassword(length):
    # password must have at least one lowercase, one uppercase, one number and one special character
    if length < 12:
        length = 12
    
    pw = []
    pw.append(LOWER_LETTERS[random.randint(0,25)])
    pw.append(NUMBERS[random.randint(0,9)])
    pw.append(SPECIAL[random.randint(0,11)])
    pw.append(UPPER_LETTERS[random.randint(0,25)])

    i = 4
    while i < length:
        pw.append(COMBINATION[random.randint(0,74)]) 
        i += 1
    
    random.shuffle(pw)
    return ''.join(pw)


assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial