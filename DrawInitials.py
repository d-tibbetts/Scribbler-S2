from Myro import *
init("COM3")

#This function allows the robot to signal when a letter is complete 
#and it is ready to be moved into position for the next letter
def readyNextLetter():
    s=readSong("charge.txt")
    playSong(s)
    wait(10)
    
    
def D(): 
    forward(50,1)
    #Top of D
    turnBy(-90)
    forward(10,.5)
    #Front of D
    turnBy(-90)
    forward(50,1)
    #Bottom of D
    turnBy(-90)
    forward(10,.5)
    
    readyNextLetter()
    
def E(): 
    #base of E
    forward(50,1)
    #Top of E
    turnBy(-90)
    forward(10,.5)
    turnBy(180)
    forward(10,.5)
    
    #middle of E
    turnBy(90)
    forward(10,.5)
    turnBy(90)
    forward(10,.5)
    turnBy(180)
    forward(11,.5)
    
    #bottom of E
    turnBy(90)
    forward(10,.5)
    turnBy(90)
    forward(10,.5)
    
    
    readyNextLetter()

def T():
    #middle of T
    forward(50,1)
    turnBy(90)
    #Top of T
    forward(11,.5)
    turnBy(-180)
    forward(11,.5)
    forward(11,.5)
    
def drawName():
    D()
    E()
    T()
    
    


def main():
    drawName()
main()


