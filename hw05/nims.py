#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

print "\n\nWelcome to the game of nims!\n"
print "Number of stones in the pile: 40"
print "Max number of stones per turn: 5\n\n"

num_stones = 40
max_picks = 5

while (num_stones > 0):
    try :
        #### Player 1 picks #####
        ply1_pick = int(raw_input("Player 1 [1-5]: "))
    
        while (ply1_pick > max_picks) or (ply1_pick < 1) :
            print "Invalid number of stones. Choose from between 1 and 5.  Please try again."
            ply1_pick = int(raw_input("Player 1 [1-5]: "))
    
        while ply1_pick > int(num_stones):
            print "Not enough stones. Only ", num_stones, " left. Please try again."
            ply1_pick = int(raw_input("Player 1 [1-5]: "))
    
        num_stones -= ply1_pick
        print num_stones, "stones left.\n"
    
        if num_stones <= 0 :
            print "\n\nPlayer 2 Wins!\n\n"
	    break
    
    
        #### Player 2 picks #####
        ply2_pick = int(raw_input("Player 2 [1-5]: "))
    
        while (ply2_pick > max_picks) or (ply2_pick < 1) :
            print "Invalid number of stones. Choose from between 1 and 5. Please try again."
            ply2_pick = int(raw_input("Player 2 [1-5]: "))
    
        while ply2_pick > int(num_stones):
            print "Not enough stones. Only ", num_stones, " left. Please try again."
            ply2_pick = int(raw_input("Player 2 [1-5]: "))
    
        num_stones -= ply2_pick
        print num_stones, "stones left.\n"
    
        if num_stones <= 0 :
            print "\n\nPlayer 1 Wins!\n\n"
            break
    
    except ValueError:	
	print "Ooops. Please enter a valid number."

print "Thank you for playing!"
