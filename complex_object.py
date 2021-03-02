# Caroline Ninganga
# CS 5001 
# Project 5 1st submission

import graphicsPlus as gr

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

    win.getMouse()
    win.close()

def draw( shapes, win ):

    for thing in shapes:
        thing.draw( win )


if __name__ == "__main__":
    test_man()