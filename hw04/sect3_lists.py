#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

print "1.", 

print len (nums)
listtotal = len (nums)

# 2.  Append 3 and 5 to nums

print "2.",

nums.append (3)
nums.append (5)
print (nums)

# 3.  Remove the last element from nums

print "3.",

lastnum = (listtotal-1)+2
print lastnum
for num in nums:
    print nums


# 4.  Set the 3rd element to 7

print "4.",

nums[3]=7
print nums
