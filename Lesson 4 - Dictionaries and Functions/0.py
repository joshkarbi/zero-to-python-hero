'''
Motivation for functions.
'''

# Reason 1: Repeat steps but not in a loop
# Program start
# Calculate how much money we can spend
chequeing_accnt_balance = 500
savings_accnt_balance = 1000
us_dollar_savings = 100
credit_card_debt = 350

amount_we_can_spend = us_dollar_savings + chequeing_accnt_balance + savings_accnt_balance + credit_card_debt

# .... some time goes by ....
# We bought something....
purchase_price = 50
credit_card_debt += purchase_price

# We need to recalculate how much we can spend
amount_we_can_spend = chequeing_accnt_balance + savings_accnt_balance + credit_card_debt


# Reason 2: Almost doing the same thing but slightly different.
# i.e. calculate the cost of an apple and an orange
apple_price = 10.99
tax_rate = 0.13
purchase_price = apple_price * (1 + tax_rate)

orange_price = 8.99
tax_rate = 0.13
purchase_price = orange_price * (1 + tax_rate)
