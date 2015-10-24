import collections
import math

'''
对于给定的一个测试用例的特征向量，与权向量计算内积，
使用Sigmoid函数，根据内积值计算出预测值y=1或y=-1的概率

对于每一个测试用例，当前的权向量都能给出一个概率值
如何更新权向量w
'''

def dot_product(w, x):
    dp = 0
    for k,v in x.items():
        dp += w.get(k,0) * v
    return dp

def probability(w, x):
    #计算 P(y=1)
    dp = dor_product(w,x)
    prob = 1/(math.exp(-dp))
    if prob >-100:
        return prob
    else:
        return 0
    
def update_LR(w, x, y, eta=1):
    y = (y+1)/2
    p = probability(w,x)
    g = y - p
    for k,v in x.items():
        w[f] = eta*g*v
    
    

x1 = {"@bias":1, "hi_darl":1, "darl_my":1, "my_photo":1, "photo_attach":1, "attach_file":1}
x2 = {"@bias":1, "hi_mark":1, "mark_kyoto":1, "kyoto_photo":1, "photo_attach":1, "attach_file":1}
y1 = +1
y2 = -1

w = collections.defaultdict(float)
print(dot_product(w, x1))



