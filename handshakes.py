def printHandshakes(people):

    shakes = 0
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i] + ' shakes hands with ' + people[j])
            shakes += 1
    
    return shakes


assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6