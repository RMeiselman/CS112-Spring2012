#!/usr/bin/env python

import random,sys,os,imghdr

from pygame import*
init()

# Constant Variables

# tx,ty = the dimensions of minefields, 100 max per side
try:
	BACKGROUND = image.load(random.choice([sys.argv[1]+'/'+f for f in os.listdir(sys.argv[1])if os.path.isfile(sys.argv[1]+'/'+f) and imghdr.what(sys.argv[1]+'/'+f)]))

	x,y=BACKGROUND.get_size()
	if x > 100 or y > 100 : BACKGROUND = transform.scale(BACKGROUND, BACKGROUND.get_rect().fit((0,0,100,100)).size);x,y = BACKGROUND.get_size()
except:
	BACKGROUND = Surface((520,520))
	BACKGROUND.fill(-1)
	x,y = BACKGROUND.get_size()

tx=x/50
ty=y/50

# mines = The number of mines in the field.
mines = (tx*ty)/10
if not mines:mines = 1

# empty =  The number of empty squares, that aren't mines.
empty = tx*ty - mines

# res = The size of a square.
res=800 / max(tx,ty)
if res > 26:res=26

screen = display.set_mode((tx * res, ty * res),0,32)
screen.blit(BACKGROUND,(-(x - tx * 26)/2, -(y - ty * 26)/2))
BACKGROUND = screen.copy();print transform.average_color(BACKGROUND)

# img_list = List of images for the square numbers (zero is left blank).
police = font.Font(font.get_default_font(), res)
police0 = font.Font(font.get_default_font(), res+2)
white = Surface((res,res));white.fill(transform.average_color(BACKGROUND)[:-1])
white.fill(-1,(0,0,res-1,res-1))
img_list = [white]+[white.copy()for i in range(8)]


for i in range(1,9):

	fi = police.render(str(i), 1, (i%2 * 124, i%8 * 31, i%4 * 62))
	fr = fi.get_rect()
	fr.center = (res - 1) / 2,(res - 1) / 2

	img_list[i].blit(fi, fr.topleft)

## Loading the Images.

boom = image.load('boom4.png')
mine = image.load('mine2.png')
flag = image.load('flag.png')
squares = image.load('squares2.png')
display.set_icon(mine)

# Temp = Making of empty boxes.
# Flags = Remembers the positions of flags.
temp = []
flags = []

# For init. other variables.
tx += 2;txy = tx * (ty + 2)
h = sum([range(x, tx - 2 + x)for x in range(tx + 1, txy - tx - 1, tx)],[])

# pt = Table representing the minefields.
pt = ['x'] * txy
for i in h:pt[i] = 0

# rects = List of rects.
rects = [screen.blit(squares, ((x%tx) * res, (x / tx) * res)) for x in range(-tx - 1, txy)]; display.flip()

# Dispersion of the mines.
for i in range(mines):
	idx = h.pop(h.index(random.choice(h)));pt[idx] = 'M'
	for i in -tx - 1, -tx, -tx + 1, -1, 1, tx - 1, tx, tx + 1:
		try:pt[idx + i] += 1 
		except:pass


## Game Loop ##

tps = 0
time.set_timer(USEREVENT,1000)

while True:
# Clicking on a box.
	e = event.wait()
	if e.type == MOUSEBUTTONDOWN:
		p = Rect((mouse.get_pos()), (1, 1)).collidelist(rects)
		if e.button == 1:

# Ending the game if a mine is clicked.
			if pt[p] == 'M':
				for i in range(txy):
					if pt[i] == 'M':screen.blit(boom,rects[i])
					elif pt[i] != 'x':screen.blit(img_list[pt[i]], rects[i])
				break

# If an empty box, show the adjacent boxes.
			elif pt[p] != 'x':
				if pt[p] == 0:
					temp.append(p)
					screen.blit(BACKGROUND, rects[p].topleft, rects[p])
					screen.blit(img_list[0], rects[p].topleft)
					pt[p] = 'x';empty -= 1
					while temp:
						i = temp.pop()
						for j in -tx,-1, 1, tx, -tx - 1, -tx + 1, tx - 1,tx + 1:
							if pt[i + j] == 0:temp.append(i + j)
							if pt[i + j] != 'x':
								screen.blit(BACKGROUND, rects[i + j].topleft, rects[i + j])
								screen.blit(img_list[pt[i + j]], rects[i + j].topleft);pt[i + j] = 'x'; empty -= 1
				else:
					screen.blit(BACKGROUND, rects[p].topleft, rects[p])
					screen.blit(img_list[pt[p]], rects[p].topleft);pt[p] = 'x';empty -= 1

# If all but the mines are revealed, then the game is finished.
				if not empty:
					for i in range(txy):
						if pt[i] == 'M':screen.blit(mine, rects[i])
					break

# Placing the flags.
		elif e.button == 3 and pt[p] != 'x':
			if p not in flags:
				screen.blit(flag, rects[p])
				flags.append(p)
			else:
				screen.blit(BACKGROUND, rects[p].topleft, rects[p]);screen.blit(deg, rects[p].topleft)
				flags.remove(p)
		display.flip()

	elif e.type == USEREVENT:
		tps += 1
		display.set_caption("minesweeper   " + str(tps / 3600).zfill(2) + ':' + str(tps / 60%60).zfill(2) + ':' + str(tps%60).zfill(2))

# Quitting the game.
	if e.type == QUIT:event.post(event.Event(QUIT)); break
display.flip()
while event.wait().type != QUIT:pass
