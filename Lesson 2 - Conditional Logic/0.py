'''
If Statements
'''

cash_balance = 99.43
price_of_headphones = 150.99

# IF 
if cash_balance >= price_of_headphones:
    print("You can afford the headphones.")
else:
    print("You cannot afford the headphones.") 

if cash_balance >= price_of_headphones:
    print("You can afford the headphones.")
print("You cannot afford the headphones.") 



# Tabs used to tell the Computer what code is inside of what
if True and False:
    print("In the if statement.")

if True or False:
    print('something')
print("Not in the if.")
if True:
    print("hey")

# Else-if
dad_is_home_for_dinner = False
mom_is_home_for_dinner = True
if dad_is_home_for_dinner:
    result = "McDonalds"
elif mom_is_home_for_dinner:
    result = "Harveys"
elif False:
    dosomething()
elif False:
    dosomething()
else:
    result = "Baskin Robbins"


## Nested Statements
if mom_is_home_for_dinner:
    if cash_balance >= price_of_headphones:
        print("BLAH")
    else:
        print("WOOHOO")
elif dad_is_home_for_dinner:
    print("Something else")
else:
    print("Another thing!")