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