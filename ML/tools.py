'''
Created on 2015年10月30日

@author: Alan HUANG
'''
import numpy as np
import numpy.linalg as linalg


def hypothesis(x,THETA):
    h = 0
    for i in range(len(THETA)):
        h += THETA[i]*x[i]
    return h

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


def normalEquation(X,Y):
    transX = np.transpose(X)
    #return (X^TX)^-1X^TY
    return np.dot(np.dot(linalg.inv(np.dot(transX,X)),transX),Y)

