#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

print "1.",
num = float(raw_input("Enter a number that is divisible by 3!: "))
while (num%3) != 0:
    num = float(raw_input('Please try again: '))
print "countdown from:",num
while num>0:
    print num
    num-=3

print "BRASTOFFFF!!!!"
