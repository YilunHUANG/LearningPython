# NumPy

标签（空格分隔）： Python

---
[toc]

##创建数组
导入numpy：
```python
import numpy as np
```
创建一个numpy数组：
创建出来的是一个ndarray的对象（注：创建后的numpy数组是无法追加对象的）
```python
a = np.array([1,2,3,4])
```
查看数组对象的属性：
```python
a.ndim
a.shape
a.size #item的总数
a.dtype
a.itemsize #每个item实际占用的大小
```
创建特定形状的数组：
```python
a = np.zeros((3,4))
a = np.ones((3,4),dtype='float64') #默认的dtype即为float64
a = np.empty((3,4))
```
创建数列形式的数组：
```python
a = np.arange(100)
a = np.arange(10,20,5)
>>>array([10,15])
```
```python
a = np.linspace(0,1,3)
>>>array([0. ,0.5 ,1,])
```

##数组操作
对数组进行切片：(和原生数组一样)
```python
a[0,:] #取第0行
a[:,0] #取第0列
```
对数组进行重塑：
```python
a.reshape(2,2)
```
数组组合：
```python
np.hstack((a,b))
np.vstack((a,b))
```

复制数组：
```python
b = np.copy(a)
```
