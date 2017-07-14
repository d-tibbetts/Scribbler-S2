from Myro import * #Simulation, makeRobot
from Graphics import *
####################################DO NOT EDIT###########################################
#This is the code for the simulator Do not edit this code 
#This puts your Robot in the correct position in the simulator..
indoor = Simulation(("Initials World"), 600,500, Color("white"))

indoor.addWall((0,0), (10,500), Color("red"))
indoor.addWall((0,0), (600,10), Color("red"))
indoor.addWall((0,490), (600,500), Color("red"))
indoor.addWall((590,0), (600,500), Color("red"))




indoor.setup() # starts simulator thread
makeRobot("SimScribbler", indoor)
indoor.setPose(0, 100, 300, -90)
#########################################################################################
#This is the Demo Code for the Draw initials ....
penDown()# takes a color parameter ie: "red" , "green" empty is default black
#back of D
forward(5,.5)
forward(5,.5)
turnTo(270)
forward(5,.5)
forward(5,.5)
#stop()
#bottom of D
turnTo(0)
forward(6,.5)
stop()
#Front of D
turnTo(90)
forward(5,.5)
forward(5,.5)
stop()
#top of D
turnTo(180)
forward(6,.5)
stop()
turnTo(270)
forward(5,.5)
forward(5,.5)
turnTo(0)
forward(7,.5)


#back of E
turnTo(90)
forward(5,.5)
forward(5,.5)
turnTo(270)
forward(5,.5)
forward(5,.5)
#bottom of E
turnTo(0)
forward(5,.5)
turnTo(180)
forward(5,.5)
#middle of E
turnTo(90)
forward(5,.5)
turnTo(0)
forward(5,.5)
turnTo(180)
forward(5,.5)
#top of E
turnTo(90)
forward(5,.5)
turnTo(0)
forward(5,.5)
turnTo(180)
forward(5,.5)
turnTo(270)
forward(5,.5)
forward(5,.5)
turnTo(0)
forward(9,.5)

#Middle of T
turnTo(90)
forward(5,.5)
forward(5,.5)
#Top Left
turnTo(180)
forward(5,.5)
#Top Right
turnTo(0)
forward(5,.5)
forward(5,.5)
