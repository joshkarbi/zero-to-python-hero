'''
Calculates an expression seperated by spaces:
i.e. 
    5 + 3
    2 x 3 / 4 - 2 + 1 - 4
'''
expression = input("Enter expression: ")
parts = expression.split(" ")

result = 0
left, middle, right = 0, 1, 2
while right < len(parts):
    op1, oper, op2 = float(parts[left]), parts[middle], float(parts[right])

    if oper=="+":
        result = op1 + op2
    elif oper == "-":
        result = op1 - op2
    elif oper == "x":
        result = op1 * op2
    else:
        result = op1 / op2

    parts[right] = result
    left += 2
    middle += 2
    right += 2

print("The result is", result)