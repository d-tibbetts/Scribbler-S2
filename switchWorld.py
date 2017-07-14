from Myro import *

from Graphics import *

from math import *



#overridden functions for the user

def getLine():

    #print("custom get line")

    leftSensor = 0;

    rightSensor = 0;

    robot=getRobot()

    if robot != None:

        IR_Loc1 = [-12,5]

        IR_Loc2 = [-12,-5]

        loc = [robot.frame.getX(),robot.frame.getY()]

        theta = -1*radians(robot.frame.rotation)

        newIR_Loc1 = [cos(theta)*IR_Loc1[0] - sin(theta)*IR_Loc1[1] + loc[0],

                        sin(theta)*IR_Loc1[0] + cos(theta)*IR_Loc1[1] + loc[1]]

        newIR_Loc2 = [cos(theta)*IR_Loc2[0] - sin(theta)*IR_Loc2[1] + loc[0],

                        sin(theta)*IR_Loc2[0] + cos(theta)*IR_Loc2[1] + loc[1]]

        #newIR_Loc1 = [cos(theta)*IR_Loc1[0] - sin(theta)*IR_Loc1[1],

        #                sin(theta)*IR_Loc1[0] + cos(theta)*IR_Loc1[1]]

        #newIR_Loc2 = [cos(theta)*IR_Loc2[0] - sin(theta)*IR_Loc2[1],

        #                sin(theta)*IR_Loc2[0] + cos(theta)*IR_Loc2[1]]

        sim=getSimulation()

        for s in sim.window.canvas.shapes:

            if s.ToString().find("Picture") != -1 and s.tag=="Tile":

                if s.hit(newIR_Loc1[0],newIR_Loc1[1]):

                    r,g,b,a=s.getRGBA(newIR_Loc1[0],newIR_Loc1[1])

                    if r==0 and g==0 and b==0 and a==255:                    

                        leftSensor = 1

                if s.hit(newIR_Loc2[0],newIR_Loc2[1]):

                    r,g,b,a=s.getRGBA(newIR_Loc2[0],newIR_Loc2[1])

                    if r==0 and g==0 and b==0 and a==255:

                        rightSensor = 1

                

    else:

        print("no robot for getline")

    return [rightSensor,leftSensor]

    

'''

sim = Simulation("lineWorld", 700, 700, Color("white"))



robot=makeRobot("SimScribbler", sim)

robot.frame.outline=makeColor(0,0,0,0)

robot.setPose(375,675,-90)

 

sim.setup

'''



# create and name world; give window size, and background color

sim = Simulation("My World", 695, 273, Color("white"))



# walls for sim world; top left of rectanlge coordinate by bottom right rectangle coordinate

sim.addWall((0, 0), (10, 273), Color("blue"))

sim.addWall((10, 0), (695, 10), Color("blue"))

sim.addWall((685, 10), (695, 90), Color("blue"))

sim.addWall((685, 170), (695, 273), Color("blue"))

sim.addWall((0, 263), (695, 273), Color("blue"))



#name robot and put it in "sim" world

r=makeRobot("SimScribbler", sim)



# set robot position; x, y coordinates, way robot is facing by degree 0=horizontal with front facing east

r.setPose(35,135,0)



# picture of line to load into sim for line following, must draw line in paint and save as .png file

# or line function will not work

# change p=Picture("name of your file.png") and nothing else

p=Picture("seqPicture.png")

p.draw(sim.window)

p.tag="Tile"

p.stackOnBottom()



sim.setup()
#Defining Switch statements in python with a dictionary
#there is not a case statement in python.



def spin(): #bot spins around 360 degrees.
    for counter in range (0,4):
        turnBy(90)
    
def playSong():
    s=readSong("chariot.txt")
    r.playSong(s)
        

# function that will make the robot beep if it is called and a line

# is detected

def beepLine():

    # left and right must be initialized like this for use
    left, right = getLine()
    

    if left==1 and right==1:
        print("Line was detected. Beep!")
        #beep(1, 300)
        return True
    else:
        print("No line was detected. Stay Silent")
        return False
        
#these are the actions performed by the bot depending on the value
#of the counter
actions = {
        1: [playSong],
        2: [spin],
        3: [spin, playSong,spin]     
        }
        
#this is the function that will perform those actions.        
def botPerform(func_list):
    for f in func_list:
        f() 
        
          
def stuff():
    wait(5)
    counter = 1;  #counter for switch statement
    while(counter <=3): #will run till 3 lines are found.
        forward(1, 1)
        if(beepLine()):
            #calls the botPerform with the value of the counter in the dictionary
            botPerform(actions[counter])
            counter = counter + 1;
            #will move off the line current line. 
            while(beepLine()):
                forward(1,1)
        else:
            forward(1,1)
            
            
stuff()            
   
