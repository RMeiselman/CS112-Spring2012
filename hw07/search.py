#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

while True:
    try:
        nums = input_nums() # User inputs a list of numbers.

        # Finds if there are duplicates of numbers
        for num in nums:
            if nums.count(num) > 1:
                raise NameError ('duplicate')
        break
    
    # Prints error statement if user types anything but number
    except ValueError:
        print "Please enter numbers."   
    
    # Prints error statement if user repeats numbers
    except NameError:
        print "Please don't repeat numbers."

nums_sort = sorted(nums) # User's number list is sorted.
print "I have sorted your numbers"
print nums_sort

while True:
    try:
        # User inputs a number to find in the list
        num_to_find = int(raw_input("Which number should I find: "))
        break

    # Prints error statement if user enters anything but number
    except ValueError:
        print "Please enter a number."

min_position = 0 # Checks the minimum position in the list

max_position = len(nums_sort) - 1 # Checks the maximum position in the list.

mid_position = (min_position + max_position) / 2 # Checks the middle position in the list by averaging the minimum and maximum positions

# While the number to find is not equal to the middle position or if the minimum position is less than maximum position:
while (nums_sort[mid_position] != num_to_find) or (min_position < max_position):

    # If the number to find is greater than the middle position, check the position to the right (add one to the middle position).
    if num_to_find > nums_sort[mid_position]:
        min_position = mid_position + 1
        
        # Check the middle position again.
        mid_position = (min_position + max_position) / 2

    # If the number to find is less than the middle position, check the position to the left (subtract one from the middle position).
    elif  num_to_find < nums_sort[mid_position]:
       max_position = mid_position - 1
       
       # Check the middle position again.
       mid_position = (min_position + max_position) / 2

    # If the middle position matches the number to find or if the minimum position becomes greater than the maximum position, break the while loop.
    if (nums_sort[mid_position] == num_to_find) or (min_position > max_position):
        break

# If the middle position is equal to the number to find then print that the number to find has been found at it's position in the list. I added one to the middle position so that when the position is printed it won't be based off of starting the counting from zero.
if (nums_sort[mid_position] == num_to_find):
     print "Found", num_to_find, "at position", mid_position + 1 , "in sorted list."

# If the number could not be found at all, print that the number couldn't be found.
else:
    print "Could not find", num_to_find



