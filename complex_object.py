# Caroline Ninganga
# CS 5001 
# Project 5 1st submission

import time 
import random
import graphicsPlus as gr

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

# define the test man function which asigns the different sizes and locations of the man it also calls the draw function passing two arguments
def test_man():
    win = gr.GraphWin( "My window", 1500, 1500 )
    
    man1 = init_man(300, 300, 1)
    man2 = init_man(250, 250, 0.5)
    man3 = init_man(400, 400, 2)

# The draw function which carries two arguments, first is the sun1 which is the list of zelle shapes which makes objects
    draw(man1, win)
    draw(man2, win)
    draw(man3, win)

    for i in range(100):
        if win.checkMouse() != None: 
            break
        elif win.checkKey() == 'q':
            break
        animate_man(man1, i, win)
        animate_man(man2, i, win)
        animate_man(man3, i, win)


        win.update() # at each iteration the window has to update
        time.sleep(0.1) # tells the loop to pause for a tenth of a second, meaning that ten loops is roughly one second of animation time.


    win.getMouse()
    win.close()

def animate_man( shapes, frame_num, win ): # shapes is equal to the man list returned in init_man
    # added some movement to the man 
    if frame_num < 50:
        move( shapes, 1, 0)
    else:
        move( shapes, -1, 0)

def draw( shapes, win ):

    for thing in shapes:
        thing.draw( win )

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

# define the test sun function which asigns the different sizes and locations of the sun it also calls the draw function passing two arguments
def test_sun():
    win = gr.GraphWin( "My window", 1500, 1500 )

    sun1 = init_sun(300, 300, 1)
    # sun2 = init_sun(250, 2500, 0.5)
    # sun3 = init_sun(400, 400, 2)
# The draw function which carries two arguments, first is the sun1 which is the list of zelle shapes which makes objects
    draw(sun1, win)
    # draw(sun2, win)
    # draw(sun3, win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    test_man()