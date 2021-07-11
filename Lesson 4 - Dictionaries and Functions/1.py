'''
Intro to functions
'''

# A simple function with no arguments or return values
def print_welcome_message():
    print("Welcome to functions!")

print_welcome_message()


def calculate_total_cost(sticker_price, tax_rate):
    total_cost = sticker_price * (1 + tax_rate)
    return total_cost

cost = calculate_total_cost(10.99, 0.13)
print(calculate_total_cost(10.99, 0.13))

# With a default tax rate
def calculate_total_cost_default(sticker_price, tax_rate=0.13):
    return sticker_price * (1 + tax_rate)

cost = calculate_total_cost_default("A", 5)



cost = calculate_total_cost_default(10.99)
cost = calculate_total_cost_default(10.99, 0.15)
print(calculate_total_cost_default(10.99))

def stupid(a, b, c):
    return 10
    print("hello")

x = stupid(1, 2, 3)

