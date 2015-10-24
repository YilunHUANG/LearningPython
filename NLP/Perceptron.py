import collections

def dot_product(w, x):
    '''
    w: weight vector; dict; feature value
    x: feature vector; dict; feature value
    '''
    dp = 0
    for f, v in x.items():
        dp += w.get(f, 0) * v
        #如果没get到feature名，则返回默认值0.，如果不指定默认值会返回None
    return dp

def update_perceptron(w, x, y):
    dp = dot_product(w, x)
    if dp*y <=0:
        for f, v in x.items():
            w[f] += y * v
            #w是一个defaultdict类型，用[key]访问w，当键不存在时会自动创建

x1 = {"@bias":1, "hi_darl":1, "darl_my":1, "my_photo":1, "photo_attach":1, "attach_file":1}
x2 = {"@bias":1, "hi_mark":1, "mark_kyoto":1, "kyoto_photo":1, "photo_attach":1, "attach_file":1}
y1 = +1
y2 = -1


w = collections.defaultdict(float) #构造一个空dict
print(w)
update_perceptron(w, x1, y1)
print(w)
print(dot_product(w, x2))
update_perceptron(w, x2, y2)
print(w)


        
        
