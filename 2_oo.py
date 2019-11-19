def add(n1, n2):
    return n1 + n2
# 心知肚明哪些可以做
print(add(3, 5))
print(add(3, 2.2))
print(add("hello", "abd"))
# print(add("hello", 3))
# 沒加():紙   有加(): 紙->執行
b = add
print(b(3, 5))

c = print
c("hello")

def test():
    return print

test()("hello")

# 預設值
def add(n1, n2, digit=2, mul=1):
    return mul * round(n1+n2, digit)
print(add(3.2, 5.12341234, mul=2))

