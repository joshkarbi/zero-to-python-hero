'''
Count numbers and say which is even or odd.
'''

x = int(input("What should we count up to? "))

# Solution 1 using while loops
current = 1
while current <= x:
    if current%2 == 0:
        print(current, "which is even.")
    else:
        print(current, "which is odd.")
    current += 1

# Solution 2 using for loops
print("\n\n")
for num in range(current-1):
    this_num = num + 1
    if this_num%2 == 0:
        print(this_num, "which is even.")
    else:
        print(this_num, "which is odd.")