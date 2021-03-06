from Myro import *
init("COM5")

#This function allows the S2 to search for line 
#The robot still needs to be in the general vicinity of the 
#line.  This is the same findLine function found in the simulated version
#lineWorld.py  
def findLine():
    speed=.5
    while True:
        left,right=getLine()
        print(left,right)
            
        if left==0 and right==0:
            print("Searching for line")
            backward(speed,.2)
        if left==1 and right==1:
            print("Line found")
            break   
        elif left==1 and right==0:
            print("Line found")
            break   
        elif left==0 and right==1:
            print("Line found")
            break    
findLine()



# This function allows the robot to follow a line using the S2's 
#onboard line sensor.  This version uses both sensors to locate the line
#instead of 1 to follow an edge.  There is a similar version in the simulated version 
#lineWorld.py
def followLine():
    endOfPath = False
    while not endOfPath:
        left,right=getLine()
        print(left,right)
    
        while left==1 and right==1: 
             backward(.2,.5)
             left,right = getLine()
        while left==0 and right==1:
             turnRight(.1,.2)
             left,right = getLine()
             lastSensorZero = "left"
        while left==1 and right==0:
             #stop()
             turnLeft(.1,.3)
             left,right = getLine()
             lastSensorZero = "right"
        if left ==0 and right == 0:
            leftLight,centerLight,rightLight=getLight()
            print(leftLight,centerLight,rightLight)
            if centerLight <= 3500:
                endOfPath = True;
                print(leftLight,centerLight,rightLight)
                break
            while(left == 0 and right == 0):
                if lastSensorZero == "right":
                    forward(.2, .5)
                    turnLeft(.1,.2)
                    lastSensorZero == "left"
                    left, right = getLine()
                    break;
                elif lastSensorZero == "left":
                    forward(.2,.5)
                    turnRight(.1,.2)
                    lastSensorZero == "right"
                    left, right = getLine()
                    break;   
           
             
        
          
followLine()
#This function allows the S2 to find a light source (set at the end of the line maze)
# after the line maze has been completed. This function is also found in the simulated version 
#lineWorld.py
def followLight():
    speed = .5
    while True:
        leftLight,centerLight,rightLight=getLight()
        print(leftLight,centerLight,rightLight)
        if leftLight < centerLight:
            print("Should be turning left")
            turnLeft(speed,0.5)
        elif rightLight < centerLight:
            print("Should be turning right")
            turnRight(speed,0.4)
        elif centerLight < leftLight and centerLight < rightLight:
            backward(speed,0.4)
            print("Should be heading to the light")
            if centerLight <= 2500:
                print("completed maze")
                stop()
                break
        else:
            print("Should be turning left")
            turnLeft(speed,0.5)
followLight()

#findLine()
#followLine()
#followLight()