'''
Nested loops.
'''

row, length = 1, 5
while row <= length:
    row += 1
    column = 1
    while column <= length:
        column += 1
        print("X", end=" ")
    print("")