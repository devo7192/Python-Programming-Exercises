def printASCIITable():
    # Displays the ASCII number and its corresponding text character, from 32 to 126 (printable ASCII chars)
    for i in range(32, 127):
        print(i, chr(i)) # chr converts int -> code point
                         # ord converts code point -> int

printASCIITable()