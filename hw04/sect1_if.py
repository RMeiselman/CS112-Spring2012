#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

n = raw_input("Enter a number: ")
n = int(n)
if n % 2 == 0 :
    print n, "is an even number"
else:
    print n, "is an odd number"
    print n,"*",2,"=",n*2

if n % 3 == 0 :
    print n+4
else :
    print n
    
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print letter

    
    

