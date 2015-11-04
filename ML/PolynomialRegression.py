'''
Polynomial Regression
Created on 2015/10/30/
@author: Alan HUANG
'''
import tools
import math
import random
import numpy as np
import matplotlib.pyplot as pl

def generateXY():
    X = []
    Y = []
    
    x = 0
    while(x<2*math.pi):
        y = math.sin(x) + random.uniform(-0.2,0.2)
        X.append(x)
        Y.append(y)
        x += random.uniform(0.5,1)
    '''    
    for i in range(10):
        x = random.uniform(0,2*math.pi)
        y = math.sin(x) + random.uniform(-0.2,0.2)
        X.append(x)
        Y.append(y)
    '''
    return (X,Y)

def initializeTHETA(power):
    THETA = []
    for i in range(power+1):
        #THETA.append(random.random())
        THETA.append(0)
    return THETA

def hypothesis(x,THETA):
    h = 0
    for i in range(len(x)):
        h += THETA[i]*x[i]
    return h    
    
def formDataSet(x,power):
    X = []
    for m in range(len(x)):
        row = []
        for i in range(power+1):
            row.append(x[m]**i)
        X.append(row)
    return X

        
def traning(X,Y,THETA,alpha):
    times = 0
    PD = derivative(THETA, X, Y)
    
    while max(np.absolute(PD))>0.001:
        for i in range(len(THETA)):
            THETA[i] = THETA[i]-alpha*PD[i]
        PD = derivative(THETA, X, Y)
        times += 1
    print("used",times,"times to train the parameter THETA")
    return THETA

def derivative(THETA,X,Y):
    PD = [] #partial derivative
    for j in range(len(THETA)): #对每一个θ求偏导
        add = 0
        for m in range(len(X)):  #m条训练记录
            add += (hypothesis(X[m], THETA)-Y[m])*X[m][j]
        PD.append(add/len(X))
    print("partial derivative is:",PD)
    return PD

def computeY(x,THETA):
    Y = []
    dataX = formDataSet(x, (len(THETA)-1))
    for row in dataX:
        Y.append(hypothesis(row, THETA))
    return Y

def computeY_scaling(x,THETA,x_mean,x_std):
    Y = []
    dataX = formDataSet(x, (len(THETA)-1))
    
    for row in dataX:
        for i in range(len(row)):
            if x_std[i] == 0:
                row[i] = 1
            else:
                row[i] = float((row[i]-x_mean[i])/x_std[i])
    
    for row in dataX:
        Y.append(hypothesis(row, THETA))
    return Y
    
def test_noScaling():
    #准备数据
    power = 3
    XY = generateXY()
    pl.scatter(XY[0],XY[1])
    
    X = formDataSet(XY[0], power)
    Y = XY[1]
    
    THETA = initializeTHETA(power)
    #最大的学习率
    alpha = 0.0001 
    
    #训练
    THETA = traning(X, Y, THETA, alpha)
    print("trained theta is:",THETA)
    
    #画sin的图
    linX = np.linspace(0,2*math.pi,num=100)
    linY = np.sin(linX)
    pl.plot(linX,linY)
    
    #画生成的曲线的图
    pl.plot(linX,computeY(linX,THETA))
    pl.legend(["sin","hypothesis"])

def test_withScaling():
    #准备数据
    power = 3
    XY = generateXY()
    pl.scatter(XY[0],XY[1])
    
    X = formDataSet(XY[0], power)
    Y = XY[1]
    
    sceledResult = tools.scaling(X)
    scaledX = sceledResult[0]
    x_mean = sceledResult[1]
    x_std = sceledResult[2]
    
    THETA = initializeTHETA(power)
    alpha = 0.3 #
    
    #训练
    THETA = traning(X, Y, THETA, alpha)
    print("trained theta is",THETA)
    
    #画sin的图
    linX = np.linspace(0,2*math.pi,num=100)
    linY = np.sin(linX)
    pl.plot(linX,linY)
    
    #画生成的曲线的图
    pl.plot(linX,computeY_scaling(linX,THETA,x_mean,x_std))
    pl.legend(["sin","hypothesis"])

if __name__ == "__main__":
    #test_noScaling()
    test_withScaling()
    pl.show()

    
    
        
    
    