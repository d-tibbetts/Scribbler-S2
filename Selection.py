from Myro import *
init("COM3")

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
            while(beepLine()):
                backward(1,.5)    
            counter = counter + 1
            print("The counter is ", counter)
            backward(202,1)
        
            
            
            
            
stuff()         
