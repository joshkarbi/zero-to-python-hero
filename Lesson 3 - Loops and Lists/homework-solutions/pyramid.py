'''
Based on size, print something like
*
**
***
**
*
(size = 5)
'''

size = 9
for i in range(size):
    if i <= size/2:
        print("* " * (i + 1))
    else:
        # When i == 3: print 2
        # When i == 4: print 1
        row_past_midpoint = i - int(size/2)
        max_width = int(size/2) + 1
        print("* " * (max_width - row_past_midpoint) )