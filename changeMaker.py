def makeChange(amount): # Enter $ amount in cents
    
    coins = {}

    if (amount//25) >= 1:
        coins['quarters'] = amount//25
        amount = amount % 25

    if (amount//10) >= 1:
        coins['dimes'] = amount//10
        amount = amount % 10

    if (amount//5) >= 1:
        coins['nickels'] = amount//5
        amount = amount % 5

    if amount >= 1:
        coins['pennies'] = amount

    return coins


assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}

