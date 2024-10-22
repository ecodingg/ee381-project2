#Eden Doss-Fillmore
#Project 2
#https://github.com/ecodingg/ee381-project2 - GitHub link


import random
import numpy as np

#Problem 1 - DONE
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

    if ((signalS == 0 and t <= e0) or (signalS == 1 and t > e1)):
        signalR = 1
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0

    if(signalR != signalS):
        return True
    else:
        return False

#Problem 2 - DONE
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

    if ((signalS == 0 and t <= e0) or (signalS == 1 and t > e1)):
        signalR = 1
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0

    if(signalR == signalS):
        return True
    else:
        return False

#Problem 3 - DONE
def prob3() -> bool:
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

    if ((signalS == 0 and t <= e0) or (signalS == 1 and t > e1)):
        signalR = 1
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0

    if(signalR != signalS):
        return False
    else:
        return True

#Problem 4 - WIP
def prob4() -> bool:
    #Variables
    p0 = 0.4
    e0 = 0.02
    e1 = 0.015
    rSignals = []
    signalD = None


    for r in range(3):
        m = random.uniform(0.00, 1.00)
        t = random.uniform(0.015, 0.02)
        
        #Assign Variable S
        if(m <= p0):
            signalS = 0
        else:
            signalS = 1
        
        if ((signalS == 0 and t <= e0) or (signalS == 1 and t > e1)):
            r = 1
            rSignals.append(r)
        elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
            r = 0
            rSignals.append(r)

    rSum = np.sum(rSignals)

    if(3.00 >= rSum >= 1.5):
        signalD = 1
    else:
        signalD = 0

    if(signalD == None):
        return True
    else:
        return False

#Main function
def main():
    #Problem 1 - Done
    count = 0
    for i in range(10000):
        result = prob1()
        if(result == False):
            count += 1

    print("Problem 1: p =",count, "/ 10000 = ", (count/10000))

    #Problem 2 - Done
    count = 0
    for i in range(100000):
        result = prob2()
        if(result == True):
            count+=1

    print("Problem 2: p =",count,"/ 100000 = ", (count/100000))

    #Problem 3 - Done
    count = 0
    for i in range(10000):
        result = prob3()
        if(result == True):
            count+=1

    print("Problem 3: p =",count,"/ 10000= ", (count/10000))

    #Problem 4 - WIP
    count = 0
    for i in range(10000):
        result = prob4()
        if(result == True):
            count += 1
    
    print("Problem 4: p =",count,"/ 10000= ", (count/10000))   
    
#Calls this to run
main()
