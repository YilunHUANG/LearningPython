'''
Created on 2015年10月10日
@author: Alan HUANG
'''


'''lecture 2'''

'''
分支语句 条件 迭代
类型： 数字 字符串 布尔
表达式 类型转换
'''

##3*4
##3*"ab"
##"a"+"abc"
##str(3)+"ab"

'''
Python没有严格的类型检查
以下是在python2中可以通过的语句
运算符有优先顺序，如有疑问请用括号
'''

##"a"<3 
##4<"3"
##"4"<"3"
##
##9/5
##9%5
##3+4*5
##（3+4）*5

'''
给变量赋值，是从变量名到变量值的绑定
变量的类型 继承自他的值类型 并且是动态变化的
可以在任何地方使用变量
'''

##x=3
##x="abc"

'''
好的方法：写注释，给变量取个好名字
module的意思是模块
Braching Program 分支语句
if后面直接跟条件
'''

##x = 15
##if (x/2)*2 == x:
##    print("Even")
##else:
##    print("Odd")


##z = "b"
##if "x"<z:
##    print ("Hello")


'''
iteration or loops
boolean  combination: and, or, not
while后面直接跟条件
'''

##y=0
##x=3
##itersLeft = x 
##while itersLeft>0:
##    y=y+x
##    itersLeft = itersLeft-1
##print(y)



'''lecture 3'''

'''
构造循环（loop）的几个要素：
有能够用于计数的变量
在循环外初始化给变量
设置并测试给变量是否符合要求

设计程序的重要工具：流程图
Exhaustive enumeration 穷举法 并不一定是一个坏方法
'''

'''
for循环 range是一个内置方法
提供到index但不包含index的所有值
'''

##x = 10
##for i in range(1,x):
##    if x%i == 0:
##        print("diviser")

'''
Tuple: ordered sequence of elements
有序的元素序列
使用圆括号圈起来
'''

##test = (1,2,3,4,5)
##test[0]
##test[-1] #返还最后一个元素
##test[-2] #返回最后一个元素
##test[1:3]   #called slice 切片 返回一个切片后的副本
###但是要注意的是，最后一个index是不会包含进去的，返回(2,3)
##test[:3]
##test[1:]

##x = 100
##divisors = ()
##for i in range(1,x):
##    if x%i ==0:
##        divisors = divisors + (i,)
##print(divisors)

'''
字符串也是一个有序元素列
对其可以进行，选择[ ]和 切片操作
是序列就可以使用for循环取出所有的元素
将一个数各位相加的简单方法
'''

##s1 = "aaa"
##s2 = "bbb"
##s1 + s2
##s1[0]
##s1[2:4] #不包含4
##s1[:5]

##sumDigits = 0
##for c in str(1999):
##    sumDigits += int(c)
##print(sumDigits)



'''lecture 4'''

'''
函数抽象与递归简介
we have already learnt
assignment, conditionals, I/O, looping constructs(for, while)
turing complete, we can program anything but may be hard

we still need decomposition and abstraction
which means we need functions to
    block up into modules
    suppress details
    create new primitives 创建新的原语
关键词 def，return
即便函数不需要返回任何东西，最好也写上 return None，
这样实际上是在减少程序出错的可能
'''

##def sqrt(x):
##    if x>=0:
##        ans = 0
##        while ans**2<x:
##            ans +=1
##        if ans**2 ==x:
##            return ans
##        else:
##            print(x,"is not a perfect square")
##            return None
##    else:
##        print(x,"is not a none-nagative number")
##        return None
##        
##print(sqrt(-10))

##def solve(numLegs, numHeads):
##    ans = ()
##    for numPigs in range(0, numHeads+1):
##        for numChickens in range(0, numHeads+1):
##            numSpiders = numHeads - numPigs - numChickens
##            if 4*numPigs + 2*numChickens + 8*numSpiders == numLegs:
##                ans = ans + ((numPigs, numChickens, numSpiders),)
##    return ans
##
##def barnYard():
##    heads = int(input("Enter number of heads: "))
##    legs = int(input("Enter number of legs: "))
##    ans = solve(legs, heads)
##    if len(ans) == 0:
##        print("no such answer")
##    else:
##        print(ans)
##    
##
##barnYard()

'''
recursion
递归的意义在于：把一个问题分解成一个更简单的同类问题
首先找出base case，找出最简单的情况下的解决方法
然后将一个普通例子逐渐还原成base case
'''

##def isPalindrome(s):
##    if len(s)<=1:
##        return True
##    else:
##        return s[0]==s[-1] and isPalindrome(s[1:-1])



'''lecture 5'''
'''
字母L，long integer，处理时会比普通的效率低很多
一旦成为L，就一直在L上了
不过似乎python3并不会在结果后面加L，而且除法得到的结果变成了浮点类型

float类型
scientific notation科学记数法
mantissa尾数  exponent 指数
0<=mantissa<2
64bits 64位，1bit for sign符号
    11bits for exponent 指数
    52bits for mantissa 尾数

    于是乎只能表示到17 decimal digits（十进制），17位的精度。高于17为python不能表示（其他很多语言也是）

    为什么会出现误差，例如1/8=0.125=1.25*10^-1=1*2^-3；这是不会出现误差的
    然而，例如1/10=0.1=1*10^-1=？却没有办法用二进制精确表示，于是产生误差
    
    用双等号来检查浮点数是不是相等是有风险的，而实际上最好不要去检查值是否相等，
    而是去检查值是不是足够接近,例如abs(a**2-2.0)<epsilon
    可以自己创建一个函数例如 near 来判断约等于。
'''


##a = 2**1000
##b = 2**999
##c = a/b
##d = 0.1
##print(a)
##print(c) #2.0
##print(d)

##x = 0.0
##for i in range(10):
##    x = x+0.1
##print(x) #可以看出误差

##import math
##x = math.sqrt(2)
##print(x)
##print(x**2==2)
##print(x**2) #false

'''
求平方根
successive approximation逐次近似
    guess = initial_guess
    for iter in range(100);
         if f(guess) close enough: return guss
         else: guess = better guess
Bisection method二分法
    有一系列线性可能结果，每次猜想（检测）中间的值

iteration method一个迭代的方法
'''




'''自己写的'''
##import math
##def squareRootBi(x, epsilon):
##    low = 0
##    high = x
##    
##    for i in range(100):
##        mid = (low+high)/2.0
##        if  abs(mid**2-x) < epsilon:
##            return mid
##        else:
##            if mid**2>x:
##                high = mid
##            else:
##                low = mid
##
##    return None

'''老师写的'''

##import math
##def squareRootBi(x, epsilon):
##    '''
##        Assume x>=0 and epsilon >0
##        Return y s.t. y*y is within epsilon of x
##    '''
##    assert x >=0, "x must be non-negative, not "+str(x)
##    assert epsilon >0, "epsilon must be positive, not "+str(epsilon)
##
##    low = 0
##    #high = x 这样写是有bug的，无法计算小于1的分数
##    high = max(x,1)
##    guess = (low + high)/2.0
##    ctr = 1
##    while abs(guess**2 - x)>epsilon and ctr <= 100:
##        if guess**2 <x:
##            low = guess
##        else:
##            high = guess
##        guess = (low + high)/2.0
##        ctr +=1
##    assert ctr<=100, "Iteration count exceed"
##    print("Bi method. Num. iterations:",ctr,"Estimate",guess)
##    return guess
##
##squareRootBi(9, 0.0001)
##squareRootBi(1, 0.0001)
##squareRootBi(0.25,0.0001)




'''lecture 6'''
'''
regression testing
speed of convergence 什么时候循环结束

derivative
newton's method
newton raphson
数组 list
'''
##import math
##def squareRootNR(x, epsilon):
##    assert x>=0, "x must be a non-nagtive number ,not "+str(x)
##    assert epsilon > 0, "epsilon must be positive, not "+ str(epsilon)
##    x = float(x)
##    guess = x/2.0
##    diff = guess**2 -x
##    ctr = 1
##    while abs(diff) > epsilon and ctr <= 100:
##        guess = guess - diff/(2.0*guess)
##        diff = guess**2 -x
##        ctr +=1
##    assert ctr<=100, "Iteration count exceeded"
##    print("NR method. Num. iteration:", ctr, "Estimate", guess)
##    return guess
##
##squareRootNR(1234567,0.0001)
##squareRootBi(1234567,0.0001)
         
     
'''lecture 7'''
'''
dictionaries字典
{}大括号
mutable 可改变
元素无序 key value pair
Hashing， constant time when searching，fast

pseudo code，写伪代码是规划程序的很好方式，不用考虑实现的细节，让思路清晰，连贯
efficiency: choice of algorithm
map problems into class of algorithms

focus on worse case
'''

def showDicts():
    EtoF = {"one":"un", "soccer":"football"}
    print (EtoF["soccer"])
    print (EtoF[0])
    print(EtoF)











































