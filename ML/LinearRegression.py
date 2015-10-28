'''
Linear Regression
Created on 2015/10/24/
@author: Alan HUANG
'''

from matplotlib.pyplot import plot, scatter, show
import numpy as np



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
    #线性模型
    #h = x0+x1+……xn
    
    h = 0
    for i in range(len(X)):
        h += X[i]*THETA[i]
    return h
    
def drawTrainingSet(THETA,X,Y):
    #根据给定的参数值，点集
    #画出对应的直线，还有样本的散点图

    #准备连续的点
    begin  = np.min(X.take(1,1))
    end = np.max(X.take(1,1))
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
    
    

def scaling(X):
    scaledX = X.copy()
    x_mean = np.mean(scaledX,axis=0)
    x_std = np.std(scaledX,axis=0)
    for row in scaledX:
        for i in range(len(row)):
            if x_std[i] == 0:
                row[i] = 1
            else:
                row[i] = float((row[i]-x_mean[i])/x_std[i])
    return (scaledX,x_mean,x_std)
     
def drawHypothesis(X,THETA,x_mean,x_std):
    #取出第二列的数据take(index，axis)
    x = X.take(1,1)
    
    begin = np.min(x)
    end = np.max(x)
    
    lineX = []
    line_x1 = np.linspace(begin,end,256,endpoint=True)
    #构成了
    for i in range(len(line_x1)):
        lineX.append([1,line_x1[i]])
    
    for line in lineX:
        for i in range(len(line)):
            if x_std[i] == 0:
                line[i] = 1
            else:
                line[i] = (line[i]-x_mean[i])/x_std[i]
    
    lineY = []
    for item in lineX:
        lineY.append(hypothesis(item, THETA))
        
    lineX = np.array(lineX)
    plot(line_x1,lineY)
    

#def normalEquation(X,Y):
     
def test1():  
    X = np.array([[1,65],[1,88],[1,95],[1,100],[1,130],[1,135]])
    Y = np.array([320985,440652,482770,518200,680600,665978])
    THETA = [0,0]
    alpha = 0.0001
    #如果不进行特征缩放的话，梯度下降法要花很久才能收敛
    traning(X, Y, THETA, alpha)
    print("theta is:",THETA)
    drawTrainingSet(THETA, X, Y)
    
def test2():
    #5个特征的情况（包含x0=1）
    X = np.array([[1,2104,5,1,45],[1,1416,3,2,40],[1,1534,3,2,30],[1,852,2,1,36]],dtype="f")
    Y = np.array([460,232,315,178],dtype="f")
    THETA = [0,0,0,0,0]
    alpha = 0.3
    #alpha 没法选到1
    scaledX = scaling(X)
    traning(scaledX, Y, THETA, alpha)
    print("theta is:",THETA)
    
def tempTest():
    #准备数据
    X = np.array([[1,65],[1,88],[1,95],[1,100],[1,130],[1,135]],dtype="f")
    Y = np.array([320985,440652,482770,518200,680600,665978],dtype="f")
    THETA = [0,0]
    alpha = 1
    #缩放数据
    scaleResult = scaling(X)
    scaledX = scaleResult[0]
    x_mean = scaleResult[1]
    x_std = scaleResult[2]
    #针对缩放后的数据进行训练
    traning(scaledX, Y, THETA, alpha)
    print("the trained theta is",THETA)
    
    #画出原本生成训练集的函数，和训练集中的样本点
    drawTrainingSet([178,5080], X, Y)
    #画出预测直线
    drawHypothesis(X, THETA, x_mean, x_std)
    
    show()
    
    
if __name__=="__main__":
    #测试在不进行特征缩放的情况下，训练theta，特征数为1
    #test1() 
    #test2()
    tempTest()
