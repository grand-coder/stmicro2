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

 
