'''
Intro to libraries.
'''

import math

for angle in [0, math.pi/2, math.pi, math.pi*3/2, 2*math.pi]:
    sin = round(math.sin(angle), 4)
    print("The sine of {} is {}".format(angle, sin) )


from math import pi

from math import sin as sine_of_angle

sine_of_angle(pi)

from math import * # now we wouldn't have to write math.__ , 