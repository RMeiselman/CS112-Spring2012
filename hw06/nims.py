#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

# Welcomes the player and explains the rules of nims. There are 40 stones in the pile and a player can only pick 5 stones per turn.
print "\n\n Welcome to the game of nims! \n"
print "Number of stones in the pile: 40"
print "Max number of stones per turn: 5 \n\n"

# The variable "num_stones" is the total number of stones left in the pile. The variable "Max_picks" sets the maximum number of stones that the player can pick per turn.
num_stones = 40
max_picks = 5


while (num_stones > 0): # While the number of stones in the pile is greater than zero.
    try :
        #### Player 1 picks #####
        ply1_pick = int(raw_input("Player 1 [1-5]: ")) # Asks player one for a number of stones to pick.
    
        # While player one's pick is greater than the maximum pick number (5) or if player one's pick is less than one.
        while (ply1_pick > max_picks) or (ply1_pick < 1) : 

            # Print an error message and have player one pick again. 
            print "Invalid number of stones. Choose from between 1 and 5.  Please try again."
            ply1_pick = int(raw_input("Player 1 [1-5]: "))
    
        # While player one's pick is greater than the number of stones left in the pile.
        while ply1_pick > int(num_stones):
            
            # Print an error message stating how many stones are left in the pile and have player one pick again.
            print "Not enough stones. Only ", num_stones, " left. Please try again."
            ply1_pick = int(raw_input("Player 1 [1-5]: "))
    
        # Subtract player one's pick from the number of stones left in the pile and print how many stones are left in the pile.
        num_stones -= ply1_pick
        print num_stones, "stones left.\n"
    
        # If the number of stones is less than or equal to zero print that player two wins and the game ends.
        if num_stones <= 0 :
            print "\n\nPlayer 2 Wins!\n\n"
	    break
    
    
        #### Player 2 picks #####
        ply2_pick = int(raw_input("Player 2 [1-5]: ")) # Asks player two for a number of stones to pick.
    
        # While player two's pick is greater than the maximum pick number (5) or if player two's pick is less than one.
        while (ply2_pick > max_picks) or (ply2_pick < 1) :
            
            # Print an error message and have player two pick again. 
            print "Invalid number of stones. Choose from between 1 and 5. Please try again."
            ply2_pick = int(raw_input("Player 2 [1-5]: "))
    
        # While player two's pick is greater than the number of stones left in the pile.
        while ply2_pick > int(num_stones):

            # Print an error message stating how many stones are left in the pile and have player two pick again.
            print "Not enough stones. Only ", num_stones, " left. Please try again."
            ply2_pick = int(raw_input("Player 2 [1-5]: "))
        
        # Subtract player two's pick from the number of stones left in the pile and print how many stones are left in the pile
        num_stones -= ply2_pick
        print num_stones, "stones left.\n"
    
        # If the number of stones is less than or equal to zero print that player one wins and the game ends.
        if num_stones <= 0 :
            print "\n\nPlayer 1 Wins!\n\n"
            break
    
    # If the player enters something other than a number print an error statement.
    except ValueError:	
	print "Ooops. Please enter a valid number."

print "Thank you for playing!"
