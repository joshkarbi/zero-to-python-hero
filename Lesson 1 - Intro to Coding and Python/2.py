'''
Intro to Variables.
'''

a = 1           # an integer
b = 1.5         # a decimal number (we call these "floats")
c = 't'         # One character
d = "a string"  # a string is a bunch of characters in one variable

a = a + 1
b = a + b

a = a * 2
b = a / 2
a = a - b

c = "My name is " + " Josh." # adding strings
c = f"A is {a} and B is {b}" # inserting values into strings
print(c)
c = "BlahBlahBlah " * 10 # will be BlahBlahBlah BlahBlahBlah... 10 times

# We can get input through the console with:
c = input("What's your name? ")
print(c)

# Casting 
age = input("What's your age")
age = int(age) # save it as a number
pi = input("Whats pi?")
pi = float(pi) # save it as a decimal number