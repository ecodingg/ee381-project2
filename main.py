#Eden Doss-Fillmore
#Project 2
import numpy
import matplotlib
import pandas
import random


#Problem 1
def prob1() -> bool:
    #Variables
    p0 = 0.4
    e0 = 0.02
    e1 = 0.015
    signalS = 0
    signalR = 0
    m = random.uniform(0.00, 1.00)
    t = random.uniform(0.015, 0.02)
    result = True
    
    #Assign Variable S
    if(m <= p0):
        signalS = 0
    else:
        signalS = 1

    if ((signalS == 0 and t <= e1) or (signalS == 1 and t > e1)):
        signalR = 1
        result = True
        return result
    elif ((signalS == 0 and t > e0) or (signalS == 1 and t <= e1)):
        signalR = 0
        result = False
        return result

#Problem 2
def prob2():

    print("oh")

#Problem 3
def prob3():
    print("eh")

#Problem 4
def prob4():
    print("uh")

def main():
    count = 0
    for i in range(10,000):
        result = prob1()
        if(result == False):
            count += 1
    print(count)