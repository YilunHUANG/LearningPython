'''
Linear Regression
Created on 2015/10/24/
@author: Alan HUANG
'''

from matplotlib.pyplot import *
import numpy as np
from numpy import dtype
from scipy.constants.constants import alpha


def traning(X,Y,THETA,alpha):
    #THETA:parameter 
    #alpha:learning rate
    times = 0
    PD = derivative(THETA, X, Y)
    while abs(max(PD))>0.01:
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

def hypothesis(X,THETA):
    #对于单独的一组输入样本，给出预测
    #X: [1,2,3,4,5]
    #THETA: [1,2,3,4,5]
    
    h = 0
    for i in range(len(X)):
        h += X[i]*THETA[i]
    return h    
    
def draw2D(THETA,X,Y):#测试通过
    #在XY坐标平面上画出预测的直线，还有样本的散点

    #准备连续的点
    begin  = np.min(X)
    end = np.max(X)
    lineX = np.linspace(begin,end,256,endpoint=True)
    lineY = []
    for item in lineX:
        lineY.append(hypothesis((1,item), THETA))
    #准备散点
    scatterX = []
    scatterY = []
    for i in range(len(X)):
        scatterX.append(X[i][1])
        scatterY.append(Y[i])
    #画图    
    scatter(scatterX,scatterY) #画散点图
    plot(lineX,lineY) #画直线
    show()
 
def scaling(X):
    tempX = X
    x_mean = np.mean(tempX,axis=0)
    x_std = np.std(tempX,axis=0)
    for row in tempX:
        for i in range(len(row)):
            if x_std[i] == 0:
                row[i] = 1
            else:
                row[i] = float((row[i]-x_mean[i])/x_std[i])
    return tempX
     
def recoverTheta(THETA, X, scaledX):
    #not finished
    '''
    for 
    
    
    
    
    for i in range(len(THETA)):
        if x_std[i] == 0:
            THETA[i] = THETA[i]
        else:
            THETA[i] = THETA[i]*x_std[i]+x_mean[i]
    return THETA
    ''' 
 
#def normalEquation(X,Y):
     
def test1():  
    X = np.array([(1,65),(1,88),(1,95),(1,100),(1,130),(1,135)])
    Y = [320985,440652,482770,518200,680600,665978]
    THETA = [0,0]
    alpha = 0.001
    
    traning(X, Y, THETA, alpha)
    print(THETA)
    draw2D(THETA, X, Y)
    
def test2():
    #5个特征的情况（包含x0=1）
    X = np.array([[1,2104,5,1,45],[1,1416,3,2,40],[1,1534,3,2,30],[1,852,2,1,36]],dtype="f")
    Y = np.array([460,232,315,178],dtype="f")
    THETA = [0,0,0,0,0]
    alpha = 0.1
    
    scaledX = scaling(X)
    print(scaledX)
    traning(scaledX, Y, THETA, alpha)
    
    print(THETA)
    
def tempTest():
    #准备数据
    X = np.array([[1,65],[1,88],[1,95],[1,100],[1,130],[1,135]],dtype="f")
    Y = np.array([320985,440652,482770,518200,680600,665978],dtype="f")
    THETA = [0,0]
    alpha = 1
    #缩放数据，训练数据
    scaledX = scaling(X)
    traning(scaledX, Y, THETA, alpha)
    print("theta before recovering is",THETA)
    
    recoverTheta(THETA, X, scaledX)
    #print("the final theta is",THETA)
    draw2D(THETA, X, Y)
    
    
if __name__=="__main__":
    test2()