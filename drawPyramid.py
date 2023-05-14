def drawPyramid(height):
    for i in range(height):
        layer = '#' * (i * 2 + 1)
        print(layer.center(1 + ((height-1)*2)))


drawPyramid(20)