#Eden Doss-Fillmore
#Project 2
import random

#Problem 1 - WIP
def prob1() -> bool:
    #Variables
    p0 = 0.4
    e0 = 0.02
    e1 = 0.015
    signalS = 0
    signalR = 0
    m = random.uniform(0.00, 1.00)
    t = random.uniform(0.015, 0.02)
    
    #Assign Variable S
    if(m <= p0):
        signalS = 0
    else:
        signalS = 1

    if ((signalS == 0 and t <= e1) or (signalS == 1 and t > e1)):
        signalR = 1
        return True
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0
        return False

#Problem 2 - WIP
def prob2() -> bool:
    #Variables
    p0 = 0.4
    e0 = 0.02
    e1 = 0.015
    signalS = 0
    signalR = 0
    m = random.uniform(0.00, 1.00)
    t = random.uniform(0.015, 0.02)
    
    #Assign Variable S
    if(m <= p0):
        signalS = 0
    else:
        signalS = 1

    if ((signalS == 0 and t <= e1) or (signalS == 1 and t > e1)):
        signalR = 1
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0

    if(signalR == signalS):
        return True
    else:
        return False

#Problem 3 - N/A
def prob3() -> bool:
    print("eh")

#Problem 4 - N/A
def prob4() -> bool:
    print("uh")

def main():
    #Problem 1
    count = 0
    for i in range(10000):
        result = prob1()
        if(result == False):
            count += 1
            
    print("Problem 1: p=",count, "/10,000")

    #Problem 2
    count = 0
    for i in range(100000):
        result = prob2()
        if(result == True):
            count+=1
    
    print("Problem 2: p=",count,"/100,000")

    #Problem 3

    #Problem 4
   
main()