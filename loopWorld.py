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
sim = Simulation("My World", 900, 800, Color("white"))

#light for sim world; coordinates, radius, color
sim.addLight((780, 85), 75, Color("yellow"))

# walls for sim world; top left of rectanlge coordinate by bottom right rectangle coordinate
sim.addWall((170, 195), (900, 280), Color("blue"))
sim.addWall((170, 280), (215, 430), Color("blue"))
sim.addWall((600, 280), (900, 430), Color("blue"))
sim.addWall((0, 530), (750, 625), Color("blue"))
sim.addWall((410, 385), (470, 530), Color("blue"))

sim.addWall((0, 0), (10, 800), Color("blue"))
sim.addWall((10, 0), (900, 10), Color("blue"))
sim.addWall((890, 195), (900, 800), Color("blue"))
sim.addWall((0, 790), (900, 800), Color("blue"))

#name robot and put it in "sim" world
r=makeRobot("SimScribbler", sim)

# set robot position; x, y coordinates, way robot is facing by degree 180=horizontal with front facing west
r.setPose(85,715,180)


# picture of line to load into sim for line following, must draw line in paint and save as .png file
# or line function will not work
# change p=Picture("name of your file.png") and nothing else
p=Picture("loopPicture.png")
p.draw(sim.window)
p.tag="Tile"
p.stackOnBottom()

sim.setup()

# function to make robot infinitly follow a line
def followLine():
	count=0
	speed=0.25
	while True:
		left,right=getLine()
		print(left,right)
		if left==1 and right==1:
			backward(speed,0.5)
			print("Should be following line")
		elif left==1 and right==0:
			print("Should be turning right")
			turnRight(speed,0.5)
		elif left==0 and right==1:
			print("Should be turning left")
			turnLeft(speed,0.5)
		else:
			print("Out of the line")
			count+=1
			if count==5:
				print("Line is done being followed. Let's see if we detect a light at the end")
				followLight()
				break
				
def followLight():
	left,middle,right=getLight()
	speed=0.75
	if left<=5000 or middle <=5000 or right<=5000:
		print("Light Detected!")
		while True:
			left,middle,right=getLight()
			backward(speed, 0.5)
			if left<=100 or middle<=100 or right<=100:
				print("Found the light!")
				break
	else:
		print("No light was detected")
wait(5)        
followLine()