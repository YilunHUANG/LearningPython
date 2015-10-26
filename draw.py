from pylab import *
import random

def generate_y(x):
    y = []
    for i in x:
        rand = random.uniform(-20000,20000)
        y.append(5080*i+178+rand)
    return y

def line(x):
    y = []
    for i in x:
        y.append(5080*i+178)
    return y

def h(thetas,x):
    theta0 = thetas[0]
    theta1 = thetas[1]
    y = []
    for i in x:
        y.append(theta1*i+theta0)
    return y


def training(thetas,x, y):
    theta0 = thetas[0]
    theta1 = thetas[1]

    num = 0
    learningRate = 0.0001
    pds = p_d(thetas,x,y)

    while (abs(pds[0])>0.1 and abs(pds[1])>0.1) or num<10000:
        theta0 = theta0 - pds[0]*learningRate
        theta1 = theta1 - pds[1]*learningRate
        pds = p_d([theta0,theta1],x,y)
        num += 1

    return [theta0,theta1]
        
    
def p_d(thetas,train_x,train_y): #partial derivative
    theta0 = thetas[0]
    theta1 = thetas[1]
    pd0 = 0
    pd1 = 0

    m = len(train_x)

    for i in range(m):
        pd0 =  pd0+theta0+theta1*train_x[i]-train_y[i]
        pd1 = pd1+train_x[i]*(theta0+theta1*train_x[i]-train_y[i])
        
    pd0 = pd0/m
    pd1 = pd1/m
    return [pd0,pd1]

train_x = [65, 88, 95, 100, 130, 135]
train_y = generate_y(train_x)
X = np.linspace(50,150, 256, endpoint=True)
Y = line(X)

thetas = training([1,1],train_x,train_y)
y = h(thetas,X)

#print(p_d([1,1],train_x,train_y))
#print(training([1,1],train_x,train_y))

scatter(train_x,train_y) #散点
plot(X,Y) #线
plot(X,y)
show()





        
    




