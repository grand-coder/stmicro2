# 物件導向

## 函式定義

自行定義可以使用的函式

### 普通函式

```python
def add(n1, n2):
  return n1 + n2
```

### 有初始值的函式

一個參數有初始值了以後，後續的參數都要有！

```python
def add(n1, n2, digit=2):
  return round(n1 + n1, digit)
```

## 濃縮函式(Packing)

### *args

打一個 * 會把所有帶入的參數組合成一個 tuple

```python
def add(*args):
  print(args)
  return sum(args)
  
print(add(2, 1, 3, 4)
```

### **kwargs

打兩個 ** 會把所有帶入的參數組合成一個字典

```python
def add(n1, n2, **kwargs):
  result = n1 + n2
  if "mul" in kwargs:
    result = result * kwargs["mul"]
  if "div" in kwargs and not kwargs["div"] == 0:
    result = result / kwargs["div"]
  return result
  
print(add(3, 4, mul=2, div=3)
```

### 組合 *args 和 *kwargs

```python
def add(*args, **kwargs):
  pass

print(add(3, 4, 5, 6, mul=2, div=3)
```

### 函式也為物件

python 的函式就跟整數，字串一樣，你可以想像成  

> 函式名字  =  一份SOP(由程式組成)

> 加入 () 代表對這個SOP做一個執行的動作

```python
# 例子1. 將print背後的東西給個新名字, 再()執行
b = print
b("hello)
```

```python
# 例子2. 將函式當成一個如同整數的東西回傳
def test():
  return print
  
test()("hello")
```

 ## 物件導向
 
 物件導向讓你可以定義出自己想要的資料樣貌，並且大量的創造
 
 ### 基本定義
 
 ```python
 class Person:
 
    # 物件導向最重要的函式, 初始化所有的資料
    def __init__(self, name, height, weight):
        # 你的物件擁有的屬性
        self.name = name
        self.height = height
        self.weight = weight
        
    # 接下來你可以定義你自己想要的函式
    def getbmi(self):
        return self.weight / (self.height / 100) ** 2
        
    # 以__開頭和結尾的是python特殊的函式
    # 你可以藉由覆蓋他來得到自己想要的行為
    # __str__是我們平常使用str()和print()所得到的東西
    def __str__(self):
        return "name:{}\theight:{}\tweight:{}".format(self.name, self.height, self.weight)
        
    # __repr__是如果你在群集裡被打印的時候所使用的函式
    def __repr__(self):
        return  self.__str__()
    
    
# 創造物件
p1 = Person("Elwing", 175, 75)
print(p1.getbmi())
```
