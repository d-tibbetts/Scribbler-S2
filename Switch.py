from Myro import *
import random
init("COM5")

def spin(): #bot spins around 360 degrees.
    for counter in range (0,4):
        turnBy(90)
    
def robotPlaySong():
    s=readSong("chariot.txt")
    playSong(s)
        

# function that will make the robot beep if it is called and a line
# is detected

def beepLine():

    # left and right must be initialized like this for use
    left, right = getLine()
    print(left, right)

    if left==1 and right==1:
        print("Line was detected. Beep!")
        #beep(1, 300)
        return True
    if left == 0 and right ==1:
        print("Line detected")
        return True
    if left == 1 and right ==0:
        print("Line detected")
        return True 
    else:
        print("No line was detected. Stay Silent")
        return False
        
#lines on the printable tracks may not line up correctly or 
#the robot may drift off course, so a some function that allows 
#the robot to adjust and find the line may be necessary
def adjust():
    turnTo(270)
    backward(1,1)
    left, right = getLine()
    #test in a 30 degreen arc ( 15 to each side)
    '''while(left == 1 and right == 0 or left == 0  and right == 1):
        turnTo(270)
        if left==0 and right==1:
            
            for counter in range(0,-15,-5):
                turnBy(counter)
                left,right = getLine()
                if(left == 1 and Right ==1):
                    #backward(200,1)
                    break;
             
        if left==1 and right==0:
            for counter in range(0,15, 5):
             turnBy(counter)
             left,right = getLine()
             if(left == 1 and right == 1):
                #backward(200,1)
                break;'''
     
                
              #choose a random direction because we don't know where 
              #the line is.  right = 0 left =1
    direction = random.choice([0,1])
    if direction == 1:
        for counter in range(0, -15,-5):
            turnBy(counter)
            left, right = getLine()
            if(left == 1 or right == 1):
                #backward(1,1)
                break;
    if direction ==0: 
        for counter in range(0,15, 5):
            turnBy(counter)
            left,right = getLine()
            if(left == 1 or right == 1):
                #backward(10,1)
                break;
           

'''def findLine():
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
            break    '''                
#these are the actions performed by the bot depending on the value
#of the counter
actions = {
        2: [spin],
        1: [robotPlaySong],
        3: [spin, robotPlaySong,spin]     
        }
        
#this is the function that will perform those actions.        
def botPerform(func_list):
    for f in func_list:
        f() 
        
          
def stuff():
    
    backward(200, 1)
    counter = 1;  #counter for switch statement
    while(counter <=3): #will run till 3 lines are found.
        
        if(beepLine()):
            stop()
            #calls the botPerform with the value of the counter in the dictionary
            botPerform(actions[counter])
            if(counter == 2 or counter == 3):
                #adjustment for spins
                turnBy(-10)
                
            counter = counter + 1
            print("The counter is ", counter)
            backward(202,1)
        else:
            adjust()
        
            
            
            
            
stuff()         
#robotPlaySong()   