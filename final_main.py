#Duncan Craine
#Final Project
#Free fall simulation + bounce
#12/7/22

from graphics import *

from random import *

from ButtonClass import *
#Button CLass was updated to include color
#Has an undraw method called delete()
#Got rid of activate and deactivate due to not needed buttons to stay

from time import *



class Freefall:
    def __init__(self, mass): #chooses color based on mass
        if mass == 10:
            self.color = 'red'
        elif mass == 15:
            self.color = 'blue'
        else: #mass == 20
            self.color = 'green'


    def xBounce(self, xVel): #bounce of the wall
        return (xVel*-0.9) #change direction and reduce xVel by 10%

    def yBounce(self, yVel): #bounce off the floor
        if yVel < 100: #if the bounce isn't big enough, start "rolling"
            return 0 #will start "rolling"
        else:
            return (yVel * -0.95) #change direction and reduce yVel by 5%

def main():

    #create window
    win = GraphWin("Freefall Sim", 600, 600)
    win.setBackground("light gray")


    #make a welcome screen to get some of these variables
    welcome = Text(Point(300,200), "Welcome to this Freefall simulation \
with bounces. \n \n \n Click on your desired mass to begin")
    welcome.draw(win)

    label = Text(Point(300,400), "Enter a positive intial x velocity in meters per second")
    xVelEnt = Entry(Point(300, 500), 10)
    xVelEnt.setText("100")
    label.draw(win)
    xVelEnt.draw(win)

    #mass buttons
    mass10 = Button(win, Point(150,300), 80, 40, "10 kg", "red")
    mass15 = Button(win, Point(300,300), 80, 40, "15 kg", "blue")
    mass20 = Button(win, Point(450,300), 80, 40, "20 kg", "green")

    pt = win.getMouse()
    #click mass to begin
    while (mass10.isClicked(pt) == False and mass15.isClicked(pt) == False and mass20.isClicked(pt) == False):
        pt = win.getMouse()

    if mass10.isClicked(pt) == True:
        mass = 10
    elif mass15.isClicked(pt) == True:
        mass = 15
    else:
        mass = 20

    mass10.delete()
    mass15.delete()
    mass20.delete()

    welcome.undraw()
    label.undraw()
    xVelEnt.undraw()
    
    #constants
    height = 550
    radius = 25
    fps = 60
    time = 0
    yPos = 600-height #takes into account the inversion of the y-axis
    xPos = 50 #initial xPos
    xVel = int(xVelEnt.getText()) #gets xVel
    yVel = 0
    wait = 0

    #create ball
    sim = Freefall(mass)
    ball = Circle(Point(xPos, yPos), radius)
    ball.setFill(sim.color)
    ball.draw(win)
    #mass label
    label = Text(Point(xPos, yPos), (str(mass) + "kg"))
    label.draw(win)



    
    while not(yVel == 0 and yPos > 560): #until it starts "rolling"
        
        time += (1/fps) #advance one frame
        yVel += (time*9.8)
        dY = yVel/fps
        yPos += dY
        dX = xVel/fps
        xPos += dX
        ball.move(dX,dY)
        label.move(dX,dY) #moves mass label with ball

        if xPos >= 575 or xPos <= 25:
            xVel = sim.xBounce(xVel)

        elif yPos >= 575 and wait <=0:
            yVel = sim.yBounce(yVel) 
            wait = 2 #prevents multiple bounces from occuring in consecutive frames
            
        else:
            wait -= 1

        sleep(1/fps) #maintains framerate and therefore time counting
        


    
    while abs(xVel) > 5: #rolling until barely moving
        time += (1/fps) #advance one frame
        dY = 0
        xVel *= .98 #slowly come to a stop
        dX = xVel/fps
        xPos += (dX)
        ball.move(dX,dY)
        label.move(dX,dY)

        if xPos >= 575 or xPos <= 25:
            xVel = sim.xBounce(xVel)
        

        sleep(1/fps)

    #quitButton
    quitButton = Button(win, Point(300,300), 200, 100, "QUIT", "red")

    pt = win.getMouse()
    #click quit to end
    while (quitButton.isClicked(pt) == False):
        pt = win.getMouse()
    win.close()

        
            
main()
