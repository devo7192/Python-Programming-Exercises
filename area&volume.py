def area(length, width):
    # Return the product of the length and width:
    return length * width

def perimeter(length, width):
    # Return the sum of the length twice and the width twice:
    return (length * 2) + (width * 2)

def volume(length, width, height):
    # Return the product of the length, width, and height:
    return length * width * height

def surfaceArea(length, width, height):
    # Return the sum of the area of each of the six sides:
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40 
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000 
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340

