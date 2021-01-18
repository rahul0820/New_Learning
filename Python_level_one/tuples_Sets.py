# Simple Tuple - Tuples are Immutable but Lists are Mutable - It can hold multitype data chars
t = ('a','b','c')
print(t[0])

t = ('a',True,123)
print(t)

# Sets 
x=set()
x.add(1)
x.add(2)
print(x)

# Picking out unique elements only
x=set()
x.add(1)
x.add(2)
x.add(9)
x.add(9)
print(x)

# Picking out unique elements only

new=set([1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,6,6,6,7])
print(new)