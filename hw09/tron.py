#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *

## Defining player one. ##
class tron_p1:
     def __init__(self, surface, x, y, length):
         self.surface = surface
         self.x = x
         self.y = y
         self.length = length
         self.dir_x = 0
         self.dir_y = -1
         self.body = []
         self.crashed = False
 
# Defining player one's keyboard controls (w,a,s,d) and which direction they move the character towards. 
     def key_event_p1(self, event):
          if event.key == pygame.K_w and self.dir_y != 1: # This prevents the player from crashing into themselves while pressing the key that would go in the opposite direction of their current movement.
               self.dir_x = 0
               self.dir_y = -1
          elif event.key == pygame.K_d and self.dir_x != -1:
               self.dir_x = 1
               self.dir_y = 0
          elif event.key == pygame.K_s and self.dir_y != -1:
               self.dir_x = 0
               self.dir_y = 1
          elif event.key == pygame.K_a and self.dir_x != 1:
               self.dir_x = -1
               self.dir_y = 0

# Defining player one's movement. 
     def move(self):
         self.x += self.dir_x
         self.y += self.dir_y
 
         # Tells the character to crash if it runs into itself.
         if (self.x, self.y) in self.body: 
             self.crashed = True
 
         self.body.insert(0, (self.x, self.y))

# Defining player one's color (red)         
     def draw(self):
         for x, y in self.body:
             self.surface.set_at((x, y), (255, 0, 0))


## Defining player two (almost the same as Player One's stuff). ##
class tron_p2:
     def __init__(self, surface, x, y, length):
         self.surface = surface
         self.x = x
         self.y = y
         self.length = length
         self.dir_x = 0
         self.dir_y = -1
         self.body = []
         self.crashed = False
 
# Defining player two's keyboard controls (the arrow keys). 
     def key_event_p2(self, event):
          if event.key == pygame.K_UP and self.dir_y != 1:
               self.dir_x = 0
               self.dir_y = -1
          elif event.key == pygame.K_RIGHT and self.dir_x != -1:
               self.dir_x = 1
               self.dir_y = 0
          elif event.key == pygame.K_DOWN and self.dir_y != -1:
               self.dir_x = 0
               self.dir_y = 1
          elif event.key == pygame.K_LEFT and self.dir_x != 1:
               self.dir_x = -1
               self.dir_y = 0

# Defining player two's movement. 
     def move(self):
         self.x += self.dir_x
         self.y += self.dir_y
 
         if (self.x, self.y) in self.body:
             self.crashed = True
 
         self.body.insert(0, (self.x, self.y))
 
# Defining player two's color (blue).         
     def draw(self):
         for x, y in self.body:
             self.surface.set_at((x, y), (0, 0, 255))
 
# The dimensions of the screen.
width = 700
height = 600
 
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
end_game = False

p1 = tron_p1(screen, width/3, height/2, 500) # Player one's starting position.
p2 = tron_p2(screen, width/2, height/2, 500) # Player two's starting position.

# Printed instructions on how to play the game.
print "Controls: "
print "Player one is Red and uses w,a,s,d to move."
print "Player two is blue and uses the arrow keys to move."
print "Avoid the edges of the screen, the other player and your own trail."

# While the game hasn't ended, play the game. (This is how the player can exit the game using the escape key but this extra while loop was originally how I was going to have the space bar start and repeat work). It also adds a pause at the end of the game after one eprson crashes (but before the player exits) so I decided to keep it in.
while end_game == False:

# While the game is running... #
     while running == True:

          screen.fill((0, 0, 0)) #Making the screen black.
    
          # Player one during the game.
          p1.move()
          p1.draw()

          # If player one crashes into itself or into the boundries of the screen, end the game.
          if p1.crashed or (p1.x <= 0) or (p1.x >= width-1) or (p1.y <= 0) or (p1.y >= height-1):
               print "Player one crashes!"
               running = False

          # If player one crashes into player two, end the game.
          if (p1.x, p1.y) in p2.body:
               p1.crashed = True
               print "Player one crashes!"
               running = False

          # Key commands for both players.
          for event in pygame.event.get():
               
               # Exiting the game using the escape key during the game.
               if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                    end_game = True
                    print "Thanks for playing!"

               # Player one and two controls.
               elif event.type == pygame.KEYDOWN:
                    p1.key_event_p1(event)

                    p2.key_event_p2(event)
 
          # Player two during the game.
          p2.move()
          p2.draw()

          # If player two crashes into itself or into the boundries of the screen, end the game.
          if p2.crashed or (p2.x <= 0) or (p2.x >= width-1) or (p2.y <= 0) or (p2.y >= height-1):
               print "Player two crashes!"
               running = False

          # If player two crashes into player one, end the game.
          if (p2.x, p2.y) in p1.body:
               p2.crashed = True
               print "Player two crashes!"
               running = False

          pygame.display.flip()
          clock.tick(250)

     # Exiting the game using the escape key after the game is over.
     for event in pygame.event.get():
          if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
               end_game = True
               print "Thanks for playing!"



"""

I couldn't find a way to make the game restart when the player hits the spacebar. All of the ways I tried made it so the game would only run if the spacebar was constantly being pressed and this was annoying. So for the sake of my sanity, the game will just have to be restarted in the terminal.

One of the most promising ways I tried to make this thing restart:
- Turning the enitre game (everything inside the "while running == True" loop) into a function (named "play_tron") and then making this:

     for event in pygame.event.get():
          if event.type == KEYDOWN and event.key == pygame.K_SPACE:
               play_tron()

          elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
               end_game = True

But this didn't work. And this was about as close as the internet got to gettingthe "spacebar restart" problem to work. Soooo... this made me sad. :(


"""
