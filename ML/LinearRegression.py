'''
Linear Regression
Created on 2015/10/24/
@author: Alan HUANG
'''

from matplotlib.pyplot import *
import numpy as np
from numpy import dtype


def traning(THETA,X,Y,alpha):
    '''THETA:parameter 
    alpha:learning rate'''
    
    PD = derivative(THETA, X, Y)
    while abs(max(PD))>0.01:
        for i in range(len(THETA)):
            THETA[i] = THETA[i]-alpha*PD[i]
        PD = derivative(THETA, X, Y)
    return THETA

def derivative(THETA,X,Y):
    PD = []
    for j in range(len(THETA)): #对每一个θ求偏导
        sum = 0
        for m in range(len(X)):  #m条训练记录
            unit = hypothesis(X[m], THETA)
            unit -= Y[m]
            unit *= X[m][j]
            sum += unit
        PD.append(sum/len(X))
    print(PD)
    return PD

def hypothesis(x,THETA):
    unit = 0
    for i in range(len(x)):
        unit += x[i]*THETA[i]
    return unit    
    
def draw2D(THETA,trainX,trainY):
    X = []
    Y = []
    x = np.linspace(50,150,256,endpoint=True)
    for point in x:
        X.append(point)
        Y.append(hypothesis((1,point), THETA))
     
    tempX = []
    for i in trainX:
        tempX.append(i[1])
         
    scatter(tempX,trainY)   
    plot(x,Y)
    
    show()
 
def normlize():
    x = np.array([[1,65],[1,88],[1,95],[1,100],[1,130],[1,135]],dtype="f")
    print(x)
    x_mean = np.mean(x,axis=0)
    print(x_mean)
    x_std = np.std(x,axis=0)
    print(x_std)
    for row in x:
        for i in range(1,len(row)):
            row[i] = float((row[i]-x_mean[i])/x_std[i])
    print(x)
    return x
     
 
#def normalEquation(X,Y):
     
def test1():  
    X = [(1,65),(1,88),(1,95),(1,100),(1,130),(1,135)]
    Y = [320985,440652,482770,518200,680600,665978]
    THETA = [0,0]
    alpha = 0.0001
    
    traning(THETA, X, Y, alpha)
    print(THETA)
    draw2D([178,5080], X, Y)
    
def test2():
    X = [(1,2104,5,1,45),(1,1416,3,2,40),(1,1534,3,2,30),(1,852,2,1,36)]
    Y = [460,232,315,178]
    THETA = [0,0,0,0,0]
    alpha = 0.00001
    
def tempTest():
    normlize()
    
    
if __name__=="__main__":
    test1()
    #tempTest()