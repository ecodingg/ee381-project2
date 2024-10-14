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
def prob4(n) -> bool:
    #Variables
    p0 = 0.4
    e0 = 0.02
    e1 = 0.015
    signalS = n
    r1,r2,r3 = 0
    rSignals = [r1, r2, r3]
    signalD = None
    m = random.uniform(0.00, 1.00)
    t = random.uniform(0.015, 0.02)


    for r in rSignals:
        if ((signalS == 0 and t <= e0) or (signalS == 1 and t > e1)):
            r = 1
        elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
            r = 0

    rSum = np.sum(rSignals)

    if(3.00 >= rSum >= 1.5):
        signalD = 1
    else:
        signalD = 0

    if(signalD == None):
        return False
    else:
        return True

#Main function
def main():
    #Problem 1
    count = 0
    for i in range(10000):
        result = prob1()
        if(result == False):
            count += 1

    print("Problem 1: p =",count, "/ 10000 = ", (count/10000))

    #Problem 2
    count = 0
    for i in range(100000):
        result = prob2()
        if(result == True):
            count+=1

    print("Problem 2: p =",count,"/ 100000 = ", (count/100000))

    #Problem 3
    count = 0
    for i in range(10000):
        result = prob3()
        if(result == True):
            count+=1

    print("Problem 3: p =",count,"/ 10000= ", (count/10000))

    #Problem 4
    count = 0
    sInput = input(print("Input S number: "))
    for i in range(10000):
        result = prob4(sInput)
        if(result == True):
            count += 1
    
    print("Problem 4: p =",count,"/ 10000= ", (count/10000))   
    

main()
