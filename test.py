# Caroline Ninganga
# CS 5001
# Project 4
# Man on a ship

import graphicsPlus as gr
import time
import random

import sys

# 
def move( shapes, dx, dy ):
    """ Draw all of the objects in shapes by dx in the x-direction
    and dy in the y-direction """
    # for each item in shapes
    for item in shapes:
        item.move( dx, dy)

# def init_man defines the pool fucntion with three parameters x, y and scales
def init_man(x, y, scale):
    # define the man shapes and put them into a list

    # Head: Create a circle with the color brown
    head = gr.Circle( gr.Point ( x+scale*10, y-scale*50), 20*scale) 
    head.setFill('brown')

    # arms : Create a rectangle with the color blue for the arms
    arms = gr.Rectangle( gr.Point ( x+scale*110, y), gr.Point(x-scale*80, y-scale*30 ))
    arms.setFill('blue')

    # stomach : Create a rectangle with the color blue for the sh 
    stomach = gr.Rectangle( gr.Point ( x+scale*70, y+scale*60), gr.Point(x-scale*50, y ))
    stomach.setFill('blue')

    # # leg2 : Create a rectangle with the color red for pants
    leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 ))
    leg1.setFill('red')

    #   # leg2 : Create a rectangle with the color red for pants 
    leg2 = gr.Rectangle( gr.Point ( x+scale*60, y+scale*60), gr.Point(x+scale*40, y+scale*180 ))
    leg2.setFill('red')

  
    # man creates the list of all the basic shapes created by zelle
    man = [ head, arms, leg1, leg2, stomach ]
    return man



# def init_sun defines the pool fucntion with three parameters x, y and scales
def init_sun(x, y, scale):
     # create a circle with the sun
    inner_sun = gr.Circle( gr.Point ( x-scale*260, y-scale*200), 120*scale) 
    inner_sun.setFill('orange')

    outer_sun= gr.Circle( gr.Point ( x-scale*260, y-scale*200), 150*scale) 
    outer_sun.setFill('yellow')

    # leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 ))
    # leg1.setFill('red')

    
    sun = [ outer_sun, inner_sun ]
    return sun


# def init_pool defines the pool fucntion with three parameters x, y and scales
def init_pool(x, y, scale):

    # # diving board : Create a rectangle with the color brown 
    diving_board = gr.Rectangle( gr.Point ( x+scale*180, y+scale*180), gr.Point(x-scale*260, y+scale*250 ))
    diving_board.setFill('brown')

    # create a swiming pool with the color skyblue
    water = gr.Rectangle( gr.Point ( x+scale*780, y+scale*880), gr.Point(x-scale*260, y+scale*250 ))
    water.setFill('skyblue')

    # create a list of the complex shapes 
    pool = [  diving_board, water ]

    return pool


#  shapes is a list of zelle objects that make a complex shape
def draw( shapes, win ):

    for thing in shapes:
        thing.draw( win )

def animate_man( shapes, frame_num, win ): # shapes is equal to the man list returned in init_man
    # added some movement to the man 
    if frame_num < 50:
        move( shapes, 1, 0)
    else:
        move( shapes, -1, 0)

# draws the entire scene with man pool and sun 
def scene( argsList ): 
 
    # this is the graphics window
    win = gr.GraphWin( "My window", 1000, 1000 )

    # This controls the scale location and size of the scene
    x = 0
    y = 0
    scale = 1

    #only save command line args if they are proivded. This section allows the user to enter the specified arguments. 
    if len(argsList) == 4:
        x = int (argsList[1])
        y = int (argsList[2])
        scale = float (argsList[3])

    print(argsList)


    # draw the man into the window 
    man = init_man( x, y, scale)

    # draw the sun into the window
    sun = init_sun( x, y, scale)

    # draw the pool into the window
    pool = init_pool( x, y, scale)

    # line 22 to 24 call the draw function which draws the zelle shapes that draw the complex shapes 
    draw(man, win)
    draw(sun, win)
    draw(pool, win)

    for i in range(100):
        if win.checkMouse() != None: 
            break
        elif win.checkKey() == 'q':
            break
        animate_man(man, i, win)


        win.update() # at each iteration the window has to update
        time.sleep(0.1) # tells the loop to pause for a tenth of a second, meaning that ten loops is roughly one second of animation time.

    # pause until user gets mouse
    # c.undraw()

   
    # wait for a mouse click
    win.getMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    scene( sys.argv)

