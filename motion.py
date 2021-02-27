# Caroline Ninganga
# CS 5001
# 02/26/2021
# Project 5 


# import the time, random and graphicsPlus packages
import time
import random
import graphicsPlus as gr

# this function should create a flying saucer from a circle and two ovals and return a list containing the basic shapes.
def init_saucer(x, y, scale):

# Assign to light a Circle object at (x, y-20*scale) with radius 4*scale.  
# Then set its color to (220, 100, 110). Remember to use a gr.Point.

Assign to body an Oval object with corners at (x-30*scale, y-20*scale) and (x+30*scale, y+20*scale). Set its color to (220, 210, 220).
Assign to saucer an Oval object with corners at (x-60*scale, y-5*scale) and (x+60*scale, y+5*scale). Set its color to (240, 230, 190).
Return a list containing light, body, and saucer, in that order

# Test code for the flying saucer
def main():
    # make a window, add a 4th argument False, which halts automatic updating
    win = gr.GraphWin( "Saucer", 400, 400, False )
    
    # create the saucer shape list
    saucer = init_saucer(200, 200, 2)
    # draw each item in the saucer shape list
    for item in saucer:
        item.draw(win)
    # update the window (draw things) and wait for a mouse click
    win.update()
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()