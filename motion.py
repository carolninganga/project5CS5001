# Caroline Ninganga
# CS 5001
# 02/26/2021
# Project 5 


# import the time, random and graphicsPlus packages
import time
import random
import graphicsPlus as gr

def draw( shapes, win ):
    """ Draw all of the objects in shapes in the window (win) """
    # for each thing in shapes
    for item in shapes:
        item.draw( win )
        # call the draw method on thing with win as the argument
def move( shapes, dx, dy ):
    """ Draw all of the objects in shapes by dx in the x-direction
    and dy in the y-direction """
    # for each item in shapes
    for item in shapes:
        item.move( dx, dy)
        # call the move method on item with dx and dy as arguments
def undraw( shapes ):
    """ Undraw all of the objects in shapes """
    # for each thing in shapes
    for item in shapes:
        item.undraw()
        # call the undraw method on thing

# create a flying saucer from a circle and two ovals and return a list containing the basic shapes.
def init_saucer(x, y, scale):

# Assign to light a Circle object at (x, y-20*scale) with radius 4*scale.  
    light = gr.Circle( gr.Point( x, y-20*scale ), 4*scale )
# Then set its color to (220, 100, 110). Remember to use a gr.Point.
    light.setFill(gr.color_rgb( 220, 100, 110))

# Assign to body an Oval object with corners at (x-30*scale, y-20*scale) and (x+30*scale, y+20*scale). 
    body = gr.Oval( gr.Point( x-30*scale, y-20*scale ), gr.Point( x+30*scale, y+20*scale ))
# Set its color to (220, 210, 220).
    body.setFill(gr.color_rgb( 220, 210, 220))

# Assign to saucer an Oval object with corners at (x-60*scale, y-5*scale) and (x+60*scale, y+5*scale).
    saucer = gr.Oval( gr.Point( x-60*scale, y-5*scale), gr.Point(x+60*scale, y+5*scale))
# Set its color to (240, 230, 190).
    saucer.setFill(gr.color_rgb(240, 230, 190))

# Return a list containing light, body, and saucer, in that order
    flying_saucer = [ light, body, saucer ]
    return flying_saucer


# This function will take two arguments, the first is a list of graphics object creating the saucer.
# The second argument, frame_num, will be the number of the frame in the animation. The final argument, win, will be the 
# GraphWin window into which the saucer has been drawn.
def animate_saucer( shapes, frame_num, win ): # shapes is equal to flying saucer list returned in init_saucer
    # added some movement to the saucer
    if frame_num < 50:
        move( shapes, -1, -1)
    else:
        move( shapes, 1, 1)

    if frame_num == 70:
        mid = shapes[0].getCenter()
        radius = shapes[0].getRadius()
        scale = radius/4 
        beam = gr.Polygon ( gr.Point(mid.getX() - scale*4, mid.getY() + scale*40), gr.Point (mid.getX() + scale*4, mid.getY() + scale*40), 
        gr.Point(mid.getX() + scale*15, mid.getY() + scale*110), gr.Point(mid.getX() - scale*15, mid.getY() + scale*110))
        beam.setFill(gr.color_rgb(255, 255, 180))
        beam.draw( win)
        shapes.append(beam)
        
    if frame_num == 90:
        beam = shapes.pop()
        beam.undraw()
    # In animate_saucer, if the frame_num % 20 is equal to 0, set the fill color of the light (the first element in shapes list) to blue, 
    # else if the frame_num % 20 is equal to 10, set the light's color to red.
    light = shapes[0]
    if frame_num % 20 == 0:
        light.setFill( 'blue')
    elif frame_num % 20 == 10:
        light.setFill( 'red')


def main():
    # make a window, add a 4th argument False, which halts automatic updating
    win = gr.GraphWin( "Saucer", 400, 400, False )
    
    # create the saucer shape list
    saucer1 = init_saucer(200, 200, 0.5)
    saucer2 = init_saucer(300, 300, 0.75)
    saucer3 = init_saucer(100, 100, 1)


    scene = [ saucer1, saucer2, saucer3 ]

    for saucer in scene:
        draw( saucer, win)
        
    # draw each item in the saucer shape list

    for i in range(100):
        if win.checkMouse() != None: 
            break
        elif win.checkKey() == 'q':
            break
        animate_saucer(saucer1, i, win)
        animate_saucer(saucer2, i, win)
        animate_saucer(saucer3, i, win)

        win.update() # at each iteration the window has to update
        time.sleep(0.1) # tells the loop to pause for a tenth of a second, meaning that ten loops is roughly one second of animation time.

    # update the window (draw things) and wait for a mouse click
    win.update()
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()