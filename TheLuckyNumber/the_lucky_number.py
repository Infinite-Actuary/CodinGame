'''
A lucky number is a 10-based number, which has at least a "6" or an "8" in its digits.
However, if it has "6" and "8" at the same time, then the number is NOT lucky.
For example, "16", "38", "666" are lucky numbers, while "234" , "687" are not.

Now we want to know how many lucky numbers (without leading zeroes) are there between L and H, inclusive?
'''

# Success: Sample, Overlapping, Same, Larger
# Failure: 64-bit integer

import sys
import math

l, h = [int(i) for i in input().split()]
n = 0

for x in range(l, r + 1):
    luck6 = False
    luck8 = False
    
    for c in str(x):
        if int(c) == 6:
            luck6 = True
        if int(c) == 8:
            luck8 = True
        if luck6 & luck8:
            break
            
    # xor 
    if luck6 ^ luck8:
        n += 1

print(n)
