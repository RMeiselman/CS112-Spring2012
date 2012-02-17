#!/usr/bin/env python
from random import randint

input_number=int(raw_input())
list1=[]

#changes the list to include random number
for _ in range(input_number):
    list1.append(randint(0,20))

#prints list a first time
print list1

s=1
while s:
    s=0
    for var in range(1,input_number):
        if list1[var-1]>list1[var]:
            input_number1=list1[var-1]
            input_number2=list1[var]
            list1[var-1]=input_number2
            list1[var]=Input_number1
            s=1
#prints list a second time
print list1
